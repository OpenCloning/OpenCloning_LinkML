from __future__ import annotations

import re
import sys
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Any, ClassVar, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )
    pass


class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta(
    {
        "default_prefix": "opencloning_linkml",
        "default_range": "string",
        "description": "A LinkML data model for OpenCloning",
        "id": "https://opencloning.github.io/OpenCloning_LinkML",
        "imports": ["linkml:types"],
        "license": "MIT",
        "name": "OpenCloning_LinkML",
        "prefixes": {
            "IAO": {"prefix_prefix": "IAO", "prefix_reference": "http://purl.obolibrary.org/obo/IAO_"},
            "NCIT": {"prefix_prefix": "NCIT", "prefix_reference": "http://purl.obolibrary.org/obo/NCIT_"},
            "OBI": {"prefix_prefix": "OBI", "prefix_reference": "http://purl.obolibrary.org/obo/OBI_"},
            "PATO": {"prefix_prefix": "PATO", "prefix_reference": "http://purl.obolibrary.org/obo/PATO_"},
            "biolink": {"prefix_prefix": "biolink", "prefix_reference": "https://w3id.org/biolink/"},
            "bioschemas": {"prefix_prefix": "bioschemas", "prefix_reference": "https://bioschemas.org/"},
            "example": {"prefix_prefix": "example", "prefix_reference": "https://example.org/"},
            "linkml": {"prefix_prefix": "linkml", "prefix_reference": "https://w3id.org/linkml/"},
            "opencloning_linkml": {
                "prefix_prefix": "opencloning_linkml",
                "prefix_reference": "https://opencloning.github.io/OpenCloning_LinkML/",
            },
            "schema": {"prefix_prefix": "schema", "prefix_reference": "http://schema.org/"},
        },
        "see_also": ["https://pypi.org/project/opencloning-linkml/"],
        "source_file": "src/opencloning_linkml/schema/opencloning_linkml.yaml",
        "title": "OpenCloning_LinkML",
        "types": {
            "version_number": {
                "description": "A version number",
                "exact_mappings": ["IAO:0000129"],
                "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
                "name": "version_number",
                "typeof": "string",
            }
        },
    }
)


class RepositoryName(str, Enum):
    addgene = "addgene"
    """
    Addgene
    """
    genbank = "genbank"
    """
    GenBank
    """
    benchling = "benchling"
    """
    Benchling
    """
    snapgene = "snapgene"
    """
    SnapGene plasmid library
    """
    euroscarf = "euroscarf"
    """
    Euroscarf (plasmids only)
    """
    igem = "igem"
    """
    iGEM collection
    """
    wekwikgene = "wekwikgene"
    """
    WekWikGene
    """
    seva = "seva"
    """
    SEVA (Standard European Vector Architecture)
    """


class Collection(str, Enum):
    AddgenePlasmid = "AddgenePlasmid"
    """
    A plasmid from Addgene
    """
    OligoPair = "OligoPair"
    """
    A pair of oligonucleotides for hybridization
    """


class SequenceFileFormat(str, Enum):
    fasta = "fasta"
    genbank = "genbank"
    snapgene = "snapgene"
    embl = "embl"


class AddgeneSequenceType(str, Enum):
    depositor_full = "depositor-full"
    """
    Full sequence of the plasmid submitted by the depositor
    """
    addgene_full = "addgene-full"
    """
    Full sequence of the plasmid performed by Addgene
    """


class GatewayReactionType(str, Enum):
    LR = "LR"
    """
    LR reaction
    """
    BP = "BP"
    """
    BP reaction
    """


class AnnotationTool(str, Enum):
    plannotate = "plannotate"


class AssociatedFileType(str, Enum):
    Sequencing_file = "Sequencing file"
    """
    A file containing sequencing data
    """


class CollectionOptionType(str, Enum):
    OligoPair = "OligoPair"
    """
    A pair of oligonucleotides for hybridization
    """
    AddgenePlasmid = "AddgenePlasmid"
    """
    A plasmid from Addgene
    """


class NamedThing(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"class_uri": "schema:Thing", "from_schema": "https://opencloning.github.io/OpenCloning_LinkML"}
    )

    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class Sequence(NamedThing):
    """
    Represents a sequence
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "class_uri": "bioschemas:DNA",
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
        }
    )

    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )
    type: Literal["Sequence"] = Field(
        default="Sequence",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )


class TemplateSequence(Sequence):
    """
    Represents a sequence that is part of a template, where the actual sequence content will be determined by the user's actions
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the sequence is circular or linear""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    primer_design: Optional[str] = Field(
        default=None,
        description="""Can be used to indicate the intended primer design for this sequence in the template""",
        json_schema_extra={"linkml_meta": {"alias": "primer_design", "domain_of": ["TemplateSequence"]}},
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )
    type: Literal["TemplateSequence"] = Field(
        default="TemplateSequence",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )


