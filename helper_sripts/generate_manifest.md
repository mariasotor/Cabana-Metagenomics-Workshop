# Generate manifest

A Bash script named *generate_manifest.sh* is available to automate the creation of this file. It is located at: `/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/helper_scripts`. 
You can either copy the script to your own folder or run it directly by specifying its full path.

The script requires a text file (.txt) containing the file paths of all the sequencing reads to be processed. You can generate this file using the following command:

`ls -1 -d /path/to/your/raw/reads/*.fastq > file_path.txt`

This will generate a file named *file_path.txt* in the current directory.

Once the input file is ready, you can create the manifest file by running:

`bash generate_manifest.sh file_path.txt`

This will generate a file named *manifest.csv* in the current directory.
