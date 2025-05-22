from ._models import *  # noqa: F403,F401
from opencloning_linkml._version import __version__
from typing import Optional
from pydantic import Field


class CloningStrategy(CloningStrategy):  # noqa: F405
    schema_version: Optional[str] = Field(
        default=__version__,
        description="""The version of the schema that was used to generate this cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "schema_version", "domain_of": ["CloningStrategy"]}},
    )
