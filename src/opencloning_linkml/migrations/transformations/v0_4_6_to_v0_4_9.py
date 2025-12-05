from ..model_archive.v0_4_9 import CloningStrategy as new_CloningStrategy
from ..model_archive.v0_4_6 import CloningStrategy as old_CloningStrategy

from copy import deepcopy


def migrate_manually_typed_source(source: dict) -> dict:
    new_source = deepcopy(source)
    for key in ["overhang_crick_3prime", "overhang_watson_3prime", "user_input", "circular"]:
        if key in new_source:
            del new_source[key]
    return new_source


def migrate_source(source: dict) -> dict:
    if source["type"] == "ManuallyTypedSource":
        return migrate_manually_typed_source(source)
    return source


def migrate_0_4_6_to_0_4_9(data: dict) -> dict:
    """Migrate data from version 0.4.6 to 0.4.9."""
    old = old_CloningStrategy.model_validate(data)
    old_dict = old.model_dump()
    old_dict["sources"] = [migrate_source(s) for s in old_dict["sources"]]
    new = new_CloningStrategy.model_validate(old_dict)
    new.schema_version = "0.4.9"
    return new.model_dump()
