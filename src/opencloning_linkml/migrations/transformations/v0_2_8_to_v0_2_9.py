from ..model_archive.v0_2_8 import CloningStrategy as old_CloningStrategy
from ..model_archive.v0_2_9 import CloningStrategy as new_CloningStrategy


def migrate_0_2_8_to_0_2_9(data: dict) -> dict:
    """Migrate data from version 0.2.8 to 0.2.9."""
    old = old_CloningStrategy.model_validate(data)
    old_dict = old.model_dump()
    for source in old_dict["sources"]:
        if "assembly" in source and source["assembly"] is not None:
            for assembly_fragment in source["assembly"]:
                for side in ["left_location", "right_location"]:
                    if assembly_fragment[side] is not None:
                        location = assembly_fragment[side]
                        if location["start"] != location["end"]:
                            assembly_fragment[side] = f"{location['start'] + 1}..{location['end']}"
                        else:
                            assembly_fragment[side] = f"{location['start']}^{location['start'] + 1}"
        elif source["type"] == "UploadedFileSource" and "coordinates" in source:
            if source["coordinates"] is not None:
                source["coordinates"] = f"{source['coordinates']['start'] + 1}..{source['coordinates']['end']}"

    new = new_CloningStrategy.model_validate(old_dict)
    new.schema_version = "0.2.9"

    return new.model_dump()
