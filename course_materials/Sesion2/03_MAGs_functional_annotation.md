### Functional Annotation of MAGs

Functional annotation of MAGs is essential to gain insigth into their metabolic potential, ecological roles, and biotechnological or biomedical applications.

### Tools Overview

For this step, we will use two tools to assess the functional potential of the MAGs:

**Bakta** – A fast and comprehensive annotation tool designed for bacterial and archaeal genomes. It predicts genes, assigns functional annotations, and provides insights into metabolic pathways, antimicrobial resistance, and virulence factors.

**AMRFinderPlus** – A specialized tool developed by the NCBI to detect antimicrobial resistance (AMR) genes, virulence factors, and stress response genes, helping to assess potential pathogenicity and resistance profiles of MAGs.

### Setting Up Output Directories

Create a new folder named `07_MAGs_func_annotation` Inside this folder, create the following subdirectories:

📂 `07_MAGs_func_annotation`/ <br>
├── 📁 `amrfinder_out`/ <br>
├── 📁 `bakta_out`/

### Create and Execute the Bash Scripts to Run AMRfinderPlus and Bakta

To run the tools, create two Bash scripts: `run_amrfinder.sh` and `run_bakta.sh`. Copy the scripts below accordingly. Before executing them, update the `batchfile` variable with the correct path to your previously created batchfile. Limit the analysis of Bakta to a maximum of 12 MAGs due to time constraints. You can make a copy of your original batchfile and save a modified version with a subset of your MAGs inside the `07_MAGs_func_annotation` directory. AMRFinderPlus can process all MAGs listed in your original batchfile.

Each script submits a SLURM job to functionally annotate the specified MAGs, storing results in their respective output directories: `amrfinder_out` and `bakta_out`.

**Bakta script**
```
#!/bin/bash

#SBATCH -J bakta
#SBATCH -D .
#SBATCH -e bakta_%j.err
#SBATCH -o bakta_%j.out
#SBATCH --cpus-per-task=8
#SBATCH --time=4:00:00	
#SBATCH --mem=8000

source /hpcfs/home/cursos/bioinf-cabana/conda/bin/activate
conda activate bakta

batchfile="/path/to/batchfile.txt"

while IFS=$'\t' read -r file MAG_ID; do

    bakta --db /hpcfs/home/cursos/bioinf-cabana/Databases/bakta/db-light --output bakta_out/$MAG_ID --threads 8 --prefix $MAG_ID $file

done < $batchfile
```

**AMRFinderPlus script**
```
#!/bin/bash

#SBATCH -J armrfinder
#SBATCH -D .
#SBATCH -e armrfinder_%j.err
#SBATCH -o armrfinder_%j.out
#SBATCH --cpus-per-task=8
#SBATCH --time=1:00:00	
#SBATCH --mem=4000

source /hpcfs/home/cursos/bioinf-cabana/conda/bin/activate
conda activate amrfinder

batchfile="/path/to/batchfile.txt"

 while IFS=$'\t' read -r file MAG_ID; do

    amrfinder -n $file -o amrfinder_out/${MAG_ID}.tsv --threads 8

done < $batchfile
```

After creating and saving the scripts, make them executable and submit them to the cluster:

```
chmod +x run_bakta.sh
chmod +x run_amrfinder.sh

sbatch run_bakta.sh
sbatch run_amrfinder.sh
```

### Output Description

After completing the functional annotation process, the `07_MAGs_func_annotation` directory will have the following structure

📂 07_MAGs_func_annotation/ <br> 
│── 📂 amrfinder_out/  <br>
│   ├── 📄 MAG_ID.tsv  (antimicrobial resistance gene predictions)  <br>
│  <br>
│── 📂 bakta_out/  <br>
│   ├── 📂 MAG_ID/  <br>
│       ├── 📄 MAG_ID.tsv  (functional annotation for predicted genes) <br>
│       ├── Multiple files containing:  <br>
│           • **Gene predictions and functional features identification** (e.g., CDS, rRNA, tRNA annotations)  
│           • **Functional annotations** (e.g., protein functions, pathways)  
│           • **Hypothetical proteins** and their potential functional inference  
│           • **GenBank & EMBL-compatible files** for database submissions  
│           • **Visualization files** (e.g., genome feature maps in PNG, SVG)  
│           • **Log & summary reports** documenting the annotation process  

For a detailed description of Bakta output files, refer to the [Bakta documentation](https://github.com/oschwengers/bakta?tab=readme-ov-file#output).