class TextFileSequence(Sequence):
    """
    A sequence (may have features) defined by the content of a text file
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {
                "overhang_crick_3prime": {"ifabsent": "int(0)", "name": "overhang_crick_3prime"},
                "overhang_watson_3prime": {"ifabsent": "int(0)", "name": "overhang_watson_3prime"},
                "sequence_file_format": {"name": "sequence_file_format", "required": True},
            },
        }
    )

    sequence_file_format: SequenceFileFormat = Field(
        default=...,
        description="""The format of a sequence file""",
        json_schema_extra={
            "linkml_meta": {"alias": "sequence_file_format", "domain_of": ["TextFileSequence", "UploadedFileSource"]}
        },
    )
    overhang_crick_3prime: Optional[int] = Field(
        default=0,
        description="""Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "overhang_crick_3prime",
                "domain_of": ["TextFileSequence", "ManuallyTypedSource", "OligoHybridizationSource"],
                "ifabsent": "int(0)",
            }
        },
    )
    overhang_watson_3prime: Optional[int] = Field(
        default=0,
        description="""The equivalent of `overhang_crick_3prime` but for the watson strand""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "overhang_watson_3prime",
                "domain_of": ["TextFileSequence", "ManuallyTypedSource"],
                "ifabsent": "int(0)",
            }
        },
    )
    file_content: Optional[str] = Field(
        default=None, json_schema_extra={"linkml_meta": {"alias": "file_content", "domain_of": ["TextFileSequence"]}}
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )
    type: Literal["TextFileSequence"] = Field(
        default="TextFileSequence",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )


class Primer(Sequence):
    """
    An oligonucleotide or primer
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    name: Optional[str] = Field(
        default=None,
        description="""A human-readable name for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": ["Primer", "CollectionOption", "CollectionOptionInfo"],
                "slot_uri": "schema:name",
            }
        },
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    sequence: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "sequence",
                "domain_of": ["Primer", "AssemblyFragment", "PlannotateAnnotationReport"],
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )
    type: Literal["Primer"] = Field(
        default="Primer",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )

    @field_validator("sequence")
    def pattern_sequence(cls, v):
        pattern = re.compile(r"^[acgtACGT]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sequence format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sequence format: {v}"
            raise ValueError(err_msg)
        return v


class SequenceCut(ConfiguredBaseModel):
    """
    Represents a cut in a DNA sequence
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    cut_watson: int = Field(
        default=...,
        description="""The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.""",
        json_schema_extra={"linkml_meta": {"alias": "cut_watson", "domain_of": ["SequenceCut"]}},
    )
    overhang: int = Field(
        default=...,
        description="""The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.""",
        json_schema_extra={"linkml_meta": {"alias": "overhang", "domain_of": ["SequenceCut"]}},
    )


class RestrictionSequenceCut(SequenceCut):
    """
    Represents a cut in a DNA sequence that is made by a restriction enzyme
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {"restriction_enzyme": {"name": "restriction_enzyme", "required": True}},
        }
    )

    restriction_enzyme: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "restriction_enzyme",
                "domain_of": ["RestrictionSequenceCut"],
                "exact_mappings": ["OBI:0000732"],
            }
        },
    )
    cut_watson: int = Field(
        default=...,
        description="""The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.""",
        json_schema_extra={"linkml_meta": {"alias": "cut_watson", "domain_of": ["SequenceCut"]}},
    )
    overhang: int = Field(
        default=...,
        description="""The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.""",
        json_schema_extra={"linkml_meta": {"alias": "overhang", "domain_of": ["SequenceCut"]}},
    )


class Source(NamedThing):
    """
    Represents the source of a sequence
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "class_uri": "schema:CreateAction",
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
        }
    )

    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["Source"] = Field(
        default="Source",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class DatabaseSource(Source):
    """
    Represents the source of a sequence that is identified by a database id
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {"database_id": {"name": "database_id", "required": True}},
        }
    )

    database_id: int = Field(
        default=...,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["DatabaseSource"] = Field(
        default="DatabaseSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class CollectionSource(Source):
    """
    Represents a collection of possible sources in a template
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    category_id: Optional[str] = Field(
        default=None,
        description="""The identifier of the category of the part in the template""",
        json_schema_extra={"linkml_meta": {"alias": "category_id", "domain_of": ["CollectionSource"]}},
    )
    title: str = Field(
        default=...,
        description="""The title of the category""",
        json_schema_extra={"linkml_meta": {"alias": "title", "domain_of": ["CollectionSource"]}},
    )
    description: Optional[str] = Field(
        default=None,
        description="""A description of the category""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["CollectionSource", "CollectionOptionInfo", "CloningStrategy"],
            }
        },
    )
    image: Optional[list[str]] = Field(
        default=None,
        description="""URL and size of the image representing this category. For images with size specification, this is a list with two elements: [url, size].""",
        json_schema_extra={"linkml_meta": {"alias": "image", "domain_of": ["CollectionSource"]}},
    )
    options: Optional[list[CollectionOption]] = Field(
        default=None,
        description="""The options available in this category.""",
        json_schema_extra={"linkml_meta": {"alias": "options", "domain_of": ["CollectionSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["CollectionSource"] = Field(
        default="CollectionSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class CollectionOption(ConfiguredBaseModel):
    """
    Represents an option in a collection
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {"name": {"name": "name", "required": True}},
        }
    )

    name: str = Field(
        default=...,
        description="""A human-readable name for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": ["Primer", "CollectionOption", "CollectionOptionInfo"],
                "slot_uri": "schema:name",
            }
        },
    )
    source: Union[
        Source,
        DatabaseSource,
        CollectionSource,
        ManuallyTypedSource,
        UploadedFileSource,
        RepositoryIdSource,
        GenomeCoordinatesSource,
        SequenceCutSource,
        AssemblySource,
        OligoHybridizationSource,
        PolymeraseExtensionSource,
        AnnotationSource,
        ReverseComplementSource,
        PCRSource,
        LigationSource,
        HomologousRecombinationSource,
        GibsonAssemblySource,
        InFusionSource,
        OverlapExtensionPCRLigationSource,
        InVivoAssemblySource,
        RestrictionAndLigationSource,
        GatewaySource,
        CreLoxRecombinationSource,
        CRISPRSource,
        RestrictionEnzymeDigestionSource,
        AddgeneIdSource,
        WekWikGeneIdSource,
        SEVASource,
        BenchlingUrlSource,
        SnapGenePlasmidSource,
        EuroscarfSource,
        IGEMSource,
    ] = Field(
        default=...,
        description="""The source of the sequence for this option""",
        json_schema_extra={"linkml_meta": {"alias": "source", "domain_of": ["CollectionOption"]}},
    )
    info: Optional[CollectionOptionInfo] = Field(
        default=None,
        description="""Additional information about this option""",
        json_schema_extra={"linkml_meta": {"alias": "info", "domain_of": ["CollectionOption"]}},
    )


class CollectionOptionInfo(ConfiguredBaseModel):
    """
    Additional information about a collection option
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {"name": {"name": "name", "required": False}},
        }
    )

    name: Optional[str] = Field(
        default=None,
        description="""A human-readable name for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "name",
                "domain_of": ["Primer", "CollectionOption", "CollectionOptionInfo"],
                "slot_uri": "schema:name",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A description of the option""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["CollectionSource", "CollectionOptionInfo", "CloningStrategy"],
            }
        },
    )
    type: Optional[CollectionOptionType] = Field(
        default=None,
        description="""The type of the option, this is redundant with the type of the source, and could be removed.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    resistance: Optional[str] = Field(
        default=None,
        description="""The antibiotic resistance of the plasmid""",
        json_schema_extra={"linkml_meta": {"alias": "resistance", "domain_of": ["CollectionOptionInfo"]}},
    )
    well: Optional[str] = Field(
        default=None,
        description="""The well position in the kit plate""",
        json_schema_extra={"linkml_meta": {"alias": "well", "domain_of": ["CollectionOptionInfo"]}},
    )


class ManuallyTypedSource(Source):
    """
    Represents the source of a sequence that is manually typed by the user
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {
                "overhang_crick_3prime": {"ifabsent": "int(0)", "name": "overhang_crick_3prime"},
                "overhang_watson_3prime": {"ifabsent": "int(0)", "name": "overhang_watson_3prime"},
            },
        }
    )

    overhang_crick_3prime: Optional[int] = Field(
        default=0,
        description="""Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "overhang_crick_3prime",
                "domain_of": ["TextFileSequence", "ManuallyTypedSource", "OligoHybridizationSource"],
                "ifabsent": "int(0)",
            }
        },
    )
    overhang_watson_3prime: Optional[int] = Field(
        default=0,
        description="""The equivalent of `overhang_crick_3prime` but for the watson strand""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "overhang_watson_3prime",
                "domain_of": ["TextFileSequence", "ManuallyTypedSource"],
                "ifabsent": "int(0)",
            }
        },
    )
    user_input: str = Field(
        default=..., json_schema_extra={"linkml_meta": {"alias": "user_input", "domain_of": ["ManuallyTypedSource"]}}
    )
    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the sequence is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["ManuallyTypedSource"] = Field(
        default="ManuallyTypedSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("user_input")
    def pattern_user_input(cls, v):
        pattern = re.compile(r"^[acgtACGT]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid user_input format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid user_input format: {v}"
            raise ValueError(err_msg)
        return v


class UploadedFileSource(Source):
    """
    Represents the source of a sequence that is uploaded as a file
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {"sequence_file_format": {"name": "sequence_file_format", "required": True}},
        }
    )

    sequence_file_format: SequenceFileFormat = Field(
        default=...,
        description="""The format of a sequence file""",
        json_schema_extra={
            "linkml_meta": {"alias": "sequence_file_format", "domain_of": ["TextFileSequence", "UploadedFileSource"]}
        },
    )
    file_name: Optional[str] = Field(
        default=None,
        description="""The name of the file""",
        json_schema_extra={
            "linkml_meta": {"alias": "file_name", "domain_of": ["UploadedFileSource", "AssociatedFile"]}
        },
    )
    index_in_file: Optional[int] = Field(
        default=None,
        description="""The index of the sequence in the file""",
        json_schema_extra={"linkml_meta": {"alias": "index_in_file", "domain_of": ["UploadedFileSource"]}},
    )
    circularize: Optional[bool] = Field(
        default=None,
        description="""Whether the sequence should be circularized (FASTA only)""",
        json_schema_extra={"linkml_meta": {"alias": "circularize", "domain_of": ["UploadedFileSource"]}},
    )
    coordinates: Optional[SimpleSequenceLocation] = Field(
        default=None,
        description="""If provided, coordinates within the sequence of the file to extract a subsequence""",
        json_schema_extra={"linkml_meta": {"alias": "coordinates", "domain_of": ["UploadedFileSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["UploadedFileSource"] = Field(
        default="UploadedFileSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class RepositoryIdSource(Source):
    """
    Represents the source of a sequence that is identified by a repository id
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    repository_id: str = Field(
        default=...,
        description="""The id of the sequence in the repository""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["RepositoryIdSource"] = Field(
        default="RepositoryIdSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class AddgeneIdSource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by an Addgene id
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    sequence_file_url: Optional[str] = Field(
        default=None,
        description="""The URL of a sequence file""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "sequence_file_url",
                "domain_of": ["AddgeneIdSource", "WekWikGeneIdSource", "SEVASource", "IGEMSource"],
            }
        },
    )
    addgene_sequence_type: Optional[AddgeneSequenceType] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "addgene_sequence_type", "domain_of": ["AddgeneIdSource"]}},
    )
    repository_id: str = Field(
        default=...,
        description="""The id of the sequence in the repository""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["AddgeneIdSource"] = Field(
        default="AddgeneIdSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("sequence_file_url")
    def pattern_sequence_file_url(cls, v):
        pattern = re.compile(
            r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
        )
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sequence_file_url format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sequence_file_url format: {v}"
            raise ValueError(err_msg)
        return v


class WekWikGeneIdSource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by a WekWikGene id
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {
                "repository_id": {
                    "description": "The id of the gene in the " "WekWik gene database",
                    "name": "repository_id",
                    "pattern": "^\\d+$",
                }
            },
        }
    )

    sequence_file_url: Optional[str] = Field(
        default=None,
        description="""The URL of a sequence file""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "sequence_file_url",
                "domain_of": ["AddgeneIdSource", "WekWikGeneIdSource", "SEVASource", "IGEMSource"],
            }
        },
    )
    repository_id: str = Field(
        default=...,
        description="""The id of the gene in the WekWik gene database""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["WekWikGeneIdSource"] = Field(
        default="WekWikGeneIdSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("sequence_file_url")
    def pattern_sequence_file_url(cls, v):
        pattern = re.compile(
            r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
        )
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sequence_file_url format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sequence_file_url format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("repository_id")
    def pattern_repository_id(cls, v):
        pattern = re.compile(r"^\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid repository_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid repository_id format: {v}"
            raise ValueError(err_msg)
        return v


class SEVASource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by a SEVA id
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {
                "repository_id": {
                    "description": "The SEVA plasmid name",
                    "name": "repository_id",
                    "pattern": "^pSEVA\\d+.*$",
                },
                "sequence_file_url": {
                    "description": "The URL of the sequence "
                    "file, which can refer to "
                    "a a gb file hosted on "
                    "the SEVA website or an "
                    "entry in the NCBI.",
                    "name": "sequence_file_url",
                    "required": True,
                },
            },
        }
    )

    sequence_file_url: str = Field(
        default=...,
        description="""The URL of the sequence file, which can refer to a a gb file hosted on the SEVA website or an entry in the NCBI.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "sequence_file_url",
                "domain_of": ["AddgeneIdSource", "WekWikGeneIdSource", "SEVASource", "IGEMSource"],
            }
        },
    )
    repository_id: str = Field(
        default=...,
        description="""The SEVA plasmid name""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["SEVASource"] = Field(
        default="SEVASource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("sequence_file_url")
    def pattern_sequence_file_url(cls, v):
        pattern = re.compile(
            r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
        )
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sequence_file_url format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sequence_file_url format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("repository_id")
    def pattern_repository_id(cls, v):
        pattern = re.compile(r"^pSEVA\d+.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid repository_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid repository_id format: {v}"
            raise ValueError(err_msg)
        return v


class BenchlingUrlSource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by a Benchling URL
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {
                "repository_id": {
                    "description": "The url of the gb file " "associated with the sequence",
                    "name": "repository_id",
                    "pattern": "^https:\\/\\/benchling\\.com\\/.+\\.gb$",
                }
            },
        }
    )

    repository_id: str = Field(
        default=...,
        description="""The url of the gb file associated with the sequence""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["BenchlingUrlSource"] = Field(
        default="BenchlingUrlSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("repository_id")
    def pattern_repository_id(cls, v):
        pattern = re.compile(r"^https:\/\/benchling\.com\/.+\.gb$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid repository_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid repository_id format: {v}"
            raise ValueError(err_msg)
        return v


class SnapGenePlasmidSource(RepositoryIdSource):
    """
    Represents the source of a sequence from the SnapGene plasmid library identified by a SnapGene subpath of https://www.snapgene.com/plasmids/
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {
                "repository_id": {
                    "description": "The subpath of the plasmid "
                    "in the SnapGene plasmid "
                    "library. Requesting the "
                    "plasmid is possible with "
                    "https://www.snapgene.com/local/fetch.php?set={category_path}&plasmid={plasmid['subpath']} "
                    "where category_path is the "
                    "left part of the subpath "
                    "before the first / and "
                    "plasmid is the subpath after "
                    "the /.",
                    "name": "repository_id",
                    "pattern": "^.+\\/.+$",
                }
            },
        }
    )

    repository_id: str = Field(
        default=...,
        description="""The subpath of the plasmid in the SnapGene plasmid library. Requesting the plasmid is possible with https://www.snapgene.com/local/fetch.php?set={category_path}&plasmid={plasmid['subpath']} where category_path is the left part of the subpath before the first / and plasmid is the subpath after the /.""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["SnapGenePlasmidSource"] = Field(
        default="SnapGenePlasmidSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("repository_id")
    def pattern_repository_id(cls, v):
        pattern = re.compile(r"^.+\/.+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid repository_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid repository_id format: {v}"
            raise ValueError(err_msg)
        return v


class EuroscarfSource(RepositoryIdSource):
    """
    Represents the source of a sequence from the Euroscarf plasmid library
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {
                "repository_id": {
                    "description": "The id of the plasmid in the " "Euroscarf plasmid library",
                    "name": "repository_id",
                    "pattern": "^P\\d+$",
                }
            },
        }
    )

    repository_id: str = Field(
        default=...,
        description="""The id of the plasmid in the Euroscarf plasmid library""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["EuroscarfSource"] = Field(
        default="EuroscarfSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("repository_id")
    def pattern_repository_id(cls, v):
        pattern = re.compile(r"^P\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid repository_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid repository_id format: {v}"
            raise ValueError(err_msg)
        return v


class IGEMSource(RepositoryIdSource):
    """
    Represents the source of a sequence from an iGEM collection
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {
                "repository_id": {
                    "description": "The unique identifier of the "
                    "sequence in the iGEM "
                    "collection (for now, "
                    "{part_id}-{plasmid_backbone})",
                    "name": "repository_id",
                },
                "sequence_file_url": {
                    "description": "The URL of the sequence " "file, for now github " "repository",
                    "name": "sequence_file_url",
                    "required": True,
                },
            },
        }
    )

    sequence_file_url: str = Field(
        default=...,
        description="""The URL of the sequence file, for now github repository""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "sequence_file_url",
                "domain_of": ["AddgeneIdSource", "WekWikGeneIdSource", "SEVASource", "IGEMSource"],
            }
        },
    )
    repository_id: str = Field(
        default=...,
        description="""The unique identifier of the sequence in the iGEM collection (for now, {part_id}-{plasmid_backbone})""",
        json_schema_extra={"linkml_meta": {"alias": "repository_id", "domain_of": ["RepositoryIdSource"]}},
    )
    repository_name: RepositoryName = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "repository_name", "domain_of": ["RepositoryIdSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["IGEMSource"] = Field(
        default="IGEMSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )

    @field_validator("sequence_file_url")
    def pattern_sequence_file_url(cls, v):
        pattern = re.compile(
            r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
        )
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sequence_file_url format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sequence_file_url format: {v}"
            raise ValueError(err_msg)
        return v


class GenomeCoordinatesSource(Source):
    """
    Represents the source of a sequence that is identified by genome coordinates, requested from NCBI
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    assembly_accession: Optional[str] = Field(
        default=None,
        description="""The accession of the assembly""",
        json_schema_extra={"linkml_meta": {"alias": "assembly_accession", "domain_of": ["GenomeCoordinatesSource"]}},
    )
    sequence_accession: str = Field(
        default=...,
        description="""The accession of the sequence""",
        json_schema_extra={"linkml_meta": {"alias": "sequence_accession", "domain_of": ["GenomeCoordinatesSource"]}},
    )
    locus_tag: Optional[str] = Field(
        default=None,
        description="""The locus tag of the sequence""",
        json_schema_extra={"linkml_meta": {"alias": "locus_tag", "domain_of": ["GenomeCoordinatesSource"]}},
    )
    gene_id: Optional[int] = Field(
        default=None,
        description="""The gene id of the sequence""",
        json_schema_extra={"linkml_meta": {"alias": "gene_id", "domain_of": ["GenomeCoordinatesSource"]}},
    )
    start: int = Field(
        default=...,
        description="""The starting coordinate (1-based) of the sequence in the sequence accession""",
        json_schema_extra={
            "linkml_meta": {"alias": "start", "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation"]}
        },
    )
    end: int = Field(
        default=...,
        description="""The ending coordinate (1-based) of the sequence in the sequence accession""",
        json_schema_extra={
            "linkml_meta": {"alias": "end", "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation"]}
        },
    )
    strand: int = Field(
        default=...,
        description="""The strand of the sequence in the sequence accession, should be 1 or -1""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strand",
                "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation", "PlannotateAnnotationReport"],
            }
        },
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["GenomeCoordinatesSource"] = Field(
        default="GenomeCoordinatesSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class SequenceCutSource(Source):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    left_edge: Optional[SequenceCut] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "left_edge",
                "domain_of": ["SequenceCutSource", "RestrictionEnzymeDigestionSource"],
            }
        },
    )
    right_edge: Optional[SequenceCut] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "right_edge",
                "domain_of": ["SequenceCutSource", "RestrictionEnzymeDigestionSource"],
            }
        },
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["SequenceCutSource"] = Field(
        default="SequenceCutSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class RestrictionEnzymeDigestionSource(SequenceCutSource):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting using restriction enzymes.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    left_edge: Optional[RestrictionSequenceCut] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "left_edge",
                "domain_of": ["SequenceCutSource", "RestrictionEnzymeDigestionSource"],
            }
        },
    )
    right_edge: Optional[RestrictionSequenceCut] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "right_edge",
                "domain_of": ["SequenceCutSource", "RestrictionEnzymeDigestionSource"],
            }
        },
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["RestrictionEnzymeDigestionSource"] = Field(
        default="RestrictionEnzymeDigestionSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class SimpleSequenceLocation(ConfiguredBaseModel):
    """
    Represents a location within a sequence, for now support for ranges only
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"class_uri": "bioschemas:SequenceRange", "from_schema": "https://opencloning.github.io/OpenCloning_LinkML"}
    )

    start: int = Field(
        default=...,
        description="""The starting coordinate (0-based) of the location""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "start",
                "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation"],
                "slot_uri": "bioschemas:rangeStart",
            }
        },
    )
    end: int = Field(
        default=...,
        description="""The ending coordinate (0-based) of the location""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "end",
                "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation"],
                "slot_uri": "bioschemas:rangeEnd",
            }
        },
    )
    strand: Optional[int] = Field(
        default=None,
        description="""The strand of the location, should be 1 or -1 or null""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strand",
                "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation", "PlannotateAnnotationReport"],
            }
        },
    )


class AssemblyFragment(ConfiguredBaseModel):
    """
    Represents a fragment in an assembly
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    sequence: int = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "sequence",
                "domain_of": ["Primer", "AssemblyFragment", "PlannotateAnnotationReport"],
            }
        },
    )
    left_location: Optional[SimpleSequenceLocation] = Field(
        default=None, json_schema_extra={"linkml_meta": {"alias": "left_location", "domain_of": ["AssemblyFragment"]}}
    )
    right_location: Optional[SimpleSequenceLocation] = Field(
        default=None, json_schema_extra={"linkml_meta": {"alias": "right_location", "domain_of": ["AssemblyFragment"]}}
    )
    reverse_complemented: bool = Field(
        default=...,
        description="""Whether the sequence is reverse complemented in the assembly""",
        json_schema_extra={"linkml_meta": {"alias": "reverse_complemented", "domain_of": ["AssemblyFragment"]}},
    )


