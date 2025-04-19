# Quality Assesment of MAGs

### Tools Overview

Evaluating the quality of metagenome-assembled genomes (MAGs) is crucial to ensure they meet quality standards and are free from contamination. This guide covers the use of CheckM2 and GUNC to assess genome completeness, contamination, and potential chimerism.

- **CheckM2**: uses machine learning models instead of static marker gene sets like CheckM. This allows for more flexible and accurate predictions, especially for unusual or underrepresented organisms
- **GUNC**: Detects chimeric MAGs and taxonomic contamination by analyzing phylogenetic inconsistencies. This ensures that MAGs represent a single, coherent genome rather than an assemblies of multiple organisms.

### Setting Up Output Directories

Create a new folder named `05_MAGs_qc`. Inside this folder, create the following subdirectories:

📂 `05_MAGs_qc`/ <br>
├── 📁 `checkm2_out`/ <br>
├── 📁 `gunc_out`/ <br>
├── 📁 `checkm2_and_gunc_out_concat`/ (store the combined results from both CheckM2 and GUNC) <br>
├── 📁 `MAGs_pass`/ (store final, curated MAGs suitable for downstream analysis)

### Create and Execute the Bash Scripts to Run GUNC and CheckM2 

To run the tools, create two Bash scripts: `run_gunc.sh` and `run_checkm2.sh`. Copy the scripts below accordingly. Before executing them, update the `MAGs_folder` variable with the correct path to your refined MAGs directory (`metawrap_50_5_bins`).

These scripts submit SLURM jobs to assess the quality of each MAG, storing the results in the respective output directories: `gunc_out` and `checkm2_out`.

**GUNC script**
```
#!/bin/bash

#SBATCH -J gunc
#SBATCH -D .
#SBATCH -e gunc_%j.err
#SBATCH -o gunc_%j.out
#SBATCH --cpus-per-task=8
#SBATCH --time=2:00:00	
#SBATCH --mem=14000	

source /hpcfs/home/cursos/bioinf-cabana/conda/bin/activate
conda activate gunc

MAGs_folder="path/to/metawrap_50_5_bins/folder"

gunc run -d $MAGs_folder -o gunc_out -e .fa -t 8 --db_file /hpcfs/home/cursos/bioinf-cabana/Databases/gunc/gunc_db_progenomes2.1.dmnd
```

**CheckM2 script**
```
#!/bin/bash

#SBATCH -J checkm2
#SBATCH -D .
#SBATCH -e checkm2_%j.err
#SBATCH -o checkm2_%j.out
#SBATCH --cpus-per-task=8
#SBATCH --time=48:00:00	
#SBATCH --mem=12000	

source /hpcfs/home/cursos/bioinf-cabana/conda/bin/activate
conda activate checkm2

MAGs_folder="path/to/metawrap_50_5_bins/folder"

checkm2 predict --threads 8 --input $MAGs_folder -x .fa --output-directory checkm2_out --remove_intermediates
```

After creating and saving the scripts, make them executable and submit them to the cluster:

```
chmod +x run_gunc.sh
chmod +x run_checkm2.sh

sbatch run_gunc.sh.sh
sbatch run_checkm2.sh
```

### Output Description

Once the processes are complete, the `05_MAGs_qc` directory will contain the following structure:

📂 `05_MAGs_qc`/ <br>
│── 📂 `checkm2_out`/ <br>
│   ├── 📄 `checkm2.log`/ <br>
│   ├── 📄 `quality_report.tsv`/ <br>
│ <br>
│── 📂 `gunc_out`/ <br>
│   ├── 📂 `diamond_output`/ <br>
│   ├── 📂 `gene_calls`/ <br>
│   ├── 📄 `GUNC.progenomes_2.1.maxCSS_level.tsv` <br>


- `checkm2.log` – log file containing details of the CheckM2 run, including parameters used, progress updates, and potential errors.
- `quality_report.tsv` – file summarizing the quality of each MAG, including completeness, contamination, and additional quality metrics.
- `diamond_output` – Contains intermediate results from DIAMOND, the tool GUNC uses for taxonomic classification and contamination detection. This includes sequence alignments and taxonomic assignments.
- `gene_calls` – Stores predicted gene sequences and annotations from MAGs, used by GUNC to evaluate phylogenetic consistency.
- `GUNC.progenomes_2.1.maxCSS_level.tsv` – file summarizing the GUNC analysis, including chimerism scores and taxonomic inconsistencies for each MAG.

### Curated set of MAGs Using GUNC and CheckM2 Data

The set of curated MAGs includes MAGs that passed GUNC’s contamination checks and meet the quality threshold of contamination < 5% and completeness > 50%.

To obtain your set of curated MAGs, use the `concat_and_filter.py` python script located at located at `/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/helper_scripts`. Copy the script file to your `checkm2_and_gunc_out_concat` directory, open it, and update the `checkm2_output_path`,  `gunc_output_path`, `mag_source_dir`, and `destination_dir` variables with the correct path. Then, ensure the `Python_3.13.2` Conda environment is activated and run the script using `python concat_and_filter.py`.

This script generates a `.csv` file named `gunc_and_checkm2_output_pass.csv`, containing CheckM2 and GUNC report data for MAGs that meet the quality criteria. It then searches for these MAGs within the refined bins directory and copies them to the `MAGs_pass` directory for downstream analysis.

### Generate the Batchfile

A batch file is a two-column text file that lists the file paths of MAGs alongside their corresponding identifiers (MAG ID), making it easier to process multiple files in a structured manner. This file will be used as input for the functional and toxonomic classification of MAGs.

To automate the creation of this file, use the `generate_batchfile.sh` script located at `/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/helper_scripts`. Copy the script to your `05_MAGs_qc` directory, update the `MAGs_pass` variable with the correct path, and execute it using `bash generate_batchfile.sh`.

This will generate a `batchfile.txt` file in the current directory, ready for downstream analysis.
