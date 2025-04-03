#!/bin/bash

# Define paths
parent_folder="path/to/metawrap_qc_out"
destination_folder="path/to/cleaned_reads"

# Loop through subfolders in the parent folder
for subdir in "$parent_folder"/*/; do
    # Get the folder name (basename)
    folder_name=$(basename "$subdir")

    # Rename and move the files
    if [[ -f "${subdir}final_pure_reads_1.fastq" ]]; then
        mv "${subdir}final_pure_reads_1.fastq" "${destination_folder}/${folder_name}_1.fastq"
    fi
    if [[ -f "${subdir}final_pure_reads_2.fastq" ]]; then
        mv "${subdir}final_pure_reads_2.fastq" "${destination_folder}/${folder_name}_2.fastq"
    fi
done

echo "Files renamed and moved successfully!"

