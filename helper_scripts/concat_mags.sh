#!/bin/bash

dereplicated_genomes="/path/to/dereplicated_genomes/folder/"

cat ${dereplicated_genomes}/*.fa > representative_genomes.fasta
