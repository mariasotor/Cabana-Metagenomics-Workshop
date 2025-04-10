#!/bin/bash

# Directory containing the .fa files
input_dir="/path/to/dereplicated_genomes/folder/"

# Loop through each .fa file in the directory
for file in "$input_dir"/*.fa; do
    filename=$(basename "$file" .fa)  # Extract filename without extension
    temp_file="${file}.tmp"  # Temporary file
    contig_number=1  # Initialize contig counter

    # Process the file and rename contigs
    awk -v prefix="${filename}_c_" '
    BEGIN { contig_number=1; OFS="\n" }
    /^>/ {
        printf ">%s%012d\n", prefix, contig_number++
        next
    }
    { print }
    ' "$file" > "$temp_file"

    # Replace the original file with the modified version
    mv "$temp_file" "$file"
    
 done

   echo "Contigs renamed successfully in all .fa files."
