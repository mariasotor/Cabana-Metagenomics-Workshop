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

To run the dereplicate workflow in dRep, two key input files are needed:

1. **File with paths to MAGs for deplication**

dRep requires a list of MAGs to process. These can be specified using wildcard expansion (e.g., `MAGs_folder/*`), but we will instead provide a text file listing the full paths to each MAG. This method is more robust and helps prevent issues related to handling large datasets.

The MAGs to be processed are those that passed the quality filters. As we will need the MAGs from all samples, your instructor will prepare a folder named `all_MAGs_pass`, containing all MAGs inside each participant’s `05_MAGs_qc/MAGs_pass` folder. This shared directory will be located at `/hpcfs/home/cursos/bioinf-cabana/cabana_workshop`

To generate the text file containing the list of MAG paths, run the following command inside the `08_drep` directory:
`ls -1 -d /hpcfs/home/cursos/bioinf-cabana/cabana_workshop/all_MAGs_pass/*.fa > MAGs_path_file.txt`

2. **File with completeness and contamination information for all MAGs**

dRep uses completeness and contamination metrics to identify the best representative genome in each cluster. Although dRep can compute these using CheckM by default, we will supply our own metrics obtained from CheckM2 in earlier steps. We will provide this information using the `--genomeInfo` option. The genome information file should be a CSV table with three columns: MAG ID, completeness, contamination.

Your instructor will generate this file (`genome_info_file.csv`) using the `gunc_and_checkm2_output_pass.csv` files from each participant. The resulting file will be placed in `/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/all_MAGs_pass`.

### Create and Execute the Bash Scripts to Run dRep

To dereplicate the specified set of MAGs, create a Bash script named `run_drep.sh`, copy the script below, and update the `MAGs_path_file` variable with the correct path before running. 

This script submits a SLURM job to run dRep using 8 threads. It applies a minimum completeness threshold of 50% and maximum contamination of 5% to filter MAGs. FastANI is used for genome comparisons, with an ANI threshold of 95% for clustering. Additionally, a minimum genome coverage of 30% is required for valid genome alignments.

```
#!/bin/bash

#SBATCH -J drep
#SBATCH -D .
#SBATCH -e drep_%j.err
#SBATCH -o drep_%j.out
#SBATCH --cpus-per-task=6
#SBATCH --time=2:00:00	
#SBATCH --mem=6000

source /hpcfs/home/cursos/bioinf-cabana/conda/bin/activate
conda activate drep

MAGs_path_file="/path/to/MAGs_path_file.txt"
genome_info_file="/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/all_MAGs_pass/genome_info_file.csv"

dRep dereplicate ./drep_out -g $MAGs_path_file -p 6 -comp 50 -con 5 --S_ani 0.95 --cov_thresh 0.30 --S_algorithm fastANI --genomeInfo $genome_info_file

```

After creating and saving the script, make it executable and submit to the cluster:

```
chmod +x run_drep.sh
sbatch run_drep.sh
```

### Output Description

Once the dereplication process is complete, you will see the following structure inside the `drep_out` directory:

📂 `drep_out`/ <br>
│── 📂 `data_tables`/ <br>
│── 📂 `dereplicated_genomes`/ <br>
│── 📂 `figures`/ <br>
│── 📂 `log`/


- `data_tables` – Stores summary tables related to genome quality, clustering, and pairwise comparisons.
- `dereplicated_genomes` – Contains the set of representative (dereplicated) genomes in FASTA format.
- `figures` – Includes graphical representations of genome clustering and similarity comparisons.
- `log` – Contains log files that track the execution of dRep, including processing steps, warnings, and errors.

### Ensure Unique Contig Names in Dereplicated MAGs for Reference Database Creation and Bowtie2 Indexing

Before concatenating dereplicated MAGs for Bowtie2 indexing, contig names must be unique to prevent conflicts. For this reason, we will modify the contig names using the format `MAG_ID_c_contig_number`.
Example: `49647_1_2_bin.1_c_000000000001`, `49647_1_2_bin.1_c_000000000002`, `49647_1_2_bin.1_c_000000000003`, etc.

To achieve this, use the `change_contigs_name.sh` script located at `/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/helper_scripts`. Copy the script to your `08_drep` directory, update the `input_dir` variable with the correct path, and execute it using `bash change_contigs_name.sh`.

This will rename all contigs in the MAGs within the `dereplicated_genomes` directory to the specified format.

