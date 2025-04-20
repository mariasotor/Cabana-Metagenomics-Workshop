#!/bin/bash

# Output file
genome_info_file="genome_info_file.csv"
tmp_file=$(mktemp)

# Initialize the temp file (no header yet)
> "$tmp_file"

# Loop through each matching CSV file in user directories
for file in /hpcfs/home/cursos/bioinf-cabana/cabana_workshop/users/*/05_MAGs_qc/checkm2_and_gunc_out_concat/gunc_and_checkm2_output_pass.csv; do
    if [[ -f "$file" ]]; then
        # Process each file, skip the header line
        awk -F',' 'NR > 1 {print $1".fa," tolower($2) "," tolower($3)}' "$file" >> "$tmp_file"
    fi
done

# Write header to final output file
echo "genome,completeness,contamination" > "$genome_info_file"

# Sort and remove duplicates, then append to output
sort -u "$tmp_file" >> "$genome_info_file"

# Clean up
rm "$tmp_file"
