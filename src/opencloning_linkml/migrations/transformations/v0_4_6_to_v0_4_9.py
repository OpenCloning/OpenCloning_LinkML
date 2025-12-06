from ..model_archive.v0_4_9 import (
    CloningStrategy as new_CloningStrategy,
    NCBISequenceSource,
    GenomeCoordinatesSource as new_GenomeCoordinatesSource,
)
from ..model_archive.v0_4_6 import (
    CloningStrategy as old_CloningStrategy,
    GenomeCoordinatesSource as old_GenomeCoordinatesSource,
)

from copy import deepcopy


def migrate_manually_typed_source(source: dict) -> dict:
    new_source = deepcopy(source)
    for key in ["overhang_crick_3prime", "overhang_watson_3prime", "user_input", "circular"]:
        if key in new_source:
            del new_source[key]
    return new_source


def migrate_genbank_repository_id(source: dict) -> dict:
    new_source = {key: value for key, value in source.items() if key not in ["type", "repository_name"]}
    return NCBISequenceSource(**new_source).model_dump()


def migrate_repository_id_source(source: dict) -> dict:
    new_source = deepcopy(source)
    del new_source["repository_name"]
    return new_source


def migrate_source(source: dict) -> dict:
    if source["type"] == "ManuallyTypedSource":
        return migrate_manually_typed_source(source)
    elif source["type"] == "RepositoryIdSource" and source["repository_name"] == "genbank":
        return migrate_genbank_repository_id(source)
    elif "repository_name" in source:
        return migrate_repository_id_source(source)
    elif source["type"] == "GenomeCoordinatesSource":
        return migrate_genome_coordinates_source(source)
    elif source["type"] == "CollectionSource":
        source["options"] = [{**o, "source": migrate_source(o["source"])} for o in source["options"]]
    return source


def migrate_genome_coordinates_source(source: dict) -> dict:
    old_source = old_GenomeCoordinatesSource.model_validate(source)
    if old_source.strand == -1:
        location = f"complement({old_source.start}..{old_source.end})"
    else:
        location = f"{old_source.start}..{old_source.end}"

    excluded_fields = ["type", "strand", "start", "end", "sequence_accession"]
    extra_fields = {key: value for key, value in source.items() if key not in excluded_fields}
    return new_GenomeCoordinatesSource(
        coordinates=location, repository_id=old_source.sequence_accession, **extra_fields
    ).model_dump()


def migrate_0_4_6_to_0_4_9(data: dict) -> dict:
    """Migrate data from version 0.4.6 to 0.4.9."""
    old = old_CloningStrategy.model_validate(data)
    old_dict = old.model_dump()
    old_dict["sources"] = [migrate_source(s) for s in old_dict["sources"]]
    new = new_CloningStrategy.model_validate(old_dict)
    new.schema_version = "0.4.9"
    return new.model_dump()
