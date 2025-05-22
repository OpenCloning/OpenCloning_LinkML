-- # Class: "NamedThing" Description: ""
--     * Slot: id Description: A unique identifier for a thing
-- # Abstract Class: "Sequence" Description: "Represents a sequence"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: type Description: Designates the class
--     * Slot: CloningStrategy_id Description: Autocreated FK slot
-- # Class: "TemplateSequence" Description: "Represents a sequence that is part of a template, where the actual sequence content will be determined by the user's actions"
--     * Slot: circular Description: Whether the sequence is circular or linear
--     * Slot: primer_design Description: Can be used to indicate the intended primer design for this sequence in the template
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: type Description: Designates the class
-- # Class: "TextFileSequence" Description: "A sequence (may have features) defined by the content of a text file"
--     * Slot: sequence_file_format Description: The format of a sequence file
--     * Slot: overhang_crick_3prime Description: Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand
--     * Slot: overhang_watson_3prime Description: The equivalent of `overhang_crick_3prime` but for the watson strand
--     * Slot: file_content Description:
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: type Description: Designates the class
-- # Class: "Primer" Description: "An oligonucleotide or primer"
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: sequence Description:
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: type Description: Designates the class
--     * Slot: CloningStrategy_id Description: Autocreated FK slot
-- # Class: "SequenceCut" Description: "Represents a cut in a DNA sequence"
--     * Slot: id Description:
--     * Slot: cut_watson Description: The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.
--     * Slot: overhang Description: The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.
-- # Class: "RestrictionSequenceCut" Description: "Represents a cut in a DNA sequence that is made by a restriction enzyme"
--     * Slot: id Description:
--     * Slot: restriction_enzyme Description:
--     * Slot: cut_watson Description: The position of the cut in the watson strand. The cut is made before the base at this position (zero-based), so that cut position 1 cuts after the first base.
--     * Slot: overhang Description: The length of the overhang that is left after the cut. It can be negative, same meaning as in pydna's `dseq::ovhg` and biopython's `Bio.Restriction.RestrictionType.ovhg`.
-- # Abstract Class: "Source" Description: "Represents the source of a sequence"
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: CloningStrategy_id Description: Autocreated FK slot
-- # Class: "DatabaseSource" Description: "Represents the source of a sequence that is identified by a database id"
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "CollectionSource" Description: "Represents a collection of possible sources in a template"
--     * Slot: category_id Description: The identifier of the category of the part in the template
--     * Slot: title Description: The title of the category
--     * Slot: description Description: A description of the category
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "CollectionOption" Description: "Represents an option in a collection"
--     * Slot: id Description:
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: CollectionSource_id Description: Autocreated FK slot
--     * Slot: source_id Description: The source of the sequence for this option
--     * Slot: info_id Description: Additional information about this option
-- # Class: "CollectionOptionInfo" Description: "Additional information about a collection option"
--     * Slot: id Description:
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A description of the option
--     * Slot: type Description: The type of the option, this is redundant with the type of the source, and could be removed.
--     * Slot: resistance Description: The antibiotic resistance of the plasmid
--     * Slot: well Description: The well position in the kit plate
-- # Class: "ManuallyTypedSource" Description: "Represents the source of a sequence that is manually typed by the user"
--     * Slot: overhang_crick_3prime Description: Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand
--     * Slot: overhang_watson_3prime Description: The equivalent of `overhang_crick_3prime` but for the watson strand
--     * Slot: user_input Description:
--     * Slot: circular Description: Whether the sequence is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "UploadedFileSource" Description: "Represents the source of a sequence that is uploaded as a file"
--     * Slot: sequence_file_format Description: The format of a sequence file
--     * Slot: file_name Description: The name of the file
--     * Slot: index_in_file Description: The index of the sequence in the file
--     * Slot: circularize Description: Whether the sequence should be circularized (FASTA only)
--     * Slot: coordinates Description: If provided, coordinates within the sequence of the file to extract a subsequence
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "RepositoryIdSource" Description: "Represents the source of a sequence that is identified by a repository id"
--     * Slot: repository_id Description: The id of the sequence in the repository
--     * Slot: repository_name Description:
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "AddgeneIdSource" Description: "Represents the source of a sequence that is identified by an Addgene id"
--     * Slot: sequence_file_url Description: The URL of a sequence file
--     * Slot: addgene_sequence_type Description:
--     * Slot: repository_id Description: The id of the sequence in the repository
--     * Slot: repository_name Description:
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "WekWikGeneIdSource" Description: "Represents the source of a sequence that is identified by a WekWikGene id"
--     * Slot: sequence_file_url Description: The URL of a sequence file
--     * Slot: repository_id Description: The id of the gene in the WekWik gene database
--     * Slot: repository_name Description:
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "SEVASource" Description: "Represents the source of a sequence that is identified by a SEVA id"
--     * Slot: sequence_file_url Description: The URL of the sequence file, which can refer to a a gb file hosted on the SEVA website or an entry in the NCBI.
--     * Slot: repository_id Description: The SEVA plasmid name
--     * Slot: repository_name Description:
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "BenchlingUrlSource" Description: "Represents the source of a sequence that is identified by a Benchling URL"
--     * Slot: repository_id Description: The url of the gb file associated with the sequence
--     * Slot: repository_name Description:
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "SnapGenePlasmidSource" Description: "Represents the source of a sequence from the SnapGene plasmid library identified by a SnapGene subpath of https://www.snapgene.com/plasmids/"
--     * Slot: repository_id Description: The subpath of the plasmid in the SnapGene plasmid library. Requesting the plasmid is possible with https://www.snapgene.com/local/fetch.php?set={category_path}&plasmid={plasmid['subpath']} where category_path is the left part of the subpath before the first / and plasmid is the subpath after the /.
--     * Slot: repository_name Description:
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "EuroscarfSource" Description: "Represents the source of a sequence from the Euroscarf plasmid library"
--     * Slot: repository_id Description: The id of the plasmid in the Euroscarf plasmid library
--     * Slot: repository_name Description:
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "IGEMSource" Description: "Represents the source of a sequence from an iGEM collection"
--     * Slot: sequence_file_url Description: The URL of the sequence file, for now github repository
--     * Slot: repository_id Description: The unique identifier of the sequence in the iGEM collection (for now, {part_id}-{plasmid_backbone})
--     * Slot: repository_name Description:
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "GenomeCoordinatesSource" Description: "Represents the source of a sequence that is identified by genome coordinates, requested from NCBI"
--     * Slot: assembly_accession Description: The accession of the assembly
--     * Slot: sequence_accession Description: The accession of the sequence
--     * Slot: locus_tag Description: The locus tag of the sequence
--     * Slot: gene_id Description: The gene id of the sequence
--     * Slot: start Description: The starting coordinate (1-based) of the sequence in the sequence accession
--     * Slot: end Description: The ending coordinate (1-based) of the sequence in the sequence accession
--     * Slot: strand Description: The strand of the sequence in the sequence accession, should be 1 or -1
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "SequenceCutSource" Description: "Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting."
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: left_edge_id Description:
--     * Slot: right_edge_id Description:
-- # Class: "RestrictionEnzymeDigestionSource" Description: "Represents the source of a sequence that is a subfragment of another sequence, generated by sequence cutting using restriction enzymes."
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: left_edge_id Description:
--     * Slot: right_edge_id Description:
-- # Class: "AssemblyFragment" Description: "Represents a fragment in an assembly"
--     * Slot: id Description:
--     * Slot: sequence Description:
--     * Slot: left_location Description:
--     * Slot: right_location Description:
--     * Slot: reverse_complemented Description: Whether the sequence is reverse complemented in the assembly
--     * Slot: AssemblySource_id Description: Autocreated FK slot
--     * Slot: PCRSource_id Description: Autocreated FK slot
--     * Slot: LigationSource_id Description: Autocreated FK slot
--     * Slot: HomologousRecombinationSource_id Description: Autocreated FK slot
--     * Slot: GibsonAssemblySource_id Description: Autocreated FK slot
--     * Slot: InFusionSource_id Description: Autocreated FK slot
--     * Slot: OverlapExtensionPCRLigationSource_id Description: Autocreated FK slot
--     * Slot: InVivoAssemblySource_id Description: Autocreated FK slot
--     * Slot: RestrictionAndLigationSource_id Description: Autocreated FK slot
--     * Slot: GatewaySource_id Description: Autocreated FK slot
--     * Slot: CreLoxRecombinationSource_id Description: Autocreated FK slot
--     * Slot: CRISPRSource_id Description: Autocreated FK slot
-- # Class: "AssemblySource" Description: "Represents the source of a sequence that is an assembly of other sequences"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "PCRSource" Description: "Represents the source of a sequence that is generated by PCR"
--     * Slot: add_primer_features Description: Whether to add primer features to the PCR product
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "LigationSource" Description: "Represents the source of a sequence that is generated by ligation with sticky or blunt ends."
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "HomologousRecombinationSource" Description: "Represents the source of a sequence that is generated by homologous recombination"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "GibsonAssemblySource" Description: "Represents the source of a sequence that is generated by Gibson assembly"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "InFusionSource" Description: "Represents the source of a sequence that is generated by In-Fusion cloning by Takara Bio"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "OverlapExtensionPCRLigationSource" Description: "Represents the source of a sequence that is generated by ligation of PCR products as part of overlap extension PCR. Algorithmically equivalent to Gibson assembly."
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "InVivoAssemblySource" Description: "Represents the source of a sequence that is generated by in vivo assembly. Algorithmically equivalent to Gibson assembly."
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "RestrictionAndLigationSource" Description: "Represents the source of a sequence that is generated by restriction and ligation"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "GatewaySource" Description: "Represents the source of a sequence that is generated by Gateway cloning"
--     * Slot: reaction_type Description:
--     * Slot: greedy Description: Whether to use a greedy consensus sequence for att sites (see https://github.com/manulera/GateWayMine)
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "CreLoxRecombinationSource" Description: "Represents the source of a sequence that is generated by Cre - Lox recombination"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "CRISPRSource" Description: "Represents the source of a sequence that is generated by CRISPR"
--     * Slot: circular Description: Whether the assembly is circular or not
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "OligoHybridizationSource" Description: "Represents the source of a sequence that is generated by oligo hybridization"
--     * Slot: overhang_crick_3prime Description: Taken from pydna's `dseq::ovhg`An integer describing the length of the crick strand overhang in the 5' of the molecule, or 3' of the crick strand
--     * Slot: forward_oligo Description: The forward oligo used in the hybridization
--     * Slot: reverse_oligo Description: The reverse oligo used in the hybridization
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "PolymeraseExtensionSource" Description: "Represents the source of a sequence that is generated by polymerase extension"
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "CloningStrategy" Description: "Represents a cloning strategy"
--     * Slot: id Description:
--     * Slot: description Description: A description of the cloning strategy
--     * Slot: schema_version Description: The version of the schema that was used to generate this cloning strategy
--     * Slot: backend_version Description: The version of the backend that was used to generate this cloning strategy
--     * Slot: frontend_version Description: The version of the frontend that was used to generate this cloning strategy
-- # Class: "AnnotationReport" Description: "Represents a report of an annotation step"
--     * Slot: id Description:
--     * Slot: type Description: Designates the class
--     * Slot: AnnotationSource_id Description: Autocreated FK slot
-- # Class: "PlannotateAnnotationReport" Description: "Represents a report of an annotation step using Plannotate"
--     * Slot: id Description:
--     * Slot: sseqid Description:
--     * Slot: start_location Description:
--     * Slot: end_location Description:
--     * Slot: strand Description:
--     * Slot: percent_identity Description:
--     * Slot: full_length_of_feature_in_db Description:
--     * Slot: length_of_found_feature Description:
--     * Slot: percent_match_length Description:
--     * Slot: fragment Description:
--     * Slot: database Description:
--     * Slot: Feature Description:
--     * Slot: Type Description:
--     * Slot: Description Description:
--     * Slot: sequence Description:
--     * Slot: type Description: Designates the class
-- # Class: "AnnotationSource" Description: "Represents a computational step in which sequence features are annotated in a sequence"
--     * Slot: annotation_tool Description:
--     * Slot: annotation_tool_version Description: The version of the annotation tool
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "ReverseComplementSource" Description: "Represents the in-silico transformation of a sequence into its reverse complement"
--     * Slot: output Description: Identifier of the sequence that is the output of this source.
--     * Slot: type Description: Designates the class
--     * Slot: output_name Description: Used to specify the name of the output sequence
--     * Slot: database_id Description: The id of an entity in a database
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "AssociatedFile" Description: "Represents a file associated with a sequence"
--     * Slot: id Description:
--     * Slot: type Description: Designates the class
--     * Slot: sequence_id Description: The sequence this file is associated with
--     * Slot: file_name Description: The name of the file
--     * Slot: file_type Description: The type of file
--     * Slot: CloningStrategy_id Description: Autocreated FK slot
-- # Class: "SequencingFile" Description: "Represents a sequencing file and its alignment to a sequence"
--     * Slot: id Description:
--     * Slot: type Description: Designates the class
--     * Slot: sequence_id Description: The sequence this file is associated with
--     * Slot: file_name Description: The name of the file
--     * Slot: file_type Description: The type of file
-- # Class: "Source_input" Description: ""
--     * Slot: Source_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "DatabaseSource_input" Description: ""
--     * Slot: DatabaseSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "CollectionSource_image" Description: ""
--     * Slot: CollectionSource_id Description: Autocreated FK slot
--     * Slot: image Description: URL and size of the image representing this category. For images with size specification, this is a list with two elements: [url, size].
-- # Class: "CollectionSource_input" Description: ""
--     * Slot: CollectionSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "ManuallyTypedSource_input" Description: ""
--     * Slot: ManuallyTypedSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "UploadedFileSource_input" Description: ""
--     * Slot: UploadedFileSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "RepositoryIdSource_input" Description: ""
--     * Slot: RepositoryIdSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "AddgeneIdSource_input" Description: ""
--     * Slot: AddgeneIdSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "WekWikGeneIdSource_input" Description: ""
--     * Slot: WekWikGeneIdSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "SEVASource_input" Description: ""
--     * Slot: SEVASource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "BenchlingUrlSource_input" Description: ""
--     * Slot: BenchlingUrlSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "SnapGenePlasmidSource_input" Description: ""
--     * Slot: SnapGenePlasmidSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "EuroscarfSource_input" Description: ""
--     * Slot: EuroscarfSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "IGEMSource_input" Description: ""
--     * Slot: IGEMSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "GenomeCoordinatesSource_input" Description: ""
--     * Slot: GenomeCoordinatesSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "SequenceCutSource_input" Description: ""
--     * Slot: SequenceCutSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "RestrictionEnzymeDigestionSource_input" Description: ""
--     * Slot: RestrictionEnzymeDigestionSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "AssemblySource_input" Description: ""
--     * Slot: AssemblySource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "PCRSource_input" Description: ""
--     * Slot: PCRSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "LigationSource_input" Description: ""
--     * Slot: LigationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "HomologousRecombinationSource_input" Description: ""
--     * Slot: HomologousRecombinationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "GibsonAssemblySource_input" Description: ""
--     * Slot: GibsonAssemblySource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "InFusionSource_input" Description: ""
--     * Slot: InFusionSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "OverlapExtensionPCRLigationSource_input" Description: ""
--     * Slot: OverlapExtensionPCRLigationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "InVivoAssemblySource_input" Description: ""
--     * Slot: InVivoAssemblySource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "RestrictionAndLigationSource_restriction_enzymes" Description: ""
--     * Slot: RestrictionAndLigationSource_id Description: Autocreated FK slot
--     * Slot: restriction_enzymes Description:
-- # Class: "RestrictionAndLigationSource_input" Description: ""
--     * Slot: RestrictionAndLigationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "GatewaySource_input" Description: ""
--     * Slot: GatewaySource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "CreLoxRecombinationSource_input" Description: ""
--     * Slot: CreLoxRecombinationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "CRISPRSource_guides" Description: ""
--     * Slot: CRISPRSource_id Description: Autocreated FK slot
--     * Slot: guides_id Description: The guide RNAs used in the CRISPR
-- # Class: "CRISPRSource_input" Description: ""
--     * Slot: CRISPRSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "OligoHybridizationSource_input" Description: ""
--     * Slot: OligoHybridizationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "PolymeraseExtensionSource_input" Description: ""
--     * Slot: PolymeraseExtensionSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "AnnotationSource_input" Description: ""
--     * Slot: AnnotationSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "ReverseComplementSource_input" Description: ""
--     * Slot: ReverseComplementSource_id Description: Autocreated FK slot
--     * Slot: input_id Description: The sequences that are an input to this source. If the source represents external import of a sequence, it's empty.
-- # Class: "SequencingFile_alignment" Description: ""
--     * Slot: SequencingFile_id Description: Autocreated FK slot
--     * Slot: alignment Description: The alignment of the sequencing read to the sequence. List of strings representing aligned sequences.

CREATE TABLE "NamedThing" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "TemplateSequence" (
	circular BOOLEAN,
	primer_design TEXT,
	id INTEGER NOT NULL,
	type TEXT,
	PRIMARY KEY (id)
);
CREATE TABLE "TextFileSequence" (
	sequence_file_format VARCHAR(8) NOT NULL,
	overhang_crick_3prime INTEGER,
	overhang_watson_3prime INTEGER,
	file_content TEXT,
	id INTEGER NOT NULL,
	type TEXT,
	PRIMARY KEY (id)
);
CREATE TABLE "SequenceCut" (
	id INTEGER NOT NULL,
	cut_watson INTEGER NOT NULL,
	overhang INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "RestrictionSequenceCut" (
	id INTEGER NOT NULL,
	restriction_enzyme TEXT NOT NULL,
	cut_watson INTEGER NOT NULL,
	overhang INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "CollectionOptionInfo" (
	id INTEGER NOT NULL,
	name TEXT,
	description TEXT,
	type VARCHAR(14),
	resistance TEXT,
	well TEXT,
	PRIMARY KEY (id)
);
CREATE TABLE "CloningStrategy" (
	id INTEGER NOT NULL,
	description TEXT,
	schema_version TEXT,
	backend_version TEXT,
	frontend_version TEXT,
	PRIMARY KEY (id)
);
CREATE TABLE "PlannotateAnnotationReport" (
	id INTEGER NOT NULL,
	sseqid TEXT,
	start_location INTEGER,
	end_location INTEGER,
	strand INTEGER,
	percent_identity FLOAT,
	full_length_of_feature_in_db INTEGER,
	length_of_found_feature INTEGER,
	percent_match_length FLOAT,
	fragment BOOLEAN,
	"database" TEXT,
	"Feature" TEXT,
	"Type" TEXT,
	"Description" TEXT,
	sequence TEXT,
	type TEXT,
	PRIMARY KEY (id)
);
CREATE TABLE "Sequence" (
	id INTEGER NOT NULL,
	type TEXT,
	"CloningStrategy_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CloningStrategy_id") REFERENCES "CloningStrategy" (id)
);
CREATE TABLE "Primer" (
	name TEXT,
	database_id INTEGER,
	sequence TEXT,
	id INTEGER NOT NULL,
	type TEXT,
	"CloningStrategy_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CloningStrategy_id") REFERENCES "CloningStrategy" (id)
);
CREATE TABLE "Source" (
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	"CloningStrategy_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id),
	FOREIGN KEY("CloningStrategy_id") REFERENCES "CloningStrategy" (id)
);
CREATE TABLE "DatabaseSource" (
	database_id INTEGER NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "CollectionSource" (
	category_id TEXT,
	title TEXT NOT NULL,
	description TEXT,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "ManuallyTypedSource" (
	overhang_crick_3prime INTEGER,
	overhang_watson_3prime INTEGER,
	user_input TEXT NOT NULL,
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "UploadedFileSource" (
	sequence_file_format VARCHAR(8) NOT NULL,
	file_name TEXT,
	index_in_file INTEGER,
	circularize BOOLEAN,
	coordinates TEXT,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "RepositoryIdSource" (
	repository_id TEXT NOT NULL,
	repository_name VARCHAR(10) NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "AddgeneIdSource" (
	sequence_file_url TEXT,
	addgene_sequence_type VARCHAR(14),
	repository_id TEXT NOT NULL,
	repository_name VARCHAR(10) NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "WekWikGeneIdSource" (
	sequence_file_url TEXT,
	repository_id TEXT NOT NULL,
	repository_name VARCHAR(10) NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "SEVASource" (
	sequence_file_url TEXT NOT NULL,
	repository_id TEXT NOT NULL,
	repository_name VARCHAR(10) NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "BenchlingUrlSource" (
	repository_id TEXT NOT NULL,
	repository_name VARCHAR(10) NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "SnapGenePlasmidSource" (
	repository_id TEXT NOT NULL,
	repository_name VARCHAR(10) NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "EuroscarfSource" (
	repository_id TEXT NOT NULL,
	repository_name VARCHAR(10) NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "IGEMSource" (
	sequence_file_url TEXT NOT NULL,
	repository_id TEXT NOT NULL,
	repository_name VARCHAR(10) NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "GenomeCoordinatesSource" (
	assembly_accession TEXT,
	sequence_accession TEXT NOT NULL,
	locus_tag TEXT,
	gene_id INTEGER,
	start INTEGER NOT NULL,
	"end" INTEGER NOT NULL,
	strand INTEGER NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "SequenceCutSource" (
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	left_edge_id INTEGER,
	right_edge_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id),
	FOREIGN KEY(left_edge_id) REFERENCES "SequenceCut" (id),
	FOREIGN KEY(right_edge_id) REFERENCES "SequenceCut" (id)
);
CREATE TABLE "RestrictionEnzymeDigestionSource" (
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	left_edge_id INTEGER,
	right_edge_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id),
	FOREIGN KEY(left_edge_id) REFERENCES "RestrictionSequenceCut" (id),
	FOREIGN KEY(right_edge_id) REFERENCES "RestrictionSequenceCut" (id)
);
CREATE TABLE "AssemblySource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "PCRSource" (
	add_primer_features BOOLEAN,
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "LigationSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "HomologousRecombinationSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "GibsonAssemblySource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "InFusionSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "OverlapExtensionPCRLigationSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "InVivoAssemblySource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "RestrictionAndLigationSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "GatewaySource" (
	reaction_type VARCHAR(2) NOT NULL,
	greedy BOOLEAN,
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "CreLoxRecombinationSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "CRISPRSource" (
	circular BOOLEAN,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "OligoHybridizationSource" (
	overhang_crick_3prime INTEGER,
	forward_oligo INTEGER NOT NULL,
	reverse_oligo INTEGER NOT NULL,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(forward_oligo) REFERENCES "Primer" (id),
	FOREIGN KEY(reverse_oligo) REFERENCES "Primer" (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "PolymeraseExtensionSource" (
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "AnnotationSource" (
	annotation_tool VARCHAR(10) NOT NULL,
	annotation_tool_version TEXT,
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "ReverseComplementSource" (
	output INTEGER,
	type TEXT,
	output_name TEXT,
	database_id INTEGER,
	id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(output) REFERENCES "Sequence" (id)
);
CREATE TABLE "AssociatedFile" (
	id INTEGER NOT NULL,
	type TEXT,
	sequence_id INTEGER NOT NULL,
	file_name TEXT NOT NULL,
	file_type VARCHAR(15) NOT NULL,
	"CloningStrategy_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id),
	FOREIGN KEY("CloningStrategy_id") REFERENCES "CloningStrategy" (id)
);
CREATE TABLE "SequencingFile" (
	id INTEGER NOT NULL,
	type TEXT,
	sequence_id INTEGER NOT NULL,
	file_name TEXT NOT NULL,
	file_type VARCHAR(15) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(sequence_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "CollectionOption" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"CollectionSource_id" INTEGER,
	source_id INTEGER NOT NULL,
	info_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CollectionSource_id") REFERENCES "CollectionSource" (id),
	FOREIGN KEY(source_id) REFERENCES "Source" (id),
	FOREIGN KEY(info_id) REFERENCES "CollectionOptionInfo" (id)
);
CREATE TABLE "AssemblyFragment" (
	id INTEGER NOT NULL,
	sequence INTEGER NOT NULL,
	left_location TEXT,
	right_location TEXT,
	reverse_complemented BOOLEAN NOT NULL,
	"AssemblySource_id" INTEGER,
	"PCRSource_id" INTEGER,
	"LigationSource_id" INTEGER,
	"HomologousRecombinationSource_id" INTEGER,
	"GibsonAssemblySource_id" INTEGER,
	"InFusionSource_id" INTEGER,
	"OverlapExtensionPCRLigationSource_id" INTEGER,
	"InVivoAssemblySource_id" INTEGER,
	"RestrictionAndLigationSource_id" INTEGER,
	"GatewaySource_id" INTEGER,
	"CreLoxRecombinationSource_id" INTEGER,
	"CRISPRSource_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(sequence) REFERENCES "Sequence" (id),
	FOREIGN KEY("AssemblySource_id") REFERENCES "AssemblySource" (id),
	FOREIGN KEY("PCRSource_id") REFERENCES "PCRSource" (id),
	FOREIGN KEY("LigationSource_id") REFERENCES "LigationSource" (id),
	FOREIGN KEY("HomologousRecombinationSource_id") REFERENCES "HomologousRecombinationSource" (id),
	FOREIGN KEY("GibsonAssemblySource_id") REFERENCES "GibsonAssemblySource" (id),
	FOREIGN KEY("InFusionSource_id") REFERENCES "InFusionSource" (id),
	FOREIGN KEY("OverlapExtensionPCRLigationSource_id") REFERENCES "OverlapExtensionPCRLigationSource" (id),
	FOREIGN KEY("InVivoAssemblySource_id") REFERENCES "InVivoAssemblySource" (id),
	FOREIGN KEY("RestrictionAndLigationSource_id") REFERENCES "RestrictionAndLigationSource" (id),
	FOREIGN KEY("GatewaySource_id") REFERENCES "GatewaySource" (id),
	FOREIGN KEY("CreLoxRecombinationSource_id") REFERENCES "CreLoxRecombinationSource" (id),
	FOREIGN KEY("CRISPRSource_id") REFERENCES "CRISPRSource" (id)
);
CREATE TABLE "AnnotationReport" (
	id INTEGER NOT NULL,
	type TEXT,
	"AnnotationSource_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AnnotationSource_id") REFERENCES "AnnotationSource" (id)
);
CREATE TABLE "Source_input" (
	"Source_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("Source_id", input_id),
	FOREIGN KEY("Source_id") REFERENCES "Source" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "DatabaseSource_input" (
	"DatabaseSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("DatabaseSource_id", input_id),
	FOREIGN KEY("DatabaseSource_id") REFERENCES "DatabaseSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "CollectionSource_image" (
	"CollectionSource_id" INTEGER,
	image TEXT,
	PRIMARY KEY ("CollectionSource_id", image),
	FOREIGN KEY("CollectionSource_id") REFERENCES "CollectionSource" (id)
);
CREATE TABLE "CollectionSource_input" (
	"CollectionSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("CollectionSource_id", input_id),
	FOREIGN KEY("CollectionSource_id") REFERENCES "CollectionSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "ManuallyTypedSource_input" (
	"ManuallyTypedSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("ManuallyTypedSource_id", input_id),
	FOREIGN KEY("ManuallyTypedSource_id") REFERENCES "ManuallyTypedSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "UploadedFileSource_input" (
	"UploadedFileSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("UploadedFileSource_id", input_id),
	FOREIGN KEY("UploadedFileSource_id") REFERENCES "UploadedFileSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "RepositoryIdSource_input" (
	"RepositoryIdSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("RepositoryIdSource_id", input_id),
	FOREIGN KEY("RepositoryIdSource_id") REFERENCES "RepositoryIdSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "AddgeneIdSource_input" (
	"AddgeneIdSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("AddgeneIdSource_id", input_id),
	FOREIGN KEY("AddgeneIdSource_id") REFERENCES "AddgeneIdSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "WekWikGeneIdSource_input" (
	"WekWikGeneIdSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("WekWikGeneIdSource_id", input_id),
	FOREIGN KEY("WekWikGeneIdSource_id") REFERENCES "WekWikGeneIdSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "SEVASource_input" (
	"SEVASource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("SEVASource_id", input_id),
	FOREIGN KEY("SEVASource_id") REFERENCES "SEVASource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "BenchlingUrlSource_input" (
	"BenchlingUrlSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("BenchlingUrlSource_id", input_id),
	FOREIGN KEY("BenchlingUrlSource_id") REFERENCES "BenchlingUrlSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "SnapGenePlasmidSource_input" (
	"SnapGenePlasmidSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("SnapGenePlasmidSource_id", input_id),
	FOREIGN KEY("SnapGenePlasmidSource_id") REFERENCES "SnapGenePlasmidSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "EuroscarfSource_input" (
	"EuroscarfSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("EuroscarfSource_id", input_id),
	FOREIGN KEY("EuroscarfSource_id") REFERENCES "EuroscarfSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "IGEMSource_input" (
	"IGEMSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("IGEMSource_id", input_id),
	FOREIGN KEY("IGEMSource_id") REFERENCES "IGEMSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "GenomeCoordinatesSource_input" (
	"GenomeCoordinatesSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("GenomeCoordinatesSource_id", input_id),
	FOREIGN KEY("GenomeCoordinatesSource_id") REFERENCES "GenomeCoordinatesSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "SequenceCutSource_input" (
	"SequenceCutSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("SequenceCutSource_id", input_id),
	FOREIGN KEY("SequenceCutSource_id") REFERENCES "SequenceCutSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "RestrictionEnzymeDigestionSource_input" (
	"RestrictionEnzymeDigestionSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("RestrictionEnzymeDigestionSource_id", input_id),
	FOREIGN KEY("RestrictionEnzymeDigestionSource_id") REFERENCES "RestrictionEnzymeDigestionSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "AssemblySource_input" (
	"AssemblySource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("AssemblySource_id", input_id),
	FOREIGN KEY("AssemblySource_id") REFERENCES "AssemblySource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "PCRSource_input" (
	"PCRSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("PCRSource_id", input_id),
	FOREIGN KEY("PCRSource_id") REFERENCES "PCRSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "LigationSource_input" (
	"LigationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("LigationSource_id", input_id),
	FOREIGN KEY("LigationSource_id") REFERENCES "LigationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "HomologousRecombinationSource_input" (
	"HomologousRecombinationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("HomologousRecombinationSource_id", input_id),
	FOREIGN KEY("HomologousRecombinationSource_id") REFERENCES "HomologousRecombinationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "GibsonAssemblySource_input" (
	"GibsonAssemblySource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("GibsonAssemblySource_id", input_id),
	FOREIGN KEY("GibsonAssemblySource_id") REFERENCES "GibsonAssemblySource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "InFusionSource_input" (
	"InFusionSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("InFusionSource_id", input_id),
	FOREIGN KEY("InFusionSource_id") REFERENCES "InFusionSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "OverlapExtensionPCRLigationSource_input" (
	"OverlapExtensionPCRLigationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("OverlapExtensionPCRLigationSource_id", input_id),
	FOREIGN KEY("OverlapExtensionPCRLigationSource_id") REFERENCES "OverlapExtensionPCRLigationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "InVivoAssemblySource_input" (
	"InVivoAssemblySource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("InVivoAssemblySource_id", input_id),
	FOREIGN KEY("InVivoAssemblySource_id") REFERENCES "InVivoAssemblySource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "RestrictionAndLigationSource_restriction_enzymes" (
	"RestrictionAndLigationSource_id" INTEGER,
	restriction_enzymes TEXT NOT NULL,
	PRIMARY KEY ("RestrictionAndLigationSource_id", restriction_enzymes),
	FOREIGN KEY("RestrictionAndLigationSource_id") REFERENCES "RestrictionAndLigationSource" (id)
);
CREATE TABLE "RestrictionAndLigationSource_input" (
	"RestrictionAndLigationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("RestrictionAndLigationSource_id", input_id),
	FOREIGN KEY("RestrictionAndLigationSource_id") REFERENCES "RestrictionAndLigationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "GatewaySource_input" (
	"GatewaySource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("GatewaySource_id", input_id),
	FOREIGN KEY("GatewaySource_id") REFERENCES "GatewaySource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "CreLoxRecombinationSource_input" (
	"CreLoxRecombinationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("CreLoxRecombinationSource_id", input_id),
	FOREIGN KEY("CreLoxRecombinationSource_id") REFERENCES "CreLoxRecombinationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "CRISPRSource_guides" (
	"CRISPRSource_id" INTEGER,
	guides_id INTEGER NOT NULL,
	PRIMARY KEY ("CRISPRSource_id", guides_id),
	FOREIGN KEY("CRISPRSource_id") REFERENCES "CRISPRSource" (id),
	FOREIGN KEY(guides_id) REFERENCES "Primer" (id)
);
CREATE TABLE "CRISPRSource_input" (
	"CRISPRSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("CRISPRSource_id", input_id),
	FOREIGN KEY("CRISPRSource_id") REFERENCES "CRISPRSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "OligoHybridizationSource_input" (
	"OligoHybridizationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("OligoHybridizationSource_id", input_id),
	FOREIGN KEY("OligoHybridizationSource_id") REFERENCES "OligoHybridizationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "PolymeraseExtensionSource_input" (
	"PolymeraseExtensionSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("PolymeraseExtensionSource_id", input_id),
	FOREIGN KEY("PolymeraseExtensionSource_id") REFERENCES "PolymeraseExtensionSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "AnnotationSource_input" (
	"AnnotationSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("AnnotationSource_id", input_id),
	FOREIGN KEY("AnnotationSource_id") REFERENCES "AnnotationSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "ReverseComplementSource_input" (
	"ReverseComplementSource_id" INTEGER,
	input_id INTEGER,
	PRIMARY KEY ("ReverseComplementSource_id", input_id),
	FOREIGN KEY("ReverseComplementSource_id") REFERENCES "ReverseComplementSource" (id),
	FOREIGN KEY(input_id) REFERENCES "Sequence" (id)
);
CREATE TABLE "SequencingFile_alignment" (
	"SequencingFile_id" INTEGER,
	alignment TEXT NOT NULL,
	PRIMARY KEY ("SequencingFile_id", alignment),
	FOREIGN KEY("SequencingFile_id") REFERENCES "SequencingFile" (id)
);
