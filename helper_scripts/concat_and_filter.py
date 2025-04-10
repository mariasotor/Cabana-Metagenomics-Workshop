#!/home/bioinf-cabana/conda/envs/python_3.13.2/bin/python

import pandas as pd
import os
import shutil

# Define paths
checkm2_output_path = "/path/to/checkm2/quality_report.tsv"
gunc_output_path = "/path/to/gunc/GUNC.progenomes_2.1.maxCSS_level.tsv"
mag_source_dir = "/path/to/refinement/folder/"
destination_dir = "/path/to/MAGs_pass/folder/"
filtered_output_path = "gunc_and_checkm2_output_pass.csv"

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Load CheckM2 and GUNC output files
checkm2_output = pd.read_csv(checkm2_output_path, sep='\t')
checkm2_output = checkm2_output.rename(columns={'Name': 'genome'})

gunc_output = pd.read_csv(gunc_output_path, sep='\t')

# Merge CheckM2 and GUNC data
merged_data = checkm2_output.merge(gunc_output[['genome', 'pass.GUNC']], on='genome', how='left')

# Apply filtering criteria
filtered_mags = merged_data[
    (merged_data['pass.GUNC'] == True) &
    (merged_data['Completeness'] >= 50) &
    (merged_data['Contamination'] <= 5)
]

# Save the filtered results
filtered_mags.to_csv(filtered_output_path, index=False)

# Move MAGs that passed QC
for genome_id in filtered_mags['genome']:
    found = False
    for sample_folder in os.listdir(mag_source_dir):
        sample_path = os.path.join(mag_source_dir, sample_folder, "metawrap_50_5_bins")
        if os.path.isdir(sample_path):
            for mag_file in os.listdir(sample_path):
                if mag_file == f"{genome_id}.fa":  # Check for exact match
                    source_path = os.path.join(sample_path, mag_file)
                    destination_path = os.path.join(destination_dir, mag_file)
                    shutil.copy(source_path, destination_path)
                    found = True
                    break
        if found:
            break

print("MAGs that passed QC have been copied successfully.")
