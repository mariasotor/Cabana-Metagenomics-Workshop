# Quality Control of Metagenomic Reads Using the Read QC Module in metaWRAP

Each participant will analyze one metagenomic sample containing approximately 15 million reads. The sequencing data is provided in FASTQ format (.fastq) and should be stored in a folder named `01_raw_reads`. These files will serve as input for the Read QC module of metaWRAP.

### Read QC Module Overview

The Read QC module of metaWRAP performs three key steps:

- **Adapter and quality trimming** – Uses Trim Galore (default settings) to remove adapters and low-quality bases.
- **Human contamination removal** – Employs BMTagger with the CHM13 human genome assembly.
- **Quality assessment** – Generates a visual quality report with FastQC.

### Preparing the Manifest File

Before running the metaWRAP Read QC module, you need to create a manifest file in the `01_raw_reads` directory to reference the paired sequencing files. This file must be in comma-separated (CSV) format with three columns: ID (Sample identifier), R1 (Path to the forward read file), R2 (Path to the reverse read file). The manifest file ensures a standardized input format and facilitates scalability. 

To contruct such manifest follow the instructions here: [generate_manifest](
https://github.com/mariasotor/Cabana-Metagenomics-Workshop/blob/main/helper_scripts/generate_manifest.md)

### Setting Up Output Directories

Once the manifest file is ready, create a new folder named `02_clean_reads`. Inside this folder, create two  subdirectories:

📂 `02_clean_reads`/ <br>
├── 📁 `metawrap_qc_out`/ <br>
├── 📁 `cleaned_reads`/ 

### Create and Execute the Bash Script to Run the metaWRAP QC Module

To process the sequencing reads using the metaWRAP Read QC module, create a Bash script named `run_metawrap_qc.sh`, copy the script below, and update the `manifest` variable with the correct path before running. This script submits a SLURM job to perform quality control on each sample listed in the manifest file, saving the output in the `metawrap_qc_out` directory.

```
#!/bin/bash

#SBATCH -J metawrap_qc
#SBATCH -D .
#SBATCH -e metawrap_qc_%j.err
#SBATCH -o metawrap_qc_%j.out
#SBATCH -n 8
#SBATCH --time=2:00:00	
#SBATCH --mem=9000	

source /hpcfs/home/cursos/bioinf-cabana/conda/bin/activate
conda activate metawrap-env

manifest="/path/to/your/raw/reads/manifest"

# Loop through each line of the manifest file (skipping the header)
tail -n +2 "$manifest" | while IFS=',' read -r sample R1 R2; do

metawrap read_qc -1 $R1 -2 $R2 -o metawrap_qc_out/$sample -t 8 -x T2T-CHM13v2.0

done
```

After creating and saving the script, make it executable and submit it to the cluster:

```
chmod +x run_metawrap.sh
sbatch run_metawrap.sh
```

### Output Description

Once your samples have finished processing, you will see the following structure inside the `metawrap_qc_out` folder:

📂 `metawrap_qc_out`/ <br>
│── 📂 `sampleID`/ <br>
│   ├── 📂 `post-QC_report`/ <br>
│   ├── 📂 `pre-QC_report`/  <br>
│   ├── 📄 `final_pure_reads_1.fastq` <br>
│   ├── 📄 `final_pure_reads_2.fastq` <br>
│   ├── 📄 `host_reads_1.fastq` <br>
│   ├── 📄 `host_reads_2.fastq`  <br>

- `final_pure_reads_1.fastq` and `final_pure_reads_2.fastq` – These are the final trimmed and decontaminated reads, ready for downstream analysis.
- `host_reads_1.fastq` and `host_reads_2.fastq` – These are reads identified as host contamination and can be safely deleted.
- `pre-QC_report` and `post-QC_report` – These directories contain FastQC html quality reports for the reads before and after quality control.

To facilitate downstream analysis, the final_pure_reads files should be renamed as sampleID_1.fastq and sampleID_2.fastq (e.g., 50027_3_3_1.fastq and 50027_3_3_2.fastq) and moved to the cleaned_reads folder created earlier.

To rename and move the files, use the `rename_and_move_fastq.sh` script located at located at `/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/helper_scripts`. Copy the script file to your `02_clean_reads` directory, open it, and update the `parent_folder` and `destination_folder` variables with the correct path. Then, run the script using `bash rename_and_move_fastq.sh`



