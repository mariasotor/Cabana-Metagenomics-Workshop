#!/home/bioinf-cabana/conda/envs/python_3.13.2/bin/python

import pandas as pd
import glob

# Define the directory containing the profile files
profile_files = glob.glob("/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/users/*/09_abundance_estimation/msamtools_out/*.profile.txt")

# Dictionary to store abundance data for each sample
abundance_dict = {}

for file in profile_files:
    sample_id = file.split("/")[-1].replace(".profile.txt", "")  # Extract sample ID from filename
    
    # Read the file and skip the first 11 lines
    df = pd.read_csv(file, sep="\t", skiprows=11, header=None, names=["genome_id", "abundance"])
    
    # Remove '.fa' from genome_id, if it exists
    df["genome_id"] = df["genome_id"].apply(lambda x: x.replace(".fa", "") if x.endswith(".fa") else x)
    
    # Drop duplicate genome IDs, keeping the first occurrence
    df = df.drop_duplicates(subset="genome_id", keep="first")
    
    # Store abundance values in a dictionary with genome IDs as keys
    abundance_dict[sample_id] = df.set_index("genome_id")["abundance"]

# Create a consolidated DataFrame (samples as rows, genome_ids as columns)
abundance_df = pd.DataFrame(abundance_dict).T.fillna(0)

# Reset index to turn sample IDs into a column
abundance_df.reset_index(inplace=True)

# Rename 'index' column to 'Sample'
abundance_df.rename(columns={"index": "Sample"}, inplace=True)

# Save the final DataFrame to CSV
abundance_df.to_csv("merged_abundance.csv", index=False)
