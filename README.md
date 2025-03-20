# CABANAnet workshop: Metagenomics analysis of the human gastrointestinal microbiome

This workshop focuses on the analysis of human gut metagenomic data. The workflow is based on the reconstruction of metagenome-assembled genomes (MAGs) from metagenomic samples.

Throughout the workshop, participants will gain knowledge in the analysis and interpretation of metagenomic data. They will also gain hands-on experience using an High-performance computing (HPC) cluster to run various bioinformatics tools for quality control, assembly, and binning of short metagenomic reads, as well as for taxonomic identification, functional annotation, and abundance estimation of bacterial genomes.

The metagenome analysis will follow the steps outlined in the diagram below.

![image](https://github.com/user-attachments/assets/7b167054-300f-4eaa-85b0-a6a6ecaa6767)

---
For detailed information about each bioinformatics tool used in the workshop, please refer to its corresponding documentation:

#### Reads quality control, assembly and binning

  - **metaWRAP**
    - https://github.com/bxlab/metaWRAP
    - https://github.com/bxlab/metaWRAP/blob/master/Module_descriptions.md
 
#### MAGs quality control

  - **MDMcleaner**
    - https://github.com/KIT-IBG-5/mdmcleaner

 - **GUNC**
     - https://grp-bork.embl-community.io/gunc/
  
 - **CheckM 2**
    - https://github.com/chklovski/CheckM2

#### MAGs dereplication

  - **dRep**
      - https://drep.readthedocs.io/en/latest/module_descriptions.html
    
#### MAGs abundance estimation

  - **Bowtie 2**
      - https://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#building-from-source

  - **Samtools**
     - https://www.htslib.org/doc/samtools.html
  
  - **msamtools**
      - https://github.com/arumugamlab/msamtools

#### MAGs taxonomy classificatioon

  - **GTDBtk**
      - https://ecogenomics.github.io/GTDBTk/
      - https://ecogenomics.github.io/GTDBTk/commands/classify_wf.html

#### MAGs functional annotation

  - **Bakta**
      - https://github.com/oschwengers/bakta

  - **AMRFinderPlus**
      - https://github.com/ncbi/amr/wiki
      - https://github.com/ncbi/amr/wiki/Running-AMRFinderPlus#usage

> The workshop material has been designed and organized by Maria Alejandra Soto and Dorian Rojas-Villalta, secondees of the CABANAnet project "Exploring the Human Gut Microbiome Diversity in Latin America: Focus on Population at Nutritional Risk".
