#!/home/bioinf-cabana/conda/envs/python_3.13.2/bin/python

import os
import glob
import pandas as pd

# Use glob to collect all .tsv files from multiple user directories
amr_files = glob.glob("/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/users/*/07_MAGs_func_annotation/amrfinder_out/*.tsv")

# List to hold individual DataFrames
dataframes = []

# Loop through each file
for file_path in amr_files:
    filename = os.path.basename(file_path)
    if filename.endswith('.tsv'):
        # Read the file into a DataFrame
        df = pd.read_csv(file_path, sep='\t')  

        # Add a new column 'user_genome' with the filename (without the extension)
        mag_id = filename.split('.tsv')[0]
        df['user_genome'] = mag_id

        # Add the 'sampling_location' column based on the condition
        df['sampling_location'] = df['user_genome'].apply(lambda x: 'Tumaco' if x.startswith('49647_1') else 'Posadas')

        # Reorder columns to place 'user_genome' at the beginning
        cols = ['user_genome', 'sampling_location'] + [col for col in df.columns if col not in ['user_genome', 'sampling_location']]
        df = df[cols]

        # Append the modified DataFrame to the list
        dataframes.append(df)

# Concatenate all DataFrames into one
consolidated_df = pd.concat(dataframes, ignore_index=True)

# Drop duplicate user_genome entries
consolidated_df = consolidated_df.drop_duplicates(subset='user_genome', keep='first')


# Load the taxonomy information table
tax_table = '/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/final_tables/all_MAGs_taxonomy.csv' 
tax_df = pd.read_csv(tax_table)

# Merge the two DataFrames on the 'user_genome' column
merged_df = pd.merge(consolidated_df, tax_df, on='user_genome', how='inner')

# Save the merged DataFrame to a new file
output_path = '/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/final_tables/all_AMR_genes.csv'
merged_df.to_csv(output_path, index=False)

print(f"Merged table saved to {output_path}")
