# Generating the Manifest File

A Bash script named `generate_manifest.sh` is available to automate the creation of this file. You can find it at: `/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/helper_scripts`. 
You can either copy the script to your `01_raw_reads` directory or run it directly by specifying its full path.

This script requires a text file (.txt) as input, containing the file paths of all sequencing reads to be processed. To generate this file, use the following command:

`ls -1 -d /path/to/your/raw/reads/*.fastq > file_path.txt`

This will create a file named `file_path.txt` in the current directory.

Once the input file is ready, generate the manifest file by running:

`bash generate_manifest.sh file_path.txt`

This will produce a file named `manifest.csv` in the current directory.
