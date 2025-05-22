from ..model_archive.v0_2_6_1 import CloningStrategy as old_CloningStrategy
from ..model_archive.v0_2_8 import CloningStrategy as new_CloningStrategy


def migrate_0_2_6_1_to_0_2_8(data: dict) -> dict:
    """Migrate data from version 0.2.6.1 to 0.2.8."""
    old = old_CloningStrategy.model_validate(data)
    new = new_CloningStrategy.model_validate(old.model_dump())
    new.schema_version = "0.2.8"
    return new.model_dump()
