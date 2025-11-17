from ..model_archive.v0_4_6 import CloningStrategy as new_CloningStrategy
from copy import deepcopy


def migrate_0_4_0_to_0_4_6(data: dict) -> dict:
    """
    Migrate data from version 0.4.0 to 0.4.6.

    In this case, it's just removing the output field from the sources,
    which were sometimes wrongly added in the frontend.

    https://github.com/OpenCloning/OpenCloning_LinkML/issues/63
    """
    new_data = deepcopy(data)

    for source in new_data["sources"]:
        if "output" in source:
            del source["output"]

    new = new_CloningStrategy.model_validate(new_data)
    new.schema_version = "0.4.6"

    return new.model_dump()
