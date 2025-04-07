# Quality assesment of MAGs

### Tools Overview

Evaluating the quality of refined bins is crucial to ensure that the recovered MAGs meet medium to high-quality standards and are free from contamination. We will be using two tools for this assessment:

- **CheckM2**: Estimates genome completeness and contamination by analyzing the presence of single-copy marker genes. 
- **GUNC** (Genome UNClutterer): Detects chimeric MAGs and taxonomic contamination by analyzing phylogenetic inconsistencies. This ensures that MAGs represent single, coherent genomes rather than artificial assemblies of multiple organisms.

### Setting Up Output Directories

Create a new folder named `05_MAGs_qc`. Inside this folder, create the following subdirectories:

📂 `05_MAGs_qc`/ <br>
├── 📁 `checkm2_out`/ <br>
├── 📁 `gunc_out`/ <br>
├── 📁 `checkm2_and_gunc_out_concat`/

### Create and Execute the Bash Script to Run GUNC and CheckM2 

To run the tools, create two Bash scripts: `run_gunc.sh` and `run_checkm2.sh`. Copy the scripts below accordingly. Before executing them, update the `MAGs_folder` variable with the correct path to your refined MAGs directory (`metawrap_50_5_bins`).

These scripts submit SLURM jobs to assess the quality of each MAG, storing the results in the respective output directories: `gunc_out` and `checkm2_out`.

**GUNC script**
```
#!/bin/bash

#SBATCH -J gunc
#SBATCH -D .
#SBATCH -e gunc_%j.err
#SBATCH -o gunc_%j.out
#SBATCH -n 8
#SBATCH --time=2:00:00	
#SBATCH --mem=14000	

source /hpcfs/home/cursos/bioinf-cabana/conda/bin/activate
conda activate gunc

MAGs_folder="path/to/metawrap_50_5_bins/folder"

gunc run -d $MAGs_folder -o gunc_out -e .fasta -t 8 --db_file /hpcfs/home/cursos/bioinf-cabana/Databases/gunc/gunc_db_progenomes2.1.dmnd
```

**CheckM2 script**
```
#!/bin/bash

#SBATCH -J checkm2
#SBATCH -D .
#SBATCH -e checkm2_%j.err
#SBATCH -o checkm2_%j.out
#SBATCH -n 8
#SBATCH --time=48:00:00	
#SBATCH --mem=12000	

source /hpcfs/home/cursos/bioinf-cabana/conda/bin/activate
conda activate checkm2

MAGs_folder="path/to/metawrap_50_5_bins/folder"

checkm2 predict --threads 8 --input $MAGs_folder -x .fasta --output-directory checkm2_out --remove_intermediates
```

After creating and saving the scripts, make them executable and submit them to the cluster:

```
chmod +x run_gunc.sh.sh
chmod +x run_checkm2.sh

sbatch run_gunc.sh.sh
sbatch run_checkm2.sh
```

### Output Description


