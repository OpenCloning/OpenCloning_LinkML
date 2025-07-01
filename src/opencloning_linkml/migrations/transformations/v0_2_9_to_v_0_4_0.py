from ..model_archive.v0_2_9 import CloningStrategy as old_CloningStrategy
from ..model_archive.v0_4_0 import CloningStrategy as new_CloningStrategy
from copy import deepcopy


def remap_source(input_source: dict, sequence_id_map: dict, primer_id_map: dict):
    """Remap ids of sequences and primers in source fields."""
    source = deepcopy(input_source)
    # Normalise input and assembly fields
    if source["input"] is None:
        source["input"] = []
    if "assembly" in source and source["assembly"] is None:
        source["assembly"] = []

    # Remap input fields
    source["input"] = [sequence_id_map[sequence_id] for sequence_id in source["input"]]

    # Remap assembly fields and CollectionSource options
    if source["type"] == "PCRSource" and len(source["assembly"]):
        fwd, tmp, rvs = source["assembly"]
        fwd["sequence"] = primer_id_map[fwd["sequence"]]
        tmp["sequence"] = sequence_id_map[tmp["sequence"]]
        rvs["sequence"] = primer_id_map[rvs["sequence"]]
    elif source["type"] == "CollectionSource":
        for option in source["options"]:
            option["source"] = remap_source(option["source"], sequence_id_map, primer_id_map)
    elif "assembly" in source:
        for assembly_fragment in source["assembly"]:
            assembly_fragment["sequence"] = sequence_id_map[assembly_fragment["sequence"]]
    elif source["type"] == "OligoHybridizationSource":
        source["forward_oligo"] = primer_id_map[source["forward_oligo"]]
        source["reverse_oligo"] = primer_id_map[source["reverse_oligo"]]

    # Remap guides field in CRISPR
    if source["type"] == "CRISPRSource":
        source["guides"] = [primer_id_map[guide] for guide in source["guides"]]

    return source


def migrate_source(input_source: dict):
    source = deepcopy(input_source)
    source_inputs = []
    is_assembly = "assembly" in source
    if source["type"] == "CollectionSource":
        for option in source["options"]:
            option["source"] = migrate_source(option["source"])
    elif is_assembly:
        for assembly_fragment in source["assembly"]:
            new_assembly_fragment = assembly_fragment.copy()
            source_inputs.append(new_assembly_fragment)
        del source["assembly"]
    elif source["type"] == "OligoHybridizationSource":
        source_inputs.extend(
            [
                {
                    "sequence": source["forward_oligo"],
                },
                {
                    "sequence": source["reverse_oligo"],
                },
            ]
        )
        del source["forward_oligo"]
        del source["reverse_oligo"]
    else:
        for sequence_id in source["input"]:
            source_inputs.append(
                {
                    "sequence": sequence_id,
                }
            )

    for source_input in source_inputs:
        source_input["type"] = "AssemblyFragment" if is_assembly else "SourceInput"

    # Special case for CRISPR, move guides to input field and drop guides field
    if source["type"] == "CRISPRSource":
        source_inputs.extend([{"sequence": guide, "type": "SourceInput"} for guide in source["guides"]])
        del source["guides"]

    # Drop output field
    del source["output"]
    source["input"] = source_inputs
    return source


def migrate_0_2_9_to_0_4_0(data: dict) -> dict:
    """Migrate data from version 0.2.9 to 0.4.0."""
    old = old_CloningStrategy.model_validate(data)
    old_dict = old.model_dump()

    # Remap ids
    primer_id_map = {}
    sequence_id_map = {}

    sorted_sources = sorted(old_dict["sources"], key=lambda x: x["id"])
    for i, source in enumerate(sorted_sources):
        source["id"] = i + 1
        if source["output"] is not None:
            # The sequence id is now the same as the source id
            sequence_id_map[source["output"]] = i + 1

    for sequence in old_dict["sequences"]:
        sequence["id"] = sequence_id_map[sequence["id"]]

    # Ids of primers cannot clash with sequences anymore
    latest_id = len(sorted_sources)
    for i, primer in enumerate(old_dict["primers"]):
        primer_id_map[primer["id"]] = latest_id + i + 1
        primer["id"] = latest_id + i + 1

    # Now remap ids of sequences and primers in source fields
    old_dict["sources"] = [remap_source(s, sequence_id_map, primer_id_map) for s in old_dict["sources"]]

    # Convert input fields from list of integers to list of SourceInput objects
    # and drop removed fields
    old_dict["sources"] = [migrate_source(s) for s in old_dict["sources"]]

    new = new_CloningStrategy.model_validate(old_dict)
    new.schema_version = "0.4.0"

    return new.model_dump()
