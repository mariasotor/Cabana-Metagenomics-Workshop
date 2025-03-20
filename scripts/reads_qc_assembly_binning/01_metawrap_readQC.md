# Quality control of metagenomic reads using the Read QC module of metaWRAP

Each participant will be responsible for analyzing one sample. The metagenomic samples are provided as compressed FASTA files (.fasta.gz), which serve as input for the Read QC module of metaWRAP.

In brief, this module trims adapters and low-quality bases using Trim Galore (default parameters), removes human contamination with BMTagger using the CHM13 human genome assembly, and generates a visual quality report with FastQC.
