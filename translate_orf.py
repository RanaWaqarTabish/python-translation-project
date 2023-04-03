#!/usr/bin/env python3

import argparse
import sys
from find_orf import find_first_orf, parse_sequence_from_path
from translate import translate_sequence

GENETIC_CODE = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*",
    "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W",
}

def main():
    # Set up the command-line interface
    parser = argparse.ArgumentParser(description="Translate the first ORF found in a nucleotide sequence.")
    parser.add_argument("path", help="path to the file containing the nucleotide sequence")
    args = parser.parse_args()

    # Parse the sequence from the file
    sequence = parse_sequence_from_path(args.path)

    # Find the first ORF
    orf = find_first_orf(sequence)

    # Translate the ORF
    amino_acid_sequence = translate_sequence(orf, GENETIC_CODE)

    # Print the amino acid sequence to standard output
    print(amino_acid_sequence)


if __name__ == "__main__":
    main()
