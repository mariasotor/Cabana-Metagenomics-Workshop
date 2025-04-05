# Quality assesment of MAGs

### Tools Overview

Evaluating the quality of refined bins is crucial to ensure that the recovered MAGs meet medium to high-quality standards and are free from contamination. We will be using two tools for this assessment:

- **CheckM2**: Estimates genome completeness and contamination by analyzing the presence of single-copy marker genes. 
- **GUNC** (Genome UNClutterer): Detects chimeric MAGs and taxonomic contamination by analyzing phylogenetic inconsistencies. This ensures that MAGs represent single, coherent genomes rather than artificial assemblies of multiple organisms.

### Setting Up Output Directories

Create a new folder named `05_MAGs_qc`. Inside this folder, create the following subdirectories:

📂 `05_MAGs_qc`/
├── 📁 `checkm2_out`/
├── 📁 `gunc_out`/
├── 📁 `checkm2_and_gunc_out_concat`/
