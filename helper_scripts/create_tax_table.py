#!/home/bioinf-cabana/conda/envs/python_3.13.2/bin/python

import pandas as pd

# File paths
taxonomy = "/path/to/gtdbtk.bac120.summary.tsv"
genome_list = "/path/to/representatives_genomes.txt" # list of representative genomes without .fa extension (one per line) 
output_csv_path = "/hpcfs/home/cursos/bioinf-cabana/cabana_workshop/final_tables/all_MAGs_taxonomy.csv"

# Step 1: Read the genome list
with open(genome_list, 'r') as file:
    genome_names = [line.strip() for line in file]  

# Step 2: Read taxonomy data and clean user_genome column
taxonomy_data = pd.read_csv(taxonomy, sep='\t')

# Step 3: Filter relevant genomes
filtered_data = taxonomy_data[taxonomy_data['user_genome'].isin(genome_names)].copy()

# Step 4: Parse classification column
taxonomy_columns = ['Domain', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
for level in taxonomy_columns:
    prefix = level[0].lower() + '__'  # Create 'd__', 'p__', etc.
    filtered_data[level] = filtered_data['classification'].str.extract(f'({prefix}[^;]*)')[0].str.replace(prefix, '', regex=False)

# Step 5: Keep only relevant columns and fill NaN values with an empty string
filtered_data = filtered_data[['user_genome'] + taxonomy_columns].fillna('')

# Step 6: Save the output
filtered_data.to_csv(output_csv_path, index=False)

print(f"Taxonomy data has been saved to {output_csv_path}.")
