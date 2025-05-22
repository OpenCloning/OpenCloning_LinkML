# Auto generated from opencloning_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-05-22T17:08:22
# Schema: OpenCloning_LinkML
#
# id: https://opencloning.github.io/OpenCloning_LinkML
# description: A LinkML data model for OpenCloning
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import date, datetime, time
from typing import Any, ClassVar, Dict, List, Optional, Union

from jsonasobj2 import JsonObj, as_dict
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import camelcase, sfx, underscore
from linkml_runtime.utils.metamodelcore import bnode, empty_dict, empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_float, extended_int, extended_str
from rdflib import Namespace, URIRef

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Namespaces
GENO = CurieNamespace("GENO", "http://purl.obolibrary.org/obo/GENO_")
IAO = CurieNamespace("IAO", "http://purl.obolibrary.org/obo/IAO_")
NCIT = CurieNamespace("NCIT", "http://purl.obolibrary.org/obo/NCIT_")
OBI = CurieNamespace("OBI", "http://purl.obolibrary.org/obo/OBI_")
PATO = CurieNamespace("PATO", "http://purl.obolibrary.org/obo/PATO_")
BIOLINK = CurieNamespace("biolink", "https://w3id.org/biolink/")
BIOSCHEMAS = CurieNamespace("bioschemas", "https://bioschemas.org/")
EXAMPLE = CurieNamespace("example", "https://example.org/")
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
OPENCLONING_LINKML = CurieNamespace("opencloning_linkml", "https://opencloning.github.io/OpenCloning_LinkML/")
SCHEMA = CurieNamespace("schema", "http://schema.org/")
XSD = CurieNamespace("xsd", "http://www.w3.org/2001/XMLSchema#")
DEFAULT_ = OPENCLONING_LINKML


# Types
class VersionNumber(String):
    """A version number"""

    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "version_number"
    type_model_uri = OPENCLONING_LINKML.VersionNumber


class SequenceRange(String):
    """A sequence range defined using genbank syntax (e.g. 1..100), note that 1..100 in genbank is equivalent to 0:100 in python"""

    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sequence_range"
    type_model_uri = OPENCLONING_LINKML.SequenceRange


# Class references
class NamedThingId(extended_int):
    pass


class SequenceId(NamedThingId):
    pass


class TemplateSequenceId(SequenceId):
    pass


class TextFileSequenceId(SequenceId):
    pass


class PrimerId(SequenceId):
    pass


class SourceId(NamedThingId):
    pass


class DatabaseSourceId(SourceId):
    pass


class CollectionSourceId(SourceId):
    pass


class ManuallyTypedSourceId(SourceId):
    pass


class UploadedFileSourceId(SourceId):
    pass


class RepositoryIdSourceId(SourceId):
    pass


class AddgeneIdSourceId(RepositoryIdSourceId):
    pass


class WekWikGeneIdSourceId(RepositoryIdSourceId):
    pass


class SEVASourceId(RepositoryIdSourceId):
    pass


class BenchlingUrlSourceId(RepositoryIdSourceId):
    pass


class SnapGenePlasmidSourceId(RepositoryIdSourceId):
    pass


class EuroscarfSourceId(RepositoryIdSourceId):
    pass


class IGEMSourceId(RepositoryIdSourceId):
    pass


class GenomeCoordinatesSourceId(SourceId):
    pass


class SequenceCutSourceId(SourceId):
    pass


class RestrictionEnzymeDigestionSourceId(SequenceCutSourceId):
    pass


class AssemblySourceId(SourceId):
    pass


class PCRSourceId(AssemblySourceId):
    pass


class LigationSourceId(AssemblySourceId):
    pass


class HomologousRecombinationSourceId(AssemblySourceId):
    pass


class GibsonAssemblySourceId(AssemblySourceId):
    pass


class InFusionSourceId(AssemblySourceId):
    pass


class OverlapExtensionPCRLigationSourceId(AssemblySourceId):
    pass


class InVivoAssemblySourceId(AssemblySourceId):
    pass


class RestrictionAndLigationSourceId(AssemblySourceId):
    pass


class GatewaySourceId(AssemblySourceId):
    pass


class CreLoxRecombinationSourceId(AssemblySourceId):
    pass


class CRISPRSourceId(HomologousRecombinationSourceId):
    pass


class OligoHybridizationSourceId(SourceId):
    pass


class PolymeraseExtensionSourceId(SourceId):
    pass


class AnnotationSourceId(SourceId):
    pass


