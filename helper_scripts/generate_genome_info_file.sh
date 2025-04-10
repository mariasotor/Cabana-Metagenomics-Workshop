#!/bin/bash

checkm2_and_gunc_out_concat_pass="/path/to/gunc_and_checkm2_output_pass.csv"
genome_info_file="genome_info_file.csv"

awk -F',' 'BEGIN {OFS=","} NR==1 {print "genome", tolower($2), tolower($3)} NR>1 {print $1".fa", $2, $3}' $checkm2_and_gunc_out_concat_pass > $genome_info_file
