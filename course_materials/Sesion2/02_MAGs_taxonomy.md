# Taxonomic Classification of MAGs

### GTDB-Tk overview
GTDB-Tk enable the taxonomic classifications of bacterial and archaeal genomes based on the Genome Database Taxonomy GTDB. The classification of a query genome is based on a combination of its placement in the GTDB reference tree, its Relative Evolutionary Divergence (RED), and its Average Nucleotide Identity (ANI) with reference genomes. Tree topology usually determines classification, but RED helps resolve ambiguous rank assignments. 

For the taxonomic classification of MAGs, we will use the Classify Workflow in GTDB-Tk and the latest GTDB database release (r220).

### Setting Up Output Directories

Create a new folder named `06_MAGs_taxonomy` Inside this folder, create the following subdirectory:

📂 `06_MAGs_taxonomy`/ <br>
├── 📁 `gtdbtk_out`/

### Create and Execute the Bash Script to Run GTDB-Tk

Since GTDB-Tk requires high RAM usage (~100 GB), **this step will be demonstrative**, and only the instructor will execute it. However, below are the steps to follow for your reference.

Create a Bash script named `run_gtdbtk.sh`, copy the script below, and update the `batchfile` variable with the correct path to your previously created batchfile. This script submits a SLURM job to process each MAG listed in the batch file, generating a taxonomic classification output in the `gtdbtk_out` folder.

```
#!/bin/bash

#SBATCH -J gtdntk_classify
#SBATCH -D .
#SBATCH -e gtdntk_classify_%j.err
#SBATCH -o gtdntk_classify_%j.out
#SBATCH --cpus-per-task=8
#SBATCH --time=4:00:00	
#SBATCH --mem=100000

source /hpcfs/home/cursos/bioinf-cabana/conda/bin/activate
conda activate gtdbtk-2.4.0

batchfile="/path/to/batchfile.txt"

gtdbtk classify_wf --batchfile ${batchfile} -x fa --skip_ani_screen --cpus 8 --out_dir gtdbtk_out
 
```

**Note**: The `--skip_ani_screen` option is used. According to the GTDB-Tk developers, results are nearly identical whether or not this option is enabled, with differences affecting less than 0.1% of genomes. Since ANI screening requires additional computational resources and provides no significant advantage in most cases, it is skipped.

After creating and saving the script, make it executable and submit to the cluster:

```
chmod +x run_gtdbtk.sh
sbatch run_gtdbtk.sh
```

### Output Description

Once your MAGs have finished processing, you will see the following structure inside the `gtdbtk_out` folder:

📂 `gtdbtk_out`/ <br>
│── 📂 `align`/ <br>
│── 📂 `classify`/ <br>
│── 📂 `identify`/  <br>
│── 📄 `gtdbtk.ar53.summary.tsv` <br>
│── 📄 `gtdbtk.bac120.summary.tsv` <br>
│── 📄 `gtdbtk.log` <br>
│── 📄 `gtdbtk.warnings.log` 


- `align` – Cotains multiple sequence alignments of marker genes used for taxonomic classification.
- `classify` – Contains files describing the placement of genomes in the GTDB reference tree and taxonomic assignments.
- `identify` – Contains files from the genome identification step, where GTDB-Tk detects marker genes and assesses genome quality before classification.
- `gtdbtk.ar53.summary.tsv` – File containing taxonomic classifications for archaeal genomes based on the GTDB archaeal (ar53) database.
- `gtdbtk.bac120.summary.tsv` – File containing taxonomic classifications for bacterial genomes based on the GTDB bacterial (bac120) database.
- `gtdbtk.log` and `gtdbtk.warnings.log` – Log files recording the execution details of GTDB-Tk, including runtime information and any issues encountered.