class AssemblySource(Source):
    """
    Represents the source of a sequence that is an assembly of other sequences
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["AssemblySource"] = Field(
        default="AssemblySource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class PCRSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by PCR
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    add_primer_features: Optional[bool] = Field(
        default=False,
        description="""Whether to add primer features to the PCR product""",
        json_schema_extra={
            "linkml_meta": {"alias": "add_primer_features", "domain_of": ["PCRSource"], "ifabsent": "boolean(false)"}
        },
    )
    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["PCRSource"] = Field(
        default="PCRSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class LigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by ligation with sticky or blunt ends.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["LigationSource"] = Field(
        default="LigationSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class HomologousRecombinationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by homologous recombination
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["HomologousRecombinationSource"] = Field(
        default="HomologousRecombinationSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class GibsonAssemblySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Gibson assembly
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["GibsonAssemblySource"] = Field(
        default="GibsonAssemblySource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class InFusionSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by In-Fusion cloning by Takara Bio
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["InFusionSource"] = Field(
        default="InFusionSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class OverlapExtensionPCRLigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by ligation of PCR products as part of overlap extension PCR. Algorithmically equivalent to Gibson assembly.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["OverlapExtensionPCRLigationSource"] = Field(
        default="OverlapExtensionPCRLigationSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class InVivoAssemblySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by in vivo assembly. Algorithmically equivalent to Gibson assembly.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["InVivoAssemblySource"] = Field(
        default="InVivoAssemblySource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class RestrictionAndLigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by restriction and ligation
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://opencloning.github.io/OpenCloning_LinkML",
            "slot_usage": {"restriction_enzymes": {"name": "restriction_enzymes", "required": True}},
        }
    )

    restriction_enzymes: list[str] = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "restriction_enzymes",
                "domain_of": ["RestrictionAndLigationSource"],
                "exact_mappings": ["OBI:0000732"],
            }
        },
    )
    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["RestrictionAndLigationSource"] = Field(
        default="RestrictionAndLigationSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class GatewaySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Gateway cloning
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    reaction_type: GatewayReactionType = Field(
        default=..., json_schema_extra={"linkml_meta": {"alias": "reaction_type", "domain_of": ["GatewaySource"]}}
    )
    greedy: Optional[bool] = Field(
        default=False,
        description="""Whether to use a greedy consensus sequence for att sites (see https://github.com/manulera/GateWayMine)""",
        json_schema_extra={
            "linkml_meta": {"alias": "greedy", "domain_of": ["GatewaySource"], "ifabsent": "boolean(false)"}
        },
    )
    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["GatewaySource"] = Field(
        default="GatewaySource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class CreLoxRecombinationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Cre - Lox recombination
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["CreLoxRecombinationSource"] = Field(
        default="CreLoxRecombinationSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class CRISPRSource(HomologousRecombinationSource):
    """
    Represents the source of a sequence that is generated by CRISPR
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    guides: list[int] = Field(
        default=...,
        description="""The guide RNAs used in the CRISPR""",
        json_schema_extra={"linkml_meta": {"alias": "guides", "domain_of": ["CRISPRSource"]}},
    )
    circular: Optional[bool] = Field(
        default=None,
        description="""Whether the assembly is circular or not""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "circular",
                "domain_of": ["TemplateSequence", "ManuallyTypedSource", "AssemblySource"],
            }
        },
    )
    assembly: Optional[list[AssemblyFragment]] = Field(
        default=None,
        description="""A list of the fragments that are assembled, in order""",
        json_schema_extra={"linkml_meta": {"alias": "assembly", "domain_of": ["AssemblySource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["CRISPRSource"] = Field(
        default="CRISPRSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class OligoHybridizationSource(Source):
    """
    Represents the source of a sequence that is generated by oligo hybridization
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    overhang_crick_3prime: Optional[int] = Field(
        default=None,
        description="""Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "overhang_crick_3prime",
                "domain_of": ["TextFileSequence", "ManuallyTypedSource", "OligoHybridizationSource"],
            }
        },
    )
    forward_oligo: int = Field(
        default=...,
        description="""The forward oligo used in the hybridization""",
        json_schema_extra={"linkml_meta": {"alias": "forward_oligo", "domain_of": ["OligoHybridizationSource"]}},
    )
    reverse_oligo: int = Field(
        default=...,
        description="""The reverse oligo used in the hybridization""",
        json_schema_extra={"linkml_meta": {"alias": "reverse_oligo", "domain_of": ["OligoHybridizationSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["OligoHybridizationSource"] = Field(
        default="OligoHybridizationSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class PolymeraseExtensionSource(Source):
    """
    Represents the source of a sequence that is generated by polymerase extension
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["PolymeraseExtensionSource"] = Field(
        default="PolymeraseExtensionSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class CloningStrategy(ConfiguredBaseModel):
    """
    Represents a cloning strategy
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    sequences: list[Union[Sequence, TemplateSequence, TextFileSequence, Primer]] = Field(
        default=...,
        description="""The sequences that are used in the cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "sequences", "domain_of": ["CloningStrategy"]}},
    )
    sources: list[
        Union[
            Source,
            DatabaseSource,
            CollectionSource,
            ManuallyTypedSource,
            UploadedFileSource,
            RepositoryIdSource,
            GenomeCoordinatesSource,
            SequenceCutSource,
            AssemblySource,
            OligoHybridizationSource,
            PolymeraseExtensionSource,
            AnnotationSource,
            ReverseComplementSource,
            PCRSource,
            LigationSource,
            HomologousRecombinationSource,
            GibsonAssemblySource,
            InFusionSource,
            OverlapExtensionPCRLigationSource,
            InVivoAssemblySource,
            RestrictionAndLigationSource,
            GatewaySource,
            CreLoxRecombinationSource,
            CRISPRSource,
            RestrictionEnzymeDigestionSource,
            AddgeneIdSource,
            WekWikGeneIdSource,
            SEVASource,
            BenchlingUrlSource,
            SnapGenePlasmidSource,
            EuroscarfSource,
            IGEMSource,
        ]
    ] = Field(
        default=...,
        description="""The sources of the sequences that are used in the cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "sources", "domain_of": ["CloningStrategy"]}},
    )
    primers: Optional[list[Primer]] = Field(
        default=None,
        description="""The primers that are used in the cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "primers", "domain_of": ["CloningStrategy"]}},
    )
    description: Optional[str] = Field(
        default=None,
        description="""A description of the cloning strategy""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["CollectionSource", "CollectionOptionInfo", "CloningStrategy"],
            }
        },
    )
    files: Optional[list[Union[AssociatedFile, SequencingFile]]] = Field(
        default=None,
        description="""Files associated with this cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "files", "domain_of": ["CloningStrategy"]}},
    )
    schema_version: Optional[str] = Field(
        default=None,
        description="""The version of the schema that was used to generate this cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "schema_version", "domain_of": ["CloningStrategy"]}},
    )
    backend_version: Optional[str] = Field(
        default=None,
        description="""The version of the backend that was used to generate this cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "backend_version", "domain_of": ["CloningStrategy"]}},
    )
    frontend_version: Optional[str] = Field(
        default=None,
        description="""The version of the frontend that was used to generate this cloning strategy""",
        json_schema_extra={"linkml_meta": {"alias": "frontend_version", "domain_of": ["CloningStrategy"]}},
    )


class AnnotationReport(ConfiguredBaseModel):
    """
    Represents a report of an annotation step
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    type: Literal["AnnotationReport"] = Field(
        default="AnnotationReport",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )


class PlannotateAnnotationReport(AnnotationReport):
    """
    Represents a report of an annotation step using Plannotate
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    sseqid: Optional[str] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "sseqid", "domain_of": ["PlannotateAnnotationReport"]}},
    )
    start_location: Optional[int] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "start_location", "domain_of": ["PlannotateAnnotationReport"]}},
    )
    end_location: Optional[int] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "end_location", "domain_of": ["PlannotateAnnotationReport"]}},
    )
    strand: Optional[int] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "strand",
                "domain_of": ["GenomeCoordinatesSource", "SimpleSequenceLocation", "PlannotateAnnotationReport"],
            }
        },
    )
    percent_identity: Optional[float] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "percent_identity", "domain_of": ["PlannotateAnnotationReport"]}},
    )
    full_length_of_feature_in_db: Optional[int] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "full_length_of_feature_in_db", "domain_of": ["PlannotateAnnotationReport"]}
        },
    )
    length_of_found_feature: Optional[int] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "length_of_found_feature", "domain_of": ["PlannotateAnnotationReport"]}
        },
    )
    percent_match_length: Optional[float] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "percent_match_length", "domain_of": ["PlannotateAnnotationReport"]}
        },
    )
    fragment: Optional[bool] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "fragment", "domain_of": ["PlannotateAnnotationReport"]}},
    )
    database: Optional[str] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "database", "domain_of": ["PlannotateAnnotationReport"]}},
    )
    Feature: Optional[str] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "Feature", "domain_of": ["PlannotateAnnotationReport"]}},
    )
    Type: Optional[str] = Field(
        default=None, json_schema_extra={"linkml_meta": {"alias": "Type", "domain_of": ["PlannotateAnnotationReport"]}}
    )
    Description: Optional[str] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "Description", "domain_of": ["PlannotateAnnotationReport"]}},
    )
    sequence: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "sequence",
                "domain_of": ["Primer", "AssemblyFragment", "PlannotateAnnotationReport"],
            }
        },
    )
    type: Literal["PlannotateAnnotationReport"] = Field(
        default="PlannotateAnnotationReport",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )


class AnnotationSource(Source):
    """
    Represents a computational step in which sequence features are annotated in a sequence
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    annotation_tool: AnnotationTool = Field(
        default=..., json_schema_extra={"linkml_meta": {"alias": "annotation_tool", "domain_of": ["AnnotationSource"]}}
    )
    annotation_tool_version: Optional[str] = Field(
        default=None,
        description="""The version of the annotation tool""",
        json_schema_extra={"linkml_meta": {"alias": "annotation_tool_version", "domain_of": ["AnnotationSource"]}},
    )
    annotation_report: Optional[list[Union[AnnotationReport, PlannotateAnnotationReport]]] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "annotation_report", "domain_of": ["AnnotationSource"]}},
    )
    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["AnnotationSource"] = Field(
        default="AnnotationSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class ReverseComplementSource(Source):
    """
    Represents the in-silico transformation of a sequence into its reverse complement
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    input: Optional[list[int]] = Field(
        default=None,
        description="""The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.""",
        json_schema_extra={"linkml_meta": {"alias": "input", "domain_of": ["Source"], "slot_uri": "schema:object"}},
    )
    output: Optional[int] = Field(
        default=None,
        description="""Identifier of the sequence that is the output of this source.""",
        json_schema_extra={"linkml_meta": {"alias": "output", "domain_of": ["Source"], "slot_uri": "schema:result"}},
    )
    type: Literal["ReverseComplementSource"] = Field(
        default="ReverseComplementSource",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    output_name: Optional[str] = Field(
        default=None,
        description="""Used to specify the name of the output sequence""",
        json_schema_extra={"linkml_meta": {"alias": "output_name", "domain_of": ["Source"]}},
    )
    database_id: Optional[int] = Field(
        default=None,
        description="""The id of an entity in a database""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "database_id",
                "domain_of": ["Primer", "Source", "DatabaseSource"],
                "slot_uri": "schema:identifier",
            }
        },
    )
    id: int = Field(
        default=...,
        description="""A unique identifier for a thing""",
        json_schema_extra={
            "linkml_meta": {"alias": "id", "domain_of": ["NamedThing", "Sequence"], "slot_uri": "schema:identifier"}
        },
    )


