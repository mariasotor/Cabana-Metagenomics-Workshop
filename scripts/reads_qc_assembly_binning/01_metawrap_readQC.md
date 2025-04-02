# Quality control of metagenomic reads using the Read QC module of metaWRAP

Each participant will analyze one metagenomic sample containing approximately 15 million reads. The sequencing data is provided in FASTQ format (.fastq), serving as input for the Read QC module of metaWRAP.

This module performs three key steps:

**Adapter and quality trimming** – Uses Trim Galore (default settings) to remove adapters and low-quality bases.
**Human contamination removal** – Employs BMTagger with the CHM13 human genome assembly. <br>
**Quality assessment** – Generates a visual quality report with FastQC.

Before running the metaWRAP Read QC module, we must create a manifest file to specify the paired sequencing files. This file must be in comma-separated (CSV) format with three columns: ID (Sample identifier), R1 (Path to the forward read file), R2 (Path to the reverse read file). The manifest file ensures a standardized input format and facilitates scalability. 

To contruct such manifest follow the instructions here: [generate_manifest] (https://github.com/mariasotor/Cabana-Metagenomics-Workshop/blob/main/helper_sripts/generate_manifest.md)
