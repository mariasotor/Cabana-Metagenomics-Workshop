#!/usr/bin/env python

import os
import gzip
import argparse

def gen_stb(fastas, output):
    stb = []
    for fasta in fastas:
        bin_name = os.path.basename(fasta)
        open_func = gzip.open if fasta.endswith('.gz') else open
        mode = 'rt'
        
        with open_func(fasta, mode) as handle:
            for line in handle:
                if line.startswith('>'):
                    scaffold = line[1:].strip().split(' ')[0]
                    stb.append(f"{bin_name}\t{scaffold}\n")
    
    with open(output, 'w') as out_file:
        out_file.writelines(stb)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a reversed scaffold-to-bin (.stb) file.')
    parser.add_argument('-f', '--fasta', nargs='+', required=True, help='List of genome FASTA files')
    parser.add_argument('-o', '--output', required=True, help='Output .stb file')
    args = parser.parse_args()
    
    gen_stb(args.fasta, args.output)