class AssociatedFile(ConfiguredBaseModel):
    """
    Represents a file associated with a sequence
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    type: Literal["AssociatedFile"] = Field(
        default="AssociatedFile",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    sequence_id: int = Field(
        default=...,
        description="""The sequence this file is associated with""",
        json_schema_extra={"linkml_meta": {"alias": "sequence_id", "domain_of": ["AssociatedFile"]}},
    )
    file_name: str = Field(
        default=...,
        description="""The name of the file""",
        json_schema_extra={
            "linkml_meta": {"alias": "file_name", "domain_of": ["UploadedFileSource", "AssociatedFile"]}
        },
    )
    file_type: AssociatedFileType = Field(
        default=...,
        description="""The type of file""",
        json_schema_extra={"linkml_meta": {"alias": "file_type", "domain_of": ["AssociatedFile"]}},
    )


class SequencingFile(AssociatedFile):
    """
    Represents a sequencing file and its alignment to a sequence
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://opencloning.github.io/OpenCloning_LinkML"})

    alignment: list[str] = Field(
        default=...,
        description="""The alignment of the sequencing read to the sequence. List of strings representing aligned sequences.""",
        json_schema_extra={"linkml_meta": {"alias": "alignment", "domain_of": ["SequencingFile"]}},
    )
    type: Literal["SequencingFile"] = Field(
        default="SequencingFile",
        description="""Designates the class""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["Sequence", "Source", "CollectionOptionInfo", "AnnotationReport", "AssociatedFile"],
            }
        },
    )
    sequence_id: int = Field(
        default=...,
        description="""The sequence this file is associated with""",
        json_schema_extra={"linkml_meta": {"alias": "sequence_id", "domain_of": ["AssociatedFile"]}},
    )
    file_name: str = Field(
        default=...,
        description="""The name of the file""",
        json_schema_extra={
            "linkml_meta": {"alias": "file_name", "domain_of": ["UploadedFileSource", "AssociatedFile"]}
        },
    )
    file_type: AssociatedFileType = Field(
        default=...,
        description="""The type of file""",
        json_schema_extra={"linkml_meta": {"alias": "file_type", "domain_of": ["AssociatedFile"]}},
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
Sequence.model_rebuild()
TemplateSequence.model_rebuild()
TextFileSequence.model_rebuild()
Primer.model_rebuild()
SequenceCut.model_rebuild()
RestrictionSequenceCut.model_rebuild()
Source.model_rebuild()
DatabaseSource.model_rebuild()
CollectionSource.model_rebuild()
CollectionOption.model_rebuild()
CollectionOptionInfo.model_rebuild()
ManuallyTypedSource.model_rebuild()
UploadedFileSource.model_rebuild()
RepositoryIdSource.model_rebuild()
AddgeneIdSource.model_rebuild()
WekWikGeneIdSource.model_rebuild()
SEVASource.model_rebuild()
BenchlingUrlSource.model_rebuild()
SnapGenePlasmidSource.model_rebuild()
EuroscarfSource.model_rebuild()
IGEMSource.model_rebuild()
GenomeCoordinatesSource.model_rebuild()
SequenceCutSource.model_rebuild()
RestrictionEnzymeDigestionSource.model_rebuild()
SimpleSequenceLocation.model_rebuild()
AssemblyFragment.model_rebuild()
AssemblySource.model_rebuild()
PCRSource.model_rebuild()
LigationSource.model_rebuild()
HomologousRecombinationSource.model_rebuild()
GibsonAssemblySource.model_rebuild()
InFusionSource.model_rebuild()
OverlapExtensionPCRLigationSource.model_rebuild()
InVivoAssemblySource.model_rebuild()
RestrictionAndLigationSource.model_rebuild()
GatewaySource.model_rebuild()
CreLoxRecombinationSource.model_rebuild()
CRISPRSource.model_rebuild()
OligoHybridizationSource.model_rebuild()
PolymeraseExtensionSource.model_rebuild()
CloningStrategy.model_rebuild()
AnnotationReport.model_rebuild()
PlannotateAnnotationReport.model_rebuild()
AnnotationSource.model_rebuild()
ReverseComplementSource.model_rebuild()
AssociatedFile.model_rebuild()
SequencingFile.model_rebuild()