class ReverseComplementSourceId(SourceId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.NamedThing

    id: Union[int, NamedThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sequence(NamedThing):
    """
    Represents a sequence
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSCHEMAS["DNA"]
    class_class_curie: ClassVar[str] = "bioschemas:DNA"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.Sequence

    id: Union[int, SequenceId] = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceId):
            self.id = SequenceId(self.id)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)

    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class TemplateSequence(Sequence):
    """
    Represents a sequence that is part of a template, where the actual sequence content will be determined by the
    user's actions
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["TemplateSequence"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:TemplateSequence"
    class_name: ClassVar[str] = "TemplateSequence"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.TemplateSequence

    id: Union[int, TemplateSequenceId] = None
    circular: Optional[Union[bool, Bool]] = None
    primer_design: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TemplateSequenceId):
            self.id = TemplateSequenceId(self.id)

        if self.circular is not None and not isinstance(self.circular, Bool):
            self.circular = Bool(self.circular)

        if self.primer_design is not None and not isinstance(self.primer_design, str):
            self.primer_design = str(self.primer_design)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class TextFileSequence(Sequence):
    """
    A sequence (may have features) defined by the content of a text file
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["TextFileSequence"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:TextFileSequence"
    class_name: ClassVar[str] = "TextFileSequence"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.TextFileSequence

    id: Union[int, TextFileSequenceId] = None
    sequence_file_format: Union[str, "SequenceFileFormat"] = None
    overhang_crick_3prime: Optional[int] = 0
    overhang_watson_3prime: Optional[int] = 0
    file_content: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TextFileSequenceId):
            self.id = TextFileSequenceId(self.id)

        if self._is_empty(self.sequence_file_format):
            self.MissingRequiredField("sequence_file_format")
        if not isinstance(self.sequence_file_format, SequenceFileFormat):
            self.sequence_file_format = SequenceFileFormat(self.sequence_file_format)

        if self.overhang_crick_3prime is not None and not isinstance(self.overhang_crick_3prime, int):
            self.overhang_crick_3prime = int(self.overhang_crick_3prime)

        if self.overhang_watson_3prime is not None and not isinstance(self.overhang_watson_3prime, int):
            self.overhang_watson_3prime = int(self.overhang_watson_3prime)

        if self.file_content is not None and not isinstance(self.file_content, str):
            self.file_content = str(self.file_content)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Primer(Sequence):
    """
    An oligonucleotide or primer
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["Primer"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:Primer"
    class_name: ClassVar[str] = "Primer"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.Primer

    id: Union[int, PrimerId] = None
    name: Optional[str] = None
    database_id: Optional[int] = None
    sequence: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrimerId):
            self.id = PrimerId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.database_id is not None and not isinstance(self.database_id, int):
            self.database_id = int(self.database_id)

        if self.sequence is not None and not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class SequenceCut(YAMLRoot):
    """
    Represents a cut in a DNA sequence
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["SequenceCut"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:SequenceCut"
    class_name: ClassVar[str] = "SequenceCut"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.SequenceCut

    cut_watson: int = None
    overhang: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cut_watson):
            self.MissingRequiredField("cut_watson")
        if not isinstance(self.cut_watson, int):
            self.cut_watson = int(self.cut_watson)

        if self._is_empty(self.overhang):
            self.MissingRequiredField("overhang")
        if not isinstance(self.overhang, int):
            self.overhang = int(self.overhang)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RestrictionSequenceCut(SequenceCut):
    """
    Represents a cut in a DNA sequence that is made by a restriction enzyme
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["RestrictionSequenceCut"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:RestrictionSequenceCut"
    class_name: ClassVar[str] = "RestrictionSequenceCut"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.RestrictionSequenceCut

    cut_watson: int = None
    overhang: int = None
    restriction_enzyme: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.restriction_enzyme):
            self.MissingRequiredField("restriction_enzyme")
        if not isinstance(self.restriction_enzyme, str):
            self.restriction_enzyme = str(self.restriction_enzyme)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Source(NamedThing):
    """
    Represents the source of a sequence
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["CreateAction"]
    class_class_curie: ClassVar[str] = "schema:CreateAction"
    class_name: ClassVar[str] = "Source"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.Source

    id: Union[int, SourceId] = None
    input: Optional[Union[Union[int, SequenceId], list[Union[int, SequenceId]]]] = empty_list()
    output: Optional[Union[int, SequenceId]] = None
    type: Optional[str] = None
    output_name: Optional[str] = None
    database_id: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.input, list):
            self.input = [self.input] if self.input is not None else []
        self.input = [v if isinstance(v, SequenceId) else SequenceId(v) for v in self.input]

        if self.output is not None and not isinstance(self.output, SequenceId):
            self.output = SequenceId(self.output)

        self.type = str(self.class_name)

        if self.output_name is not None and not isinstance(self.output_name, str):
            self.output_name = str(self.output_name)

        if self.database_id is not None and not isinstance(self.database_id, int):
            self.database_id = int(self.database_id)

        super().__post_init__(**kwargs)

    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class DatabaseSource(Source):
    """
    Represents the source of a sequence that is identified by a database id
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["DatabaseSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:DatabaseSource"
    class_name: ClassVar[str] = "DatabaseSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.DatabaseSource

    id: Union[int, DatabaseSourceId] = None
    database_id: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatabaseSourceId):
            self.id = DatabaseSourceId(self.id)

        if self._is_empty(self.database_id):
            self.MissingRequiredField("database_id")
        if not isinstance(self.database_id, int):
            self.database_id = int(self.database_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class CollectionSource(Source):
    """
    Represents a collection of possible sources in a template
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["CollectionSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:CollectionSource"
    class_name: ClassVar[str] = "CollectionSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.CollectionSource

    id: Union[int, CollectionSourceId] = None
    title: str = None
    category_id: Optional[str] = None
    description: Optional[str] = None
    image: Optional[Union[str, list[str]]] = empty_list()
    options: Optional[Union[Union[dict, "CollectionOption"], list[Union[dict, "CollectionOption"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CollectionSourceId):
            self.id = CollectionSourceId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.category_id is not None and not isinstance(self.category_id, str):
            self.category_id = str(self.category_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.image, list):
            self.image = [self.image] if self.image is not None else []
        self.image = [v if isinstance(v, str) else str(v) for v in self.image]

        if not isinstance(self.options, list):
            self.options = [self.options] if self.options is not None else []
        self.options = [v if isinstance(v, CollectionOption) else CollectionOption(**as_dict(v)) for v in self.options]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class CollectionOption(YAMLRoot):
    """
    Represents an option in a collection
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["CollectionOption"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:CollectionOption"
    class_name: ClassVar[str] = "CollectionOption"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.CollectionOption

    name: str = None
    source: Union[dict, Source] = None
    info: Optional[Union[dict, "CollectionOptionInfo"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, Source):
            self.source = Source(**as_dict(self.source))

        if self.info is not None and not isinstance(self.info, CollectionOptionInfo):
            self.info = CollectionOptionInfo(**as_dict(self.info))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CollectionOptionInfo(YAMLRoot):
    """
    Additional information about a collection option
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["CollectionOptionInfo"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:CollectionOptionInfo"
    class_name: ClassVar[str] = "CollectionOptionInfo"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.CollectionOptionInfo

    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Union[str, "CollectionOptionType"]] = None
    resistance: Optional[str] = None
    well: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, CollectionOptionType):
            self.type = CollectionOptionType(self.type)

        if self.resistance is not None and not isinstance(self.resistance, str):
            self.resistance = str(self.resistance)

        if self.well is not None and not isinstance(self.well, str):
            self.well = str(self.well)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ManuallyTypedSource(Source):
    """
    Represents the source of a sequence that is manually typed by the user
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["ManuallyTypedSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:ManuallyTypedSource"
    class_name: ClassVar[str] = "ManuallyTypedSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.ManuallyTypedSource

    id: Union[int, ManuallyTypedSourceId] = None
    user_input: str = None
    overhang_crick_3prime: Optional[int] = 0
    overhang_watson_3prime: Optional[int] = 0
    circular: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManuallyTypedSourceId):
            self.id = ManuallyTypedSourceId(self.id)

        if self._is_empty(self.user_input):
            self.MissingRequiredField("user_input")
        if not isinstance(self.user_input, str):
            self.user_input = str(self.user_input)

        if self.overhang_crick_3prime is not None and not isinstance(self.overhang_crick_3prime, int):
            self.overhang_crick_3prime = int(self.overhang_crick_3prime)

        if self.overhang_watson_3prime is not None and not isinstance(self.overhang_watson_3prime, int):
            self.overhang_watson_3prime = int(self.overhang_watson_3prime)

        if self.circular is not None and not isinstance(self.circular, Bool):
            self.circular = Bool(self.circular)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class UploadedFileSource(Source):
    """
    Represents the source of a sequence that is uploaded as a file
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["UploadedFileSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:UploadedFileSource"
    class_name: ClassVar[str] = "UploadedFileSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.UploadedFileSource

    id: Union[int, UploadedFileSourceId] = None
    sequence_file_format: Union[str, "SequenceFileFormat"] = None
    file_name: Optional[str] = None
    index_in_file: Optional[int] = None
    circularize: Optional[Union[bool, Bool]] = None
    coordinates: Optional[Union[str, SequenceRange]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UploadedFileSourceId):
            self.id = UploadedFileSourceId(self.id)

        if self._is_empty(self.sequence_file_format):
            self.MissingRequiredField("sequence_file_format")
        if not isinstance(self.sequence_file_format, SequenceFileFormat):
            self.sequence_file_format = SequenceFileFormat(self.sequence_file_format)

        if self.file_name is not None and not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.index_in_file is not None and not isinstance(self.index_in_file, int):
            self.index_in_file = int(self.index_in_file)

        if self.circularize is not None and not isinstance(self.circularize, Bool):
            self.circularize = Bool(self.circularize)

        if self.coordinates is not None and not isinstance(self.coordinates, SequenceRange):
            self.coordinates = SequenceRange(self.coordinates)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class RepositoryIdSource(Source):
    """
    Represents the source of a sequence that is identified by a repository id
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["RepositoryIdSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:RepositoryIdSource"
    class_name: ClassVar[str] = "RepositoryIdSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.RepositoryIdSource

    id: Union[int, RepositoryIdSourceId] = None
    repository_id: str = None
    repository_name: Union[str, "RepositoryName"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepositoryIdSourceId):
            self.id = RepositoryIdSourceId(self.id)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        if self._is_empty(self.repository_name):
            self.MissingRequiredField("repository_name")
        if not isinstance(self.repository_name, RepositoryName):
            self.repository_name = RepositoryName(self.repository_name)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class AddgeneIdSource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by an Addgene id
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["AddgeneIdSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:AddgeneIdSource"
    class_name: ClassVar[str] = "AddgeneIdSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.AddgeneIdSource

    id: Union[int, AddgeneIdSourceId] = None
    repository_id: str = None
    repository_name: Union[str, "RepositoryName"] = None
    sequence_file_url: Optional[str] = None
    addgene_sequence_type: Optional[Union[str, "AddgeneSequenceType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AddgeneIdSourceId):
            self.id = AddgeneIdSourceId(self.id)

        if self.sequence_file_url is not None and not isinstance(self.sequence_file_url, str):
            self.sequence_file_url = str(self.sequence_file_url)

        if self.addgene_sequence_type is not None and not isinstance(self.addgene_sequence_type, AddgeneSequenceType):
            self.addgene_sequence_type = AddgeneSequenceType(self.addgene_sequence_type)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class WekWikGeneIdSource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by a WekWikGene id
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["WekWikGeneIdSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:WekWikGeneIdSource"
    class_name: ClassVar[str] = "WekWikGeneIdSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.WekWikGeneIdSource

    id: Union[int, WekWikGeneIdSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    repository_id: str = None
    sequence_file_url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WekWikGeneIdSourceId):
            self.id = WekWikGeneIdSourceId(self.id)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        if self.sequence_file_url is not None and not isinstance(self.sequence_file_url, str):
            self.sequence_file_url = str(self.sequence_file_url)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class SEVASource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by a SEVA id
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["SEVASource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:SEVASource"
    class_name: ClassVar[str] = "SEVASource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.SEVASource

    id: Union[int, SEVASourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    sequence_file_url: str = None
    repository_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SEVASourceId):
            self.id = SEVASourceId(self.id)

        if self._is_empty(self.sequence_file_url):
            self.MissingRequiredField("sequence_file_url")
        if not isinstance(self.sequence_file_url, str):
            self.sequence_file_url = str(self.sequence_file_url)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class BenchlingUrlSource(RepositoryIdSource):
    """
    Represents the source of a sequence that is identified by a Benchling URL
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["BenchlingUrlSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:BenchlingUrlSource"
    class_name: ClassVar[str] = "BenchlingUrlSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.BenchlingUrlSource

    id: Union[int, BenchlingUrlSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    repository_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenchlingUrlSourceId):
            self.id = BenchlingUrlSourceId(self.id)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class SnapGenePlasmidSource(RepositoryIdSource):
    """
    Represents the source of a sequence from the SnapGene plasmid library identified by a SnapGene subpath of
    https://www.snapgene.com/plasmids/
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["SnapGenePlasmidSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:SnapGenePlasmidSource"
    class_name: ClassVar[str] = "SnapGenePlasmidSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.SnapGenePlasmidSource

    id: Union[int, SnapGenePlasmidSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    repository_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SnapGenePlasmidSourceId):
            self.id = SnapGenePlasmidSourceId(self.id)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class EuroscarfSource(RepositoryIdSource):
    """
    Represents the source of a sequence from the Euroscarf plasmid library
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["EuroscarfSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:EuroscarfSource"
    class_name: ClassVar[str] = "EuroscarfSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.EuroscarfSource

    id: Union[int, EuroscarfSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    repository_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EuroscarfSourceId):
            self.id = EuroscarfSourceId(self.id)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class IGEMSource(RepositoryIdSource):
    """
    Represents the source of a sequence from an iGEM collection
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["IGEMSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:IGEMSource"
    class_name: ClassVar[str] = "IGEMSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.IGEMSource

    id: Union[int, IGEMSourceId] = None
    repository_name: Union[str, "RepositoryName"] = None
    sequence_file_url: str = None
    repository_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IGEMSourceId):
            self.id = IGEMSourceId(self.id)

        if self._is_empty(self.sequence_file_url):
            self.MissingRequiredField("sequence_file_url")
        if not isinstance(self.sequence_file_url, str):
            self.sequence_file_url = str(self.sequence_file_url)

        if self._is_empty(self.repository_id):
            self.MissingRequiredField("repository_id")
        if not isinstance(self.repository_id, str):
            self.repository_id = str(self.repository_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class GenomeCoordinatesSource(Source):
    """
    Represents the source of a sequence that is identified by genome coordinates, requested from NCBI
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["GenomeCoordinatesSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:GenomeCoordinatesSource"
    class_name: ClassVar[str] = "GenomeCoordinatesSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.GenomeCoordinatesSource

    id: Union[int, GenomeCoordinatesSourceId] = None
    sequence_accession: str = None
    start: int = None
    end: int = None
    strand: int = None
    assembly_accession: Optional[str] = None
    locus_tag: Optional[str] = None
    gene_id: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenomeCoordinatesSourceId):
            self.id = GenomeCoordinatesSourceId(self.id)

        if self._is_empty(self.sequence_accession):
            self.MissingRequiredField("sequence_accession")
        if not isinstance(self.sequence_accession, str):
            self.sequence_accession = str(self.sequence_accession)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        if self._is_empty(self.strand):
            self.MissingRequiredField("strand")
        if not isinstance(self.strand, int):
            self.strand = int(self.strand)

        if self.assembly_accession is not None and not isinstance(self.assembly_accession, str):
            self.assembly_accession = str(self.assembly_accession)

        if self.locus_tag is not None and not isinstance(self.locus_tag, str):
            self.locus_tag = str(self.locus_tag)

        if self.gene_id is not None and not isinstance(self.gene_id, int):
            self.gene_id = int(self.gene_id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class SequenceCutSource(Source):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["SequenceCutSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:SequenceCutSource"
    class_name: ClassVar[str] = "SequenceCutSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.SequenceCutSource

    id: Union[int, SequenceCutSourceId] = None
    left_edge: Optional[Union[dict, SequenceCut]] = None
    right_edge: Optional[Union[dict, SequenceCut]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceCutSourceId):
            self.id = SequenceCutSourceId(self.id)

        if self.left_edge is not None and not isinstance(self.left_edge, SequenceCut):
            self.left_edge = SequenceCut(**as_dict(self.left_edge))

        if self.right_edge is not None and not isinstance(self.right_edge, SequenceCut):
            self.right_edge = SequenceCut(**as_dict(self.right_edge))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class RestrictionEnzymeDigestionSource(SequenceCutSource):
    """
    Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting using
    restriction enzymes.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["RestrictionEnzymeDigestionSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:RestrictionEnzymeDigestionSource"
    class_name: ClassVar[str] = "RestrictionEnzymeDigestionSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.RestrictionEnzymeDigestionSource

    id: Union[int, RestrictionEnzymeDigestionSourceId] = None
    left_edge: Optional[Union[dict, RestrictionSequenceCut]] = None
    right_edge: Optional[Union[dict, RestrictionSequenceCut]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RestrictionEnzymeDigestionSourceId):
            self.id = RestrictionEnzymeDigestionSourceId(self.id)

        if self.left_edge is not None and not isinstance(self.left_edge, RestrictionSequenceCut):
            self.left_edge = RestrictionSequenceCut(**as_dict(self.left_edge))

        if self.right_edge is not None and not isinstance(self.right_edge, RestrictionSequenceCut):
            self.right_edge = RestrictionSequenceCut(**as_dict(self.right_edge))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class AssemblyFragment(YAMLRoot):
    """
    Represents a fragment in an assembly
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["AssemblyFragment"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:AssemblyFragment"
    class_name: ClassVar[str] = "AssemblyFragment"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.AssemblyFragment

    sequence: Union[int, SequenceId] = None
    reverse_complemented: Union[bool, Bool] = None
    left_location: Optional[Union[str, SequenceRange]] = None
    right_location: Optional[Union[str, SequenceRange]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, SequenceId):
            self.sequence = SequenceId(self.sequence)

        if self._is_empty(self.reverse_complemented):
            self.MissingRequiredField("reverse_complemented")
        if not isinstance(self.reverse_complemented, Bool):
            self.reverse_complemented = Bool(self.reverse_complemented)

        if self.left_location is not None and not isinstance(self.left_location, SequenceRange):
            self.left_location = SequenceRange(self.left_location)

        if self.right_location is not None and not isinstance(self.right_location, SequenceRange):
            self.right_location = SequenceRange(self.right_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssemblySource(Source):
    """
    Represents the source of a sequence that is an assembly of other sequences
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["AssemblySource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:AssemblySource"
    class_name: ClassVar[str] = "AssemblySource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.AssemblySource

    id: Union[int, AssemblySourceId] = None
    circular: Optional[Union[bool, Bool]] = None
    assembly: Optional[Union[Union[dict, AssemblyFragment], list[Union[dict, AssemblyFragment]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssemblySourceId):
            self.id = AssemblySourceId(self.id)

        if self.circular is not None and not isinstance(self.circular, Bool):
            self.circular = Bool(self.circular)

        if not isinstance(self.assembly, list):
            self.assembly = [self.assembly] if self.assembly is not None else []
        self.assembly = [
            v if isinstance(v, AssemblyFragment) else AssemblyFragment(**as_dict(v)) for v in self.assembly
        ]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class PCRSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by PCR
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["PCRSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:PCRSource"
    class_name: ClassVar[str] = "PCRSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.PCRSource

    id: Union[int, PCRSourceId] = None
    add_primer_features: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PCRSourceId):
            self.id = PCRSourceId(self.id)

        if self.add_primer_features is not None and not isinstance(self.add_primer_features, Bool):
            self.add_primer_features = Bool(self.add_primer_features)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class LigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by ligation with sticky or blunt ends.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["LigationSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:LigationSource"
    class_name: ClassVar[str] = "LigationSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.LigationSource

    id: Union[int, LigationSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LigationSourceId):
            self.id = LigationSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HomologousRecombinationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by homologous recombination
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["HomologousRecombinationSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:HomologousRecombinationSource"
    class_name: ClassVar[str] = "HomologousRecombinationSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.HomologousRecombinationSource

    id: Union[int, HomologousRecombinationSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HomologousRecombinationSourceId):
            self.id = HomologousRecombinationSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class GibsonAssemblySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Gibson assembly
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["GibsonAssemblySource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:GibsonAssemblySource"
    class_name: ClassVar[str] = "GibsonAssemblySource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.GibsonAssemblySource

    id: Union[int, GibsonAssemblySourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GibsonAssemblySourceId):
            self.id = GibsonAssemblySourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class InFusionSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by In-Fusion cloning by Takara Bio
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["InFusionSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:InFusionSource"
    class_name: ClassVar[str] = "InFusionSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.InFusionSource

    id: Union[int, InFusionSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InFusionSourceId):
            self.id = InFusionSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class OverlapExtensionPCRLigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by ligation of PCR products as part of overlap extension
    PCR. Algorithmically equivalent to Gibson assembly.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["OverlapExtensionPCRLigationSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:OverlapExtensionPCRLigationSource"
    class_name: ClassVar[str] = "OverlapExtensionPCRLigationSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.OverlapExtensionPCRLigationSource

    id: Union[int, OverlapExtensionPCRLigationSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OverlapExtensionPCRLigationSourceId):
            self.id = OverlapExtensionPCRLigationSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class InVivoAssemblySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by in vivo assembly. Algorithmically equivalent to Gibson
    assembly.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["InVivoAssemblySource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:InVivoAssemblySource"
    class_name: ClassVar[str] = "InVivoAssemblySource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.InVivoAssemblySource

    id: Union[int, InVivoAssemblySourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InVivoAssemblySourceId):
            self.id = InVivoAssemblySourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class RestrictionAndLigationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by restriction and ligation
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["RestrictionAndLigationSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:RestrictionAndLigationSource"
    class_name: ClassVar[str] = "RestrictionAndLigationSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.RestrictionAndLigationSource

    id: Union[int, RestrictionAndLigationSourceId] = None
    restriction_enzymes: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RestrictionAndLigationSourceId):
            self.id = RestrictionAndLigationSourceId(self.id)

        if self._is_empty(self.restriction_enzymes):
            self.MissingRequiredField("restriction_enzymes")
        if not isinstance(self.restriction_enzymes, list):
            self.restriction_enzymes = [self.restriction_enzymes] if self.restriction_enzymes is not None else []
        self.restriction_enzymes = [v if isinstance(v, str) else str(v) for v in self.restriction_enzymes]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class GatewaySource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Gateway cloning
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["GatewaySource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:GatewaySource"
    class_name: ClassVar[str] = "GatewaySource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.GatewaySource

    id: Union[int, GatewaySourceId] = None
    reaction_type: Union[str, "GatewayReactionType"] = None
    greedy: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GatewaySourceId):
            self.id = GatewaySourceId(self.id)

        if self._is_empty(self.reaction_type):
            self.MissingRequiredField("reaction_type")
        if not isinstance(self.reaction_type, GatewayReactionType):
            self.reaction_type = GatewayReactionType(self.reaction_type)

        if self.greedy is not None and not isinstance(self.greedy, Bool):
            self.greedy = Bool(self.greedy)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class CreLoxRecombinationSource(AssemblySource):
    """
    Represents the source of a sequence that is generated by Cre - Lox recombination
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["CreLoxRecombinationSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:CreLoxRecombinationSource"
    class_name: ClassVar[str] = "CreLoxRecombinationSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.CreLoxRecombinationSource

    id: Union[int, CreLoxRecombinationSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CreLoxRecombinationSourceId):
            self.id = CreLoxRecombinationSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class CRISPRSource(HomologousRecombinationSource):
    """
    Represents the source of a sequence that is generated by CRISPR
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["CRISPRSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:CRISPRSource"
    class_name: ClassVar[str] = "CRISPRSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.CRISPRSource

    id: Union[int, CRISPRSourceId] = None
    guides: Union[Union[int, PrimerId], list[Union[int, PrimerId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CRISPRSourceId):
            self.id = CRISPRSourceId(self.id)

        if self._is_empty(self.guides):
            self.MissingRequiredField("guides")
        if not isinstance(self.guides, list):
            self.guides = [self.guides] if self.guides is not None else []
        self.guides = [v if isinstance(v, PrimerId) else PrimerId(v) for v in self.guides]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class OligoHybridizationSource(Source):
    """
    Represents the source of a sequence that is generated by oligo hybridization
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["OligoHybridizationSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:OligoHybridizationSource"
    class_name: ClassVar[str] = "OligoHybridizationSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.OligoHybridizationSource

    id: Union[int, OligoHybridizationSourceId] = None
    forward_oligo: Union[int, PrimerId] = None
    reverse_oligo: Union[int, PrimerId] = None
    overhang_crick_3prime: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OligoHybridizationSourceId):
            self.id = OligoHybridizationSourceId(self.id)

        if self._is_empty(self.forward_oligo):
            self.MissingRequiredField("forward_oligo")
        if not isinstance(self.forward_oligo, PrimerId):
            self.forward_oligo = PrimerId(self.forward_oligo)

        if self._is_empty(self.reverse_oligo):
            self.MissingRequiredField("reverse_oligo")
        if not isinstance(self.reverse_oligo, PrimerId):
            self.reverse_oligo = PrimerId(self.reverse_oligo)

        if self.overhang_crick_3prime is not None and not isinstance(self.overhang_crick_3prime, int):
            self.overhang_crick_3prime = int(self.overhang_crick_3prime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class PolymeraseExtensionSource(Source):
    """
    Represents the source of a sequence that is generated by polymerase extension
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["PolymeraseExtensionSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:PolymeraseExtensionSource"
    class_name: ClassVar[str] = "PolymeraseExtensionSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.PolymeraseExtensionSource

    id: Union[int, PolymeraseExtensionSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolymeraseExtensionSourceId):
            self.id = PolymeraseExtensionSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class CloningStrategy(YAMLRoot):
    """
    Represents a cloning strategy
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["CloningStrategy"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:CloningStrategy"
    class_name: ClassVar[str] = "CloningStrategy"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.CloningStrategy

    sequences: Union[dict[Union[int, SequenceId], Union[dict, Sequence]], list[Union[dict, Sequence]]] = empty_dict()
    sources: Union[dict[Union[int, SourceId], Union[dict, Source]], list[Union[dict, Source]]] = empty_dict()
    primers: Optional[Union[dict[Union[int, PrimerId], Union[dict, Primer]], list[Union[dict, Primer]]]] = empty_dict()
    description: Optional[str] = None
    files: Optional[Union[Union[dict, "AssociatedFile"], list[Union[dict, "AssociatedFile"]]]] = empty_list()
    schema_version: Optional[Union[str, VersionNumber]] = None
    backend_version: Optional[Union[str, VersionNumber]] = None
    frontend_version: Optional[Union[str, VersionNumber]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sequences):
            self.MissingRequiredField("sequences")
        self._normalize_inlined_as_list(slot_name="sequences", slot_type=Sequence, key_name="id", keyed=True)

        if self._is_empty(self.sources):
            self.MissingRequiredField("sources")
        self._normalize_inlined_as_list(slot_name="sources", slot_type=Source, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="primers", slot_type=Primer, key_name="id", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.files, list):
            self.files = [self.files] if self.files is not None else []
        self.files = [v if isinstance(v, AssociatedFile) else AssociatedFile(**as_dict(v)) for v in self.files]

        if self.schema_version is not None and not isinstance(self.schema_version, VersionNumber):
            self.schema_version = VersionNumber(self.schema_version)

        if self.backend_version is not None and not isinstance(self.backend_version, VersionNumber):
            self.backend_version = VersionNumber(self.backend_version)

        if self.frontend_version is not None and not isinstance(self.frontend_version, VersionNumber):
            self.frontend_version = VersionNumber(self.frontend_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnnotationReport(YAMLRoot):
    """
    Represents a report of an annotation step
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["AnnotationReport"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:AnnotationReport"
    class_name: ClassVar[str] = "AnnotationReport"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.AnnotationReport

    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self.type = str(self.class_name)

        super().__post_init__(**kwargs)

    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class PlannotateAnnotationReport(AnnotationReport):
    """
    Represents a report of an annotation step using Plannotate
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["PlannotateAnnotationReport"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:PlannotateAnnotationReport"
    class_name: ClassVar[str] = "PlannotateAnnotationReport"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.PlannotateAnnotationReport

    sseqid: Optional[str] = None
    start_location: Optional[int] = None
    end_location: Optional[int] = None
    strand: Optional[int] = None
    percent_identity: Optional[float] = None
    full_length_of_feature_in_db: Optional[int] = None
    length_of_found_feature: Optional[int] = None
    percent_match_length: Optional[float] = None
    fragment: Optional[Union[bool, Bool]] = None
    database: Optional[str] = None
    Feature: Optional[str] = None
    Type: Optional[str] = None
    Description: Optional[str] = None
    sequence: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sseqid is not None and not isinstance(self.sseqid, str):
            self.sseqid = str(self.sseqid)

        if self.start_location is not None and not isinstance(self.start_location, int):
            self.start_location = int(self.start_location)

        if self.end_location is not None and not isinstance(self.end_location, int):
            self.end_location = int(self.end_location)

        if self.strand is not None and not isinstance(self.strand, int):
            self.strand = int(self.strand)

        if self.percent_identity is not None and not isinstance(self.percent_identity, float):
            self.percent_identity = float(self.percent_identity)

        if self.full_length_of_feature_in_db is not None and not isinstance(self.full_length_of_feature_in_db, int):
            self.full_length_of_feature_in_db = int(self.full_length_of_feature_in_db)

        if self.length_of_found_feature is not None and not isinstance(self.length_of_found_feature, int):
            self.length_of_found_feature = int(self.length_of_found_feature)

        if self.percent_match_length is not None and not isinstance(self.percent_match_length, float):
            self.percent_match_length = float(self.percent_match_length)

        if self.fragment is not None and not isinstance(self.fragment, Bool):
            self.fragment = Bool(self.fragment)

        if self.database is not None and not isinstance(self.database, str):
            self.database = str(self.database)

        if self.Feature is not None and not isinstance(self.Feature, str):
            self.Feature = str(self.Feature)

        if self.Type is not None and not isinstance(self.Type, str):
            self.Type = str(self.Type)

        if self.Description is not None and not isinstance(self.Description, str):
            self.Description = str(self.Description)

        if self.sequence is not None and not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class AnnotationSource(Source):
    """
    Represents a computational step in which sequence features are annotated in a sequence
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["AnnotationSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:AnnotationSource"
    class_name: ClassVar[str] = "AnnotationSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.AnnotationSource

    id: Union[int, AnnotationSourceId] = None
    annotation_tool: Union[str, "AnnotationTool"] = None
    annotation_tool_version: Optional[str] = None
    annotation_report: Optional[Union[Union[dict, AnnotationReport], list[Union[dict, AnnotationReport]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnnotationSourceId):
            self.id = AnnotationSourceId(self.id)

        if self._is_empty(self.annotation_tool):
            self.MissingRequiredField("annotation_tool")
        if not isinstance(self.annotation_tool, AnnotationTool):
            self.annotation_tool = AnnotationTool(self.annotation_tool)

        if self.annotation_tool_version is not None and not isinstance(self.annotation_tool_version, str):
            self.annotation_tool_version = str(self.annotation_tool_version)

        if not isinstance(self.annotation_report, list):
            self.annotation_report = [self.annotation_report] if self.annotation_report is not None else []
        self.annotation_report = [
            v if isinstance(v, AnnotationReport) else AnnotationReport(**as_dict(v)) for v in self.annotation_report
        ]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class ReverseComplementSource(Source):
    """
    Represents the in-silico transformation of a sequence into its reverse complement
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["ReverseComplementSource"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:ReverseComplementSource"
    class_name: ClassVar[str] = "ReverseComplementSource"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.ReverseComplementSource

    id: Union[int, ReverseComplementSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReverseComplementSourceId):
            self.id = ReverseComplementSourceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class AssociatedFile(YAMLRoot):
    """
    Represents a file associated with a sequence
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["AssociatedFile"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:AssociatedFile"
    class_name: ClassVar[str] = "AssociatedFile"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.AssociatedFile

    sequence_id: Union[int, SequenceId] = None
    file_name: str = None
    file_type: Union[str, "AssociatedFileType"] = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sequence_id):
            self.MissingRequiredField("sequence_id")
        if not isinstance(self.sequence_id, SequenceId):
            self.sequence_id = SequenceId(self.sequence_id)

        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.file_type):
            self.MissingRequiredField("file_type")
        if not isinstance(self.file_type, AssociatedFileType):
            self.file_type = AssociatedFileType(self.file_type)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)

    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class SequencingFile(AssociatedFile):
    """
    Represents a sequencing file and its alignment to a sequence
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCLONING_LINKML["SequencingFile"]
    class_class_curie: ClassVar[str] = "opencloning_linkml:SequencingFile"
    class_name: ClassVar[str] = "SequencingFile"
    class_model_uri: ClassVar[URIRef] = OPENCLONING_LINKML.SequencingFile

    sequence_id: Union[int, SequenceId] = None
    file_name: str = None
    file_type: Union[str, "AssociatedFileType"] = None
    alignment: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.alignment):
            self.MissingRequiredField("alignment")
        if not isinstance(self.alignment, list):
            self.alignment = [self.alignment] if self.alignment is not None else []
        self.alignment = [v if isinstance(v, str) else str(v) for v in self.alignment]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


# Enumerations
class RepositoryName(EnumDefinitionImpl):

    addgene = PermissibleValue(text="addgene", description="Addgene")
    genbank = PermissibleValue(text="genbank", description="GenBank")
    benchling = PermissibleValue(text="benchling", description="Benchling")
    snapgene = PermissibleValue(text="snapgene", description="SnapGene plasmid library")
    euroscarf = PermissibleValue(text="euroscarf", description="Euroscarf (plasmids only)")
    igem = PermissibleValue(text="igem", description="iGEM collection")
    wekwikgene = PermissibleValue(text="wekwikgene", description="WekWikGene")
    seva = PermissibleValue(text="seva", description="SEVA (Standard European Vector Architecture)")

    _defn = EnumDefinition(
        name="RepositoryName",
    )


class Collection(EnumDefinitionImpl):

    AddgenePlasmid = PermissibleValue(text="AddgenePlasmid", description="A plasmid from Addgene")
    OligoPair = PermissibleValue(text="OligoPair", description="A pair of oligonucleotides for hybridization")

    _defn = EnumDefinition(
        name="Collection",
    )


class SequenceFileFormat(EnumDefinitionImpl):

    fasta = PermissibleValue(text="fasta")
    genbank = PermissibleValue(text="genbank")
    snapgene = PermissibleValue(text="snapgene")
    embl = PermissibleValue(text="embl")

    _defn = EnumDefinition(
        name="SequenceFileFormat",
    )


class AddgeneSequenceType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AddgeneSequenceType",
    )

    @classmethod
    def _addvals(cls):
        setattr(
            cls,
            "depositor-full",
            PermissibleValue(
                text="depositor-full", description="Full sequence of the plasmid submitted by the depositor"
            ),
        )
        setattr(
            cls,
            "addgene-full",
            PermissibleValue(text="addgene-full", description="Full sequence of the plasmid performed by Addgene"),
        )


class GatewayReactionType(EnumDefinitionImpl):

    LR = PermissibleValue(text="LR", description="LR reaction")
    BP = PermissibleValue(text="BP", description="BP reaction")

    _defn = EnumDefinition(
        name="GatewayReactionType",
    )


class AnnotationTool(EnumDefinitionImpl):

    plannotate = PermissibleValue(text="plannotate")

    _defn = EnumDefinition(
        name="AnnotationTool",
    )


class AssociatedFileType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AssociatedFileType",
    )

    @classmethod
    def _addvals(cls):
        setattr(
            cls,
            "Sequencing file",
            PermissibleValue(
                text="Sequencing file", description="A file containing sequencing data", meaning=NCIT["C171177"]
            ),
        )


class CollectionOptionType(EnumDefinitionImpl):

    OligoPair = PermissibleValue(text="OligoPair", description="A pair of oligonucleotides for hybridization")
    AddgenePlasmid = PermissibleValue(text="AddgenePlasmid", description="A plasmid from Addgene")

    _defn = EnumDefinition(
        name="CollectionOptionType",
    )


# Slots
class slots:
    pass


slots.id = Slot(
    uri=SCHEMA.identifier,
    name="id",
    curie=SCHEMA.curie("identifier"),
    model_uri=OPENCLONING_LINKML.id,
    domain=None,
    range=URIRef,
)

slots.database_id = Slot(
    uri=SCHEMA.identifier,
    name="database_id",
    curie=SCHEMA.curie("identifier"),
    model_uri=OPENCLONING_LINKML.database_id,
    domain=None,
    range=Optional[int],
)

slots.name = Slot(
    uri=SCHEMA.name,
    name="name",
    curie=SCHEMA.curie("name"),
    model_uri=OPENCLONING_LINKML.name,
    domain=None,
    range=Optional[str],
)

slots.restriction_enzyme = Slot(
    uri=OPENCLONING_LINKML.restriction_enzyme,
    name="restriction_enzyme",
    curie=OPENCLONING_LINKML.curie("restriction_enzyme"),
    model_uri=OPENCLONING_LINKML.restriction_enzyme,
    domain=None,
    range=Optional[str],
)

slots.restriction_enzymes = Slot(
    uri=OPENCLONING_LINKML.restriction_enzymes,
    name="restriction_enzymes",
    curie=OPENCLONING_LINKML.curie("restriction_enzymes"),
    model_uri=OPENCLONING_LINKML.restriction_enzymes,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.input = Slot(
    uri=SCHEMA.object,
    name="input",
    curie=SCHEMA.curie("object"),
    model_uri=OPENCLONING_LINKML.input,
    domain=None,
    range=Optional[Union[Union[int, SequenceId], list[Union[int, SequenceId]]]],
)

slots.output = Slot(
    uri=SCHEMA.result,
    name="output",
    curie=SCHEMA.curie("result"),
    model_uri=OPENCLONING_LINKML.output,
    domain=None,
    range=Optional[Union[int, SequenceId]],
)

slots.output_name = Slot(
    uri=OPENCLONING_LINKML.output_name,
    name="output_name",
    curie=OPENCLONING_LINKML.curie("output_name"),
    model_uri=OPENCLONING_LINKML.output_name,
    domain=None,
    range=Optional[str],
)

slots.type = Slot(
    uri=OPENCLONING_LINKML.type,
    name="type",
    curie=OPENCLONING_LINKML.curie("type"),
    model_uri=OPENCLONING_LINKML.type,
    domain=None,
    range=Optional[str],
)

slots.sequence_file_format = Slot(
    uri=OPENCLONING_LINKML.sequence_file_format,
    name="sequence_file_format",
    curie=OPENCLONING_LINKML.curie("sequence_file_format"),
    model_uri=OPENCLONING_LINKML.sequence_file_format,
    domain=None,
    range=Optional[Union[str, "SequenceFileFormat"]],
)

slots.overhang_crick_3prime = Slot(
    uri=OPENCLONING_LINKML.overhang_crick_3prime,
    name="overhang_crick_3prime",
    curie=OPENCLONING_LINKML.curie("overhang_crick_3prime"),
    model_uri=OPENCLONING_LINKML.overhang_crick_3prime,
    domain=None,
    range=Optional[int],
)

slots.overhang_watson_3prime = Slot(
    uri=OPENCLONING_LINKML.overhang_watson_3prime,
    name="overhang_watson_3prime",
    curie=OPENCLONING_LINKML.curie("overhang_watson_3prime"),
    model_uri=OPENCLONING_LINKML.overhang_watson_3prime,
    domain=None,
    range=Optional[int],
)

slots.sequence_file_url = Slot(
    uri=OPENCLONING_LINKML.sequence_file_url,
    name="sequence_file_url",
    curie=OPENCLONING_LINKML.curie("sequence_file_url"),
    model_uri=OPENCLONING_LINKML.sequence_file_url,
    domain=None,
    range=Optional[str],
    pattern=re.compile(
        r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
    ),
)

slots.repository_id = Slot(
    uri=OPENCLONING_LINKML.repository_id,
    name="repository_id",
    curie=OPENCLONING_LINKML.curie("repository_id"),
    model_uri=OPENCLONING_LINKML.repository_id,
    domain=None,
    range=str,
)

slots.templateSequence__circular = Slot(
    uri=OPENCLONING_LINKML.circular,
    name="templateSequence__circular",
    curie=OPENCLONING_LINKML.curie("circular"),
    model_uri=OPENCLONING_LINKML.templateSequence__circular,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.templateSequence__primer_design = Slot(
    uri=OPENCLONING_LINKML.primer_design,
    name="templateSequence__primer_design",
    curie=OPENCLONING_LINKML.curie("primer_design"),
    model_uri=OPENCLONING_LINKML.templateSequence__primer_design,
    domain=None,
    range=Optional[str],
)

slots.textFileSequence__file_content = Slot(
    uri=OPENCLONING_LINKML.file_content,
    name="textFileSequence__file_content",
    curie=OPENCLONING_LINKML.curie("file_content"),
    model_uri=OPENCLONING_LINKML.textFileSequence__file_content,
    domain=None,
    range=Optional[str],
)

slots.primer__sequence = Slot(
    uri=OPENCLONING_LINKML.sequence,
    name="primer__sequence",
    curie=OPENCLONING_LINKML.curie("sequence"),
    model_uri=OPENCLONING_LINKML.primer__sequence,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^[acgtACGT]+$"),
)

slots.sequenceCut__cut_watson = Slot(
    uri=OPENCLONING_LINKML.cut_watson,
    name="sequenceCut__cut_watson",
    curie=OPENCLONING_LINKML.curie("cut_watson"),
    model_uri=OPENCLONING_LINKML.sequenceCut__cut_watson,
    domain=None,
    range=int,
)

slots.sequenceCut__overhang = Slot(
    uri=OPENCLONING_LINKML.overhang,
    name="sequenceCut__overhang",
    curie=OPENCLONING_LINKML.curie("overhang"),
    model_uri=OPENCLONING_LINKML.sequenceCut__overhang,
    domain=None,
    range=int,
)

slots.collectionSource__category_id = Slot(
    uri=OPENCLONING_LINKML.category_id,
    name="collectionSource__category_id",
    curie=OPENCLONING_LINKML.curie("category_id"),
    model_uri=OPENCLONING_LINKML.collectionSource__category_id,
    domain=None,
    range=Optional[str],
)

slots.collectionSource__title = Slot(
    uri=OPENCLONING_LINKML.title,
    name="collectionSource__title",
    curie=OPENCLONING_LINKML.curie("title"),
    model_uri=OPENCLONING_LINKML.collectionSource__title,
    domain=None,
    range=str,
)

slots.collectionSource__description = Slot(
    uri=OPENCLONING_LINKML.description,
    name="collectionSource__description",
    curie=OPENCLONING_LINKML.curie("description"),
    model_uri=OPENCLONING_LINKML.collectionSource__description,
    domain=None,
    range=Optional[str],
)

slots.collectionSource__image = Slot(
    uri=OPENCLONING_LINKML.image,
    name="collectionSource__image",
    curie=OPENCLONING_LINKML.curie("image"),
    model_uri=OPENCLONING_LINKML.collectionSource__image,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.collectionSource__options = Slot(
    uri=OPENCLONING_LINKML.options,
    name="collectionSource__options",
    curie=OPENCLONING_LINKML.curie("options"),
    model_uri=OPENCLONING_LINKML.collectionSource__options,
    domain=None,
    range=Optional[Union[Union[dict, CollectionOption], list[Union[dict, CollectionOption]]]],
)

slots.collectionOption__source = Slot(
    uri=OPENCLONING_LINKML.source,
    name="collectionOption__source",
    curie=OPENCLONING_LINKML.curie("source"),
    model_uri=OPENCLONING_LINKML.collectionOption__source,
    domain=None,
    range=Union[dict, Source],
)

slots.collectionOption__info = Slot(
    uri=OPENCLONING_LINKML.info,
    name="collectionOption__info",
    curie=OPENCLONING_LINKML.curie("info"),
    model_uri=OPENCLONING_LINKML.collectionOption__info,
    domain=None,
    range=Optional[Union[dict, CollectionOptionInfo]],
)

slots.collectionOptionInfo__description = Slot(
    uri=OPENCLONING_LINKML.description,
    name="collectionOptionInfo__description",
    curie=OPENCLONING_LINKML.curie("description"),
    model_uri=OPENCLONING_LINKML.collectionOptionInfo__description,
    domain=None,
    range=Optional[str],
)

slots.collectionOptionInfo__type = Slot(
    uri=OPENCLONING_LINKML.type,
    name="collectionOptionInfo__type",
    curie=OPENCLONING_LINKML.curie("type"),
    model_uri=OPENCLONING_LINKML.collectionOptionInfo__type,
    domain=None,
    range=Optional[Union[str, "CollectionOptionType"]],
)

slots.collectionOptionInfo__resistance = Slot(
    uri=OPENCLONING_LINKML.resistance,
    name="collectionOptionInfo__resistance",
    curie=OPENCLONING_LINKML.curie("resistance"),
    model_uri=OPENCLONING_LINKML.collectionOptionInfo__resistance,
    domain=None,
    range=Optional[str],
)

slots.collectionOptionInfo__well = Slot(
    uri=OPENCLONING_LINKML.well,
    name="collectionOptionInfo__well",
    curie=OPENCLONING_LINKML.curie("well"),
    model_uri=OPENCLONING_LINKML.collectionOptionInfo__well,
    domain=None,
    range=Optional[str],
)

slots.manuallyTypedSource__user_input = Slot(
    uri=OPENCLONING_LINKML.user_input,
    name="manuallyTypedSource__user_input",
    curie=OPENCLONING_LINKML.curie("user_input"),
    model_uri=OPENCLONING_LINKML.manuallyTypedSource__user_input,
    domain=None,
    range=str,
    pattern=re.compile(r"^[acgtACGT]+$"),
)

slots.manuallyTypedSource__circular = Slot(
    uri=OPENCLONING_LINKML.circular,
    name="manuallyTypedSource__circular",
    curie=OPENCLONING_LINKML.curie("circular"),
    model_uri=OPENCLONING_LINKML.manuallyTypedSource__circular,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.uploadedFileSource__file_name = Slot(
    uri=OPENCLONING_LINKML.file_name,
    name="uploadedFileSource__file_name",
    curie=OPENCLONING_LINKML.curie("file_name"),
    model_uri=OPENCLONING_LINKML.uploadedFileSource__file_name,
    domain=None,
    range=Optional[str],
)

slots.uploadedFileSource__index_in_file = Slot(
    uri=OPENCLONING_LINKML.index_in_file,
    name="uploadedFileSource__index_in_file",
    curie=OPENCLONING_LINKML.curie("index_in_file"),
    model_uri=OPENCLONING_LINKML.uploadedFileSource__index_in_file,
    domain=None,
    range=Optional[int],
)

slots.uploadedFileSource__circularize = Slot(
    uri=OPENCLONING_LINKML.circularize,
    name="uploadedFileSource__circularize",
    curie=OPENCLONING_LINKML.curie("circularize"),
    model_uri=OPENCLONING_LINKML.uploadedFileSource__circularize,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.uploadedFileSource__coordinates = Slot(
    uri=OPENCLONING_LINKML.coordinates,
    name="uploadedFileSource__coordinates",
    curie=OPENCLONING_LINKML.curie("coordinates"),
    model_uri=OPENCLONING_LINKML.uploadedFileSource__coordinates,
    domain=None,
    range=Optional[Union[str, SequenceRange]],
)

slots.repositoryIdSource__repository_name = Slot(
    uri=OPENCLONING_LINKML.repository_name,
    name="repositoryIdSource__repository_name",
    curie=OPENCLONING_LINKML.curie("repository_name"),
    model_uri=OPENCLONING_LINKML.repositoryIdSource__repository_name,
    domain=None,
    range=Union[str, "RepositoryName"],
)

slots.addgeneIdSource__addgene_sequence_type = Slot(
    uri=OPENCLONING_LINKML.addgene_sequence_type,
    name="addgeneIdSource__addgene_sequence_type",
    curie=OPENCLONING_LINKML.curie("addgene_sequence_type"),
    model_uri=OPENCLONING_LINKML.addgeneIdSource__addgene_sequence_type,
    domain=None,
    range=Optional[Union[str, "AddgeneSequenceType"]],
)

slots.genomeCoordinatesSource__assembly_accession = Slot(
    uri=OPENCLONING_LINKML.assembly_accession,
    name="genomeCoordinatesSource__assembly_accession",
    curie=OPENCLONING_LINKML.curie("assembly_accession"),
    model_uri=OPENCLONING_LINKML.genomeCoordinatesSource__assembly_accession,
    domain=None,
    range=Optional[str],
)

slots.genomeCoordinatesSource__sequence_accession = Slot(
    uri=OPENCLONING_LINKML.sequence_accession,
    name="genomeCoordinatesSource__sequence_accession",
    curie=OPENCLONING_LINKML.curie("sequence_accession"),
    model_uri=OPENCLONING_LINKML.genomeCoordinatesSource__sequence_accession,
    domain=None,
    range=str,
)

slots.genomeCoordinatesSource__locus_tag = Slot(
    uri=OPENCLONING_LINKML.locus_tag,
    name="genomeCoordinatesSource__locus_tag",
    curie=OPENCLONING_LINKML.curie("locus_tag"),
    model_uri=OPENCLONING_LINKML.genomeCoordinatesSource__locus_tag,
    domain=None,
    range=Optional[str],
)

slots.genomeCoordinatesSource__gene_id = Slot(
    uri=OPENCLONING_LINKML.gene_id,
    name="genomeCoordinatesSource__gene_id",
    curie=OPENCLONING_LINKML.curie("gene_id"),
    model_uri=OPENCLONING_LINKML.genomeCoordinatesSource__gene_id,
    domain=None,
    range=Optional[int],
)

slots.genomeCoordinatesSource__start = Slot(
    uri=OPENCLONING_LINKML.start,
    name="genomeCoordinatesSource__start",
    curie=OPENCLONING_LINKML.curie("start"),
    model_uri=OPENCLONING_LINKML.genomeCoordinatesSource__start,
    domain=None,
    range=int,
)

slots.genomeCoordinatesSource__end = Slot(
    uri=OPENCLONING_LINKML.end,
    name="genomeCoordinatesSource__end",
    curie=OPENCLONING_LINKML.curie("end"),
    model_uri=OPENCLONING_LINKML.genomeCoordinatesSource__end,
    domain=None,
    range=int,
)

slots.genomeCoordinatesSource__strand = Slot(
    uri=OPENCLONING_LINKML.strand,
    name="genomeCoordinatesSource__strand",
    curie=OPENCLONING_LINKML.curie("strand"),
    model_uri=OPENCLONING_LINKML.genomeCoordinatesSource__strand,
    domain=None,
    range=int,
)

slots.sequenceCutSource__left_edge = Slot(
    uri=OPENCLONING_LINKML.left_edge,
    name="sequenceCutSource__left_edge",
    curie=OPENCLONING_LINKML.curie("left_edge"),
    model_uri=OPENCLONING_LINKML.sequenceCutSource__left_edge,
    domain=None,
    range=Optional[Union[dict, SequenceCut]],
)

slots.sequenceCutSource__right_edge = Slot(
    uri=OPENCLONING_LINKML.right_edge,
    name="sequenceCutSource__right_edge",
    curie=OPENCLONING_LINKML.curie("right_edge"),
    model_uri=OPENCLONING_LINKML.sequenceCutSource__right_edge,
    domain=None,
    range=Optional[Union[dict, SequenceCut]],
)

slots.restrictionEnzymeDigestionSource__left_edge = Slot(
    uri=OPENCLONING_LINKML.left_edge,
    name="restrictionEnzymeDigestionSource__left_edge",
    curie=OPENCLONING_LINKML.curie("left_edge"),
    model_uri=OPENCLONING_LINKML.restrictionEnzymeDigestionSource__left_edge,
    domain=None,
    range=Optional[Union[dict, RestrictionSequenceCut]],
)

slots.restrictionEnzymeDigestionSource__right_edge = Slot(
    uri=OPENCLONING_LINKML.right_edge,
    name="restrictionEnzymeDigestionSource__right_edge",
    curie=OPENCLONING_LINKML.curie("right_edge"),
    model_uri=OPENCLONING_LINKML.restrictionEnzymeDigestionSource__right_edge,
    domain=None,
    range=Optional[Union[dict, RestrictionSequenceCut]],
)

slots.assemblyFragment__sequence = Slot(
    uri=OPENCLONING_LINKML.sequence,
    name="assemblyFragment__sequence",
    curie=OPENCLONING_LINKML.curie("sequence"),
    model_uri=OPENCLONING_LINKML.assemblyFragment__sequence,
    domain=None,
    range=Union[int, SequenceId],
)

slots.assemblyFragment__left_location = Slot(
    uri=OPENCLONING_LINKML.left_location,
    name="assemblyFragment__left_location",
    curie=OPENCLONING_LINKML.curie("left_location"),
    model_uri=OPENCLONING_LINKML.assemblyFragment__left_location,
    domain=None,
    range=Optional[Union[str, SequenceRange]],
)

slots.assemblyFragment__right_location = Slot(
    uri=OPENCLONING_LINKML.right_location,
    name="assemblyFragment__right_location",
    curie=OPENCLONING_LINKML.curie("right_location"),
    model_uri=OPENCLONING_LINKML.assemblyFragment__right_location,
    domain=None,
    range=Optional[Union[str, SequenceRange]],
)

slots.assemblyFragment__reverse_complemented = Slot(
    uri=OPENCLONING_LINKML.reverse_complemented,
    name="assemblyFragment__reverse_complemented",
    curie=OPENCLONING_LINKML.curie("reverse_complemented"),
    model_uri=OPENCLONING_LINKML.assemblyFragment__reverse_complemented,
    domain=None,
    range=Union[bool, Bool],
)

slots.assemblySource__circular = Slot(
    uri=OPENCLONING_LINKML.circular,
    name="assemblySource__circular",
    curie=OPENCLONING_LINKML.curie("circular"),
    model_uri=OPENCLONING_LINKML.assemblySource__circular,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.assemblySource__assembly = Slot(
    uri=OPENCLONING_LINKML.assembly,
    name="assemblySource__assembly",
    curie=OPENCLONING_LINKML.curie("assembly"),
    model_uri=OPENCLONING_LINKML.assemblySource__assembly,
    domain=None,
    range=Optional[Union[Union[dict, AssemblyFragment], list[Union[dict, AssemblyFragment]]]],
)

slots.pCRSource__add_primer_features = Slot(
    uri=OPENCLONING_LINKML.add_primer_features,
    name="pCRSource__add_primer_features",
    curie=OPENCLONING_LINKML.curie("add_primer_features"),
    model_uri=OPENCLONING_LINKML.pCRSource__add_primer_features,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.gatewaySource__reaction_type = Slot(
    uri=OPENCLONING_LINKML.reaction_type,
    name="gatewaySource__reaction_type",
    curie=OPENCLONING_LINKML.curie("reaction_type"),
    model_uri=OPENCLONING_LINKML.gatewaySource__reaction_type,
    domain=None,
    range=Union[str, "GatewayReactionType"],
)

slots.gatewaySource__greedy = Slot(
    uri=OPENCLONING_LINKML.greedy,
    name="gatewaySource__greedy",
    curie=OPENCLONING_LINKML.curie("greedy"),
    model_uri=OPENCLONING_LINKML.gatewaySource__greedy,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.cRISPRSource__guides = Slot(
    uri=OPENCLONING_LINKML.guides,
    name="cRISPRSource__guides",
    curie=OPENCLONING_LINKML.curie("guides"),
    model_uri=OPENCLONING_LINKML.cRISPRSource__guides,
    domain=None,
    range=Union[Union[int, PrimerId], list[Union[int, PrimerId]]],
)

slots.oligoHybridizationSource__forward_oligo = Slot(
    uri=OPENCLONING_LINKML.forward_oligo,
    name="oligoHybridizationSource__forward_oligo",
    curie=OPENCLONING_LINKML.curie("forward_oligo"),
    model_uri=OPENCLONING_LINKML.oligoHybridizationSource__forward_oligo,
    domain=None,
    range=Union[int, PrimerId],
)

slots.oligoHybridizationSource__reverse_oligo = Slot(
    uri=OPENCLONING_LINKML.reverse_oligo,
    name="oligoHybridizationSource__reverse_oligo",
    curie=OPENCLONING_LINKML.curie("reverse_oligo"),
    model_uri=OPENCLONING_LINKML.oligoHybridizationSource__reverse_oligo,
    domain=None,
    range=Union[int, PrimerId],
)

slots.cloningStrategy__sequences = Slot(
    uri=OPENCLONING_LINKML.sequences,
    name="cloningStrategy__sequences",
    curie=OPENCLONING_LINKML.curie("sequences"),
    model_uri=OPENCLONING_LINKML.cloningStrategy__sequences,
    domain=None,
    range=Union[dict[Union[int, SequenceId], Union[dict, Sequence]], list[Union[dict, Sequence]]],
)

slots.cloningStrategy__sources = Slot(
    uri=OPENCLONING_LINKML.sources,
    name="cloningStrategy__sources",
    curie=OPENCLONING_LINKML.curie("sources"),
    model_uri=OPENCLONING_LINKML.cloningStrategy__sources,
    domain=None,
    range=Union[dict[Union[int, SourceId], Union[dict, Source]], list[Union[dict, Source]]],
)

slots.cloningStrategy__primers = Slot(
    uri=OPENCLONING_LINKML.primers,
    name="cloningStrategy__primers",
    curie=OPENCLONING_LINKML.curie("primers"),
    model_uri=OPENCLONING_LINKML.cloningStrategy__primers,
    domain=None,
    range=Optional[Union[dict[Union[int, PrimerId], Union[dict, Primer]], list[Union[dict, Primer]]]],
)

slots.cloningStrategy__description = Slot(
    uri=OPENCLONING_LINKML.description,
    name="cloningStrategy__description",
    curie=OPENCLONING_LINKML.curie("description"),
    model_uri=OPENCLONING_LINKML.cloningStrategy__description,
    domain=None,
    range=Optional[str],
)

slots.cloningStrategy__files = Slot(
    uri=OPENCLONING_LINKML.files,
    name="cloningStrategy__files",
    curie=OPENCLONING_LINKML.curie("files"),
    model_uri=OPENCLONING_LINKML.cloningStrategy__files,
    domain=None,
    range=Optional[Union[Union[dict, AssociatedFile], list[Union[dict, AssociatedFile]]]],
)

slots.cloningStrategy__schema_version = Slot(
    uri=OPENCLONING_LINKML.schema_version,
    name="cloningStrategy__schema_version",
    curie=OPENCLONING_LINKML.curie("schema_version"),
    model_uri=OPENCLONING_LINKML.cloningStrategy__schema_version,
    domain=None,
    range=Optional[Union[str, VersionNumber]],
)

slots.cloningStrategy__backend_version = Slot(
    uri=OPENCLONING_LINKML.backend_version,
    name="cloningStrategy__backend_version",
    curie=OPENCLONING_LINKML.curie("backend_version"),
    model_uri=OPENCLONING_LINKML.cloningStrategy__backend_version,
    domain=None,
    range=Optional[Union[str, VersionNumber]],
)

slots.cloningStrategy__frontend_version = Slot(
    uri=OPENCLONING_LINKML.frontend_version,
    name="cloningStrategy__frontend_version",
    curie=OPENCLONING_LINKML.curie("frontend_version"),
    model_uri=OPENCLONING_LINKML.cloningStrategy__frontend_version,
    domain=None,
    range=Optional[Union[str, VersionNumber]],
)

slots.plannotateAnnotationReport__sseqid = Slot(
    uri=OPENCLONING_LINKML.sseqid,
    name="plannotateAnnotationReport__sseqid",
    curie=OPENCLONING_LINKML.curie("sseqid"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__sseqid,
    domain=None,
    range=Optional[str],
)

slots.plannotateAnnotationReport__start_location = Slot(
    uri=OPENCLONING_LINKML.start_location,
    name="plannotateAnnotationReport__start_location",
    curie=OPENCLONING_LINKML.curie("start_location"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__start_location,
    domain=None,
    range=Optional[int],
)

slots.plannotateAnnotationReport__end_location = Slot(
    uri=OPENCLONING_LINKML.end_location,
    name="plannotateAnnotationReport__end_location",
    curie=OPENCLONING_LINKML.curie("end_location"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__end_location,
    domain=None,
    range=Optional[int],
)

slots.plannotateAnnotationReport__strand = Slot(
    uri=OPENCLONING_LINKML.strand,
    name="plannotateAnnotationReport__strand",
    curie=OPENCLONING_LINKML.curie("strand"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__strand,
    domain=None,
    range=Optional[int],
)

slots.plannotateAnnotationReport__percent_identity = Slot(
    uri=OPENCLONING_LINKML.percent_identity,
    name="plannotateAnnotationReport__percent_identity",
    curie=OPENCLONING_LINKML.curie("percent_identity"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__percent_identity,
    domain=None,
    range=Optional[float],
)

slots.plannotateAnnotationReport__full_length_of_feature_in_db = Slot(
    uri=OPENCLONING_LINKML.full_length_of_feature_in_db,
    name="plannotateAnnotationReport__full_length_of_feature_in_db",
    curie=OPENCLONING_LINKML.curie("full_length_of_feature_in_db"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__full_length_of_feature_in_db,
    domain=None,
    range=Optional[int],
)

slots.plannotateAnnotationReport__length_of_found_feature = Slot(
    uri=OPENCLONING_LINKML.length_of_found_feature,
    name="plannotateAnnotationReport__length_of_found_feature",
    curie=OPENCLONING_LINKML.curie("length_of_found_feature"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__length_of_found_feature,
    domain=None,
    range=Optional[int],
)

slots.plannotateAnnotationReport__percent_match_length = Slot(
    uri=OPENCLONING_LINKML.percent_match_length,
    name="plannotateAnnotationReport__percent_match_length",
    curie=OPENCLONING_LINKML.curie("percent_match_length"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__percent_match_length,
    domain=None,
    range=Optional[float],
)

slots.plannotateAnnotationReport__fragment = Slot(
    uri=OPENCLONING_LINKML.fragment,
    name="plannotateAnnotationReport__fragment",
    curie=OPENCLONING_LINKML.curie("fragment"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__fragment,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.plannotateAnnotationReport__database = Slot(
    uri=OPENCLONING_LINKML.database,
    name="plannotateAnnotationReport__database",
    curie=OPENCLONING_LINKML.curie("database"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__database,
    domain=None,
    range=Optional[str],
)

slots.plannotateAnnotationReport__Feature = Slot(
    uri=OPENCLONING_LINKML.Feature,
    name="plannotateAnnotationReport__Feature",
    curie=OPENCLONING_LINKML.curie("Feature"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__Feature,
    domain=None,
    range=Optional[str],
)

slots.plannotateAnnotationReport__Type = Slot(
    uri=OPENCLONING_LINKML.Type,
    name="plannotateAnnotationReport__Type",
    curie=OPENCLONING_LINKML.curie("Type"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__Type,
    domain=None,
    range=Optional[str],
)

slots.plannotateAnnotationReport__Description = Slot(
    uri=OPENCLONING_LINKML.Description,
    name="plannotateAnnotationReport__Description",
    curie=OPENCLONING_LINKML.curie("Description"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__Description,
    domain=None,
    range=Optional[str],
)

slots.plannotateAnnotationReport__sequence = Slot(
    uri=OPENCLONING_LINKML.sequence,
    name="plannotateAnnotationReport__sequence",
    curie=OPENCLONING_LINKML.curie("sequence"),
    model_uri=OPENCLONING_LINKML.plannotateAnnotationReport__sequence,
    domain=None,
    range=Optional[str],
)

slots.annotationSource__annotation_tool = Slot(
    uri=OPENCLONING_LINKML.annotation_tool,
    name="annotationSource__annotation_tool",
    curie=OPENCLONING_LINKML.curie("annotation_tool"),
    model_uri=OPENCLONING_LINKML.annotationSource__annotation_tool,
    domain=None,
    range=Union[str, "AnnotationTool"],
)

slots.annotationSource__annotation_tool_version = Slot(
    uri=OPENCLONING_LINKML.annotation_tool_version,
    name="annotationSource__annotation_tool_version",
    curie=OPENCLONING_LINKML.curie("annotation_tool_version"),
    model_uri=OPENCLONING_LINKML.annotationSource__annotation_tool_version,
    domain=None,
    range=Optional[str],
)

slots.annotationSource__annotation_report = Slot(
    uri=OPENCLONING_LINKML.annotation_report,
    name="annotationSource__annotation_report",
    curie=OPENCLONING_LINKML.curie("annotation_report"),
    model_uri=OPENCLONING_LINKML.annotationSource__annotation_report,
    domain=None,
    range=Optional[Union[Union[dict, AnnotationReport], list[Union[dict, AnnotationReport]]]],
)

slots.associatedFile__sequence_id = Slot(
    uri=OPENCLONING_LINKML.sequence_id,
    name="associatedFile__sequence_id",
    curie=OPENCLONING_LINKML.curie("sequence_id"),
    model_uri=OPENCLONING_LINKML.associatedFile__sequence_id,
    domain=None,
    range=Union[int, SequenceId],
)

slots.associatedFile__file_name = Slot(
    uri=OPENCLONING_LINKML.file_name,
    name="associatedFile__file_name",
    curie=OPENCLONING_LINKML.curie("file_name"),
    model_uri=OPENCLONING_LINKML.associatedFile__file_name,
    domain=None,
    range=str,
)

slots.associatedFile__file_type = Slot(
    uri=OPENCLONING_LINKML.file_type,
    name="associatedFile__file_type",
    curie=OPENCLONING_LINKML.curie("file_type"),
    model_uri=OPENCLONING_LINKML.associatedFile__file_type,
    domain=None,
    range=Union[str, "AssociatedFileType"],
)

slots.sequencingFile__alignment = Slot(
    uri=OPENCLONING_LINKML.alignment,
    name="sequencingFile__alignment",
    curie=OPENCLONING_LINKML.curie("alignment"),
    model_uri=OPENCLONING_LINKML.sequencingFile__alignment,
    domain=None,
    range=Union[str, list[str]],
)

slots.TextFileSequence_sequence_file_format = Slot(
    uri=OPENCLONING_LINKML.sequence_file_format,
    name="TextFileSequence_sequence_file_format",
    curie=OPENCLONING_LINKML.curie("sequence_file_format"),
    model_uri=OPENCLONING_LINKML.TextFileSequence_sequence_file_format,
    domain=TextFileSequence,
    range=Union[str, "SequenceFileFormat"],
)

slots.TextFileSequence_overhang_crick_3prime = Slot(
    uri=OPENCLONING_LINKML.overhang_crick_3prime,
    name="TextFileSequence_overhang_crick_3prime",
    curie=OPENCLONING_LINKML.curie("overhang_crick_3prime"),
    model_uri=OPENCLONING_LINKML.TextFileSequence_overhang_crick_3prime,
    domain=TextFileSequence,
    range=Optional[int],
)

slots.TextFileSequence_overhang_watson_3prime = Slot(
    uri=OPENCLONING_LINKML.overhang_watson_3prime,
    name="TextFileSequence_overhang_watson_3prime",
    curie=OPENCLONING_LINKML.curie("overhang_watson_3prime"),
    model_uri=OPENCLONING_LINKML.TextFileSequence_overhang_watson_3prime,
    domain=TextFileSequence,
    range=Optional[int],
)

slots.RestrictionSequenceCut_restriction_enzyme = Slot(
    uri=OPENCLONING_LINKML.restriction_enzyme,
    name="RestrictionSequenceCut_restriction_enzyme",
    curie=OPENCLONING_LINKML.curie("restriction_enzyme"),
    model_uri=OPENCLONING_LINKML.RestrictionSequenceCut_restriction_enzyme,
    domain=RestrictionSequenceCut,
    range=str,
)

slots.DatabaseSource_database_id = Slot(
    uri=SCHEMA.identifier,
    name="DatabaseSource_database_id",
    curie=SCHEMA.curie("identifier"),
    model_uri=OPENCLONING_LINKML.DatabaseSource_database_id,
    domain=DatabaseSource,
    range=int,
)

slots.CollectionOption_name = Slot(
    uri=SCHEMA.name,
    name="CollectionOption_name",
    curie=SCHEMA.curie("name"),
    model_uri=OPENCLONING_LINKML.CollectionOption_name,
    domain=CollectionOption,
    range=str,
)

slots.CollectionOptionInfo_name = Slot(
    uri=SCHEMA.name,
    name="CollectionOptionInfo_name",
    curie=SCHEMA.curie("name"),
    model_uri=OPENCLONING_LINKML.CollectionOptionInfo_name,
    domain=CollectionOptionInfo,
    range=Optional[str],
)

slots.ManuallyTypedSource_overhang_crick_3prime = Slot(
    uri=OPENCLONING_LINKML.overhang_crick_3prime,
    name="ManuallyTypedSource_overhang_crick_3prime",
    curie=OPENCLONING_LINKML.curie("overhang_crick_3prime"),
    model_uri=OPENCLONING_LINKML.ManuallyTypedSource_overhang_crick_3prime,
    domain=ManuallyTypedSource,
    range=Optional[int],
)

slots.ManuallyTypedSource_overhang_watson_3prime = Slot(
    uri=OPENCLONING_LINKML.overhang_watson_3prime,
    name="ManuallyTypedSource_overhang_watson_3prime",
    curie=OPENCLONING_LINKML.curie("overhang_watson_3prime"),
    model_uri=OPENCLONING_LINKML.ManuallyTypedSource_overhang_watson_3prime,
    domain=ManuallyTypedSource,
    range=Optional[int],
)

slots.UploadedFileSource_sequence_file_format = Slot(
    uri=OPENCLONING_LINKML.sequence_file_format,
    name="UploadedFileSource_sequence_file_format",
    curie=OPENCLONING_LINKML.curie("sequence_file_format"),
    model_uri=OPENCLONING_LINKML.UploadedFileSource_sequence_file_format,
    domain=UploadedFileSource,
    range=Union[str, "SequenceFileFormat"],
)

slots.WekWikGeneIdSource_repository_id = Slot(
    uri=OPENCLONING_LINKML.repository_id,
    name="WekWikGeneIdSource_repository_id",
    curie=OPENCLONING_LINKML.curie("repository_id"),
    model_uri=OPENCLONING_LINKML.WekWikGeneIdSource_repository_id,
    domain=WekWikGeneIdSource,
    range=str,
    pattern=re.compile(r"^\d+$"),
)

slots.SEVASource_repository_id = Slot(
    uri=OPENCLONING_LINKML.repository_id,
    name="SEVASource_repository_id",
    curie=OPENCLONING_LINKML.curie("repository_id"),
    model_uri=OPENCLONING_LINKML.SEVASource_repository_id,
    domain=SEVASource,
    range=str,
    pattern=re.compile(r"^pSEVA\d+.*$"),
)

slots.SEVASource_sequence_file_url = Slot(
    uri=OPENCLONING_LINKML.sequence_file_url,
    name="SEVASource_sequence_file_url",
    curie=OPENCLONING_LINKML.curie("sequence_file_url"),
    model_uri=OPENCLONING_LINKML.SEVASource_sequence_file_url,
    domain=SEVASource,
    range=str,
    pattern=re.compile(
        r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
    ),
)

slots.BenchlingUrlSource_repository_id = Slot(
    uri=OPENCLONING_LINKML.repository_id,
    name="BenchlingUrlSource_repository_id",
    curie=OPENCLONING_LINKML.curie("repository_id"),
    model_uri=OPENCLONING_LINKML.BenchlingUrlSource_repository_id,
    domain=BenchlingUrlSource,
    range=str,
    pattern=re.compile(r"^https:\/\/benchling\.com\/.+\.gb$"),
)

slots.SnapGenePlasmidSource_repository_id = Slot(
    uri=OPENCLONING_LINKML.repository_id,
    name="SnapGenePlasmidSource_repository_id",
    curie=OPENCLONING_LINKML.curie("repository_id"),
    model_uri=OPENCLONING_LINKML.SnapGenePlasmidSource_repository_id,
    domain=SnapGenePlasmidSource,
    range=str,
    pattern=re.compile(r"^.+\/.+$"),
)

slots.EuroscarfSource_repository_id = Slot(
    uri=OPENCLONING_LINKML.repository_id,
    name="EuroscarfSource_repository_id",
    curie=OPENCLONING_LINKML.curie("repository_id"),
    model_uri=OPENCLONING_LINKML.EuroscarfSource_repository_id,
    domain=EuroscarfSource,
    range=str,
    pattern=re.compile(r"^P\d+$"),
)

slots.IGEMSource_repository_id = Slot(
    uri=OPENCLONING_LINKML.repository_id,
    name="IGEMSource_repository_id",
    curie=OPENCLONING_LINKML.curie("repository_id"),
    model_uri=OPENCLONING_LINKML.IGEMSource_repository_id,
    domain=IGEMSource,
    range=str,
)

slots.IGEMSource_sequence_file_url = Slot(
    uri=OPENCLONING_LINKML.sequence_file_url,
    name="IGEMSource_sequence_file_url",
    curie=OPENCLONING_LINKML.curie("sequence_file_url"),
    model_uri=OPENCLONING_LINKML.IGEMSource_sequence_file_url,
    domain=IGEMSource,
    range=str,
    pattern=re.compile(
        r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
    ),
)

slots.RestrictionAndLigationSource_restriction_enzymes = Slot(
    uri=OPENCLONING_LINKML.restriction_enzymes,
    name="RestrictionAndLigationSource_restriction_enzymes",
    curie=OPENCLONING_LINKML.curie("restriction_enzymes"),
    model_uri=OPENCLONING_LINKML.RestrictionAndLigationSource_restriction_enzymes,
    domain=RestrictionAndLigationSource,
    range=Union[str, list[str]],
)
