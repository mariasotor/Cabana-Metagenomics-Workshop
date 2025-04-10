# Selection of Representative Genomes Using dRep

During the independent assembly of each sample within a project, highly similar MAGs may be reconstructed. This redundancy in the MAGs dataset must be resolved before estimating MAG abundance in metagenomic samples. If not addressed, redundant MAGs can lead to:
- Ambiguous read mapping, where sequencing reads align to multiple similar MAGs, reducing mapping accuracy.
- Artificially low abundance estimates, as reads are distributed among redundant MAGs instead of a single representative genome.

### dRep Overview
To eliminate redundancy in our set of curated MAGs, we will use dRep, a tool designed to dereplicate MAGs by clustering similar genomes and selecting the highest-quality representative from each cluster. This ensures that only the most complete, least contaminated, and best-assembled genomes are retained for downstream analysis.

### Setting Up Output Directories

Create a new folder named `08_drep`. Inside this folder, create the following subdirectory:

📂 `08_drep`/ <br>
├── 📁 `drep_out`/

### Generating Required Input Files

We will use the Dereplicate workflow in dRep, which requires a set of MAGs as input. These MAGs can be specified using wildcard expansion (MAGs_folder/*) or provided in a text file listing the paths to each MAG (used here). Using a text file helps avoid potential OS-related issues when handling large datasets.

Additionally, dRep incorporate completeness and contamination values to aid in selecting the best representative genome. By default, dRep calculates these metrics using CheckM, but since we have already obtained them using CheckM2 in previous steps, we will provide this information using the `--genomeInfo option`. The genome information file should be a CSV table with three columns: MAG ID, completeness, contamination.

To create the text file listing the paths to each MAG, run the following command inside the `08_drep` directory:
`ls -1 -d /path/to/MAGs_pass/folder/*.fa > MAGs_path_file.txt`

To generate the genome information file, use the `generate_genome_info_file.sh` script located at /hpcfs/home/cursos/bioinf-cabana/cabana_workshop/helper_scripts. Copy the script to your `08_drep` directory, update the `checkm2_and_gunc_out_concat_pass` variable with the correct path, and execute it using `bash generate_genome_info_file.sh`.

### Create and Execute the Bash Scripts to Run dRep

To dereplicate the specified set of MAGs, create a Bash script named `run_drep.sh`, copy the script below, and update the `MAGs_path_file` and `genome_info_file` variables with the correct paths before running. 

This script submits a SLURM job to run dRep using 8 threads. It applies a minimum completeness threshold of 50% and maximum contamination of 5% to filter MAGs. FastANI is used for genome comparisons, with an ANI threshold of 95% for clustering. Additionally, a minimum genome coverage of 30% is required for valid genome alignments.

```
#!/bin/bash

#SBATCH -J drep
#SBATCH -D .
#SBATCH -e drep_%j.err
#SBATCH -o drep_%j.out
#SBATCH --cpus-per-task=8
#SBATCH --time=2:00:00	
#SBATCH --mem=6000

source /hpcfs/home/cursos/bioinf-cabana/conda/bin/activate
conda activate drep

MAGs_path_file="/path/to/MAGs_path_file.txt"
genome_info_file="/path/to/genome_info_file.csv"

dRep dereplicate ./drep_out -g $MAGs_path_file -p 8 -comp 50 -con 5 --S_ani 0.95 --cov_thresh 0.30 --S_algorithm fastANI --genomeInfo $genome_info_file

```

### Output Description

