#!/bin/bash

# Define file paths
MAGs_pass="/path/to/MAGs_pass/folder/"
MAGs_path_and_name="batchfile.txt"

# Create or clear the output file
> "$MAGs_path_and_name"

# Loop through the .fa files in MAGs_pass
for file in "$MAGs_pass"/*.fa; do
    filename=$(basename "$file")  # Get the filename
    mag_id="${filename%.fa}"      # Remove the .fa extension to get the MAG ID

    # Append the file path and MAG ID to the batch file
    echo -e "$file\t$mag_id" >> "$MAGs_path_and_name"
done

echo "Batchfile generated successfully."
