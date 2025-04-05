
#!/bin/bash

# Define the parent directory
parent_folder="path/to/refinement/folder"

# Loop through each sample ID folder
for sample_folder in "$parent_folder"/*/; do
    # Extract the sample ID (folder name)
    sample_id=$(basename "$sample_folder")

    # Define the path to the metawrap_50_5_bins folder
    bins_folder="$sample_folder/metawrap_50_5_bins"

    # Check if the metawrap_50_5_bins folder exists
    if [[ -d "$bins_folder" ]]; then
        # Loop through .fa files in the metawrap_50_5_bins folder
        for file in "$bins_folder"/*.fa; do
            # Extract the bin identifier (bin.1, bin.2, etc.)
            bin_id=$(basename "$file" | sed -E 's/(bin\.[0-9]+)\..*\.fa/\1/')

            # Define the new filename
            new_name="${sample_id}_${bin_id}.fa"

            # Rename the file
            mv "$file" "$bins_folder/$new_name"
        done
    fi
done

echo "Files renamed successfully!"
