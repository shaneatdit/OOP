##########################################################################
#                                                                        #
# DNA-to-amino-acid.py                                                   #
#   by Shane                                                             #
#                                                                        #
# Reads a sequence of DNA from a FASTA file and translates it into       #
# a string of amino acids, via the following steps:                      #
#                                                                        #
# 1. Reads the FASTA file                                                #
# 2. Generates the reverse complement of the DNA string                  #
# 3. Transcribes the DNA and its reverse complement into RNA             #
# 4. Translates from RNA into amino acids, printing all six              #
#    possible reading frames (three reading frames each                  #
#    for both the original DNA string and its reverse complement)        #
#                                                                        #
# (Note: STOP codons are converted to line breaks)                       #
#                                                                        #
##########################################################################

FILE = "FASTA2.txt"


def read_file(file):
    """Returns the contents of file."""
    with open(file) as f:
        return f.read()


def rna_translate(codon):
    """Translates an RNA codon into an amino acid.

    Args:
        A three-letter string of RNA bases.

    Returns:
        A single-character string representing an amino acid
        (or "\n" in the case of a STOP codon).
    """

    table = {"U": {"U": {"U": "F", "C": "F", "A": "L", "G": "L"}, "C": {"U": "S", "C": "S", "A": "S", "G": "S"}, "A": {"U": "Y", "C": "Y", "A": "\n", "G": "\n"}, "G": {"U": "C", "C": "C", "A": "\n", "G": "W"}}, "C": {"U": {"U": "L", "C": "L", "A": "L", "G": "L"}, "C": {"U": "P", "C": "P", "A": "P", "G": "P"}, "A": {"U": "H", "C": "H", "A": "Q", "G": "Q"}, "G": {"U": "R", "C": "R", "A": "R", "G": "R"}}, "A": {"U": {"U": "I", "C": "I", "A": "I", "G": "M"}, "C": {"U": "T", "C": "T", "A": "T", "G": "T"}, "A": {"U": "N", "C": "N", "A": "K", "G": "K"}, "G": {"U": "S", "C": "S", "A": "R", "G": "R"}}, "G": {"U": {"U": "V", "C": "V", "A": "V", "G": "V"}, "C": {"U": "A", "C": "A", "A": "A", "G": "A"}, "A": {"U": "D", "C": "D", "A": "E", "G": "E"}, "G": {"U": "G", "C": "G", "A": "G", "G": "G"}}}
    return table[codon[0]][codon[1]][codon[2]]


def dna_transcription(string):
    """Transcribes a string of DNA into RNA."""
    return string.replace("T", "U")


def rna_to_amino(rna_string):
    """Translates a string of RNA bases into amino acids.

    Args:
        A string of RNA bases.

    Returns:
        A list of three translations
        (starting at the first base, second base,
        and third base, respectively).
    """

    aminos = ["", "", ""]
    for i in range(3):
        for j in range(i, len(rna_string) - 2, 3):
            codon = rna_string[j:j + 3]
            amino_acid = rna_translate(codon)
            aminos[i] += amino_acid
    return aminos


def dna_reverse_complement(string):
    """Returns the reverse complement of a DNA string."""
    complement = ""
    for i in string:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "G":
            complement += "C"
        elif i == "C":
            complement += "G"
    return complement[::-1]


def print_list(amino_list):
    """Prints each list item on a new line."""
    print()
    for i in amino_list:
        print(i)


def main():
    dna_string = read_file(FILE)
    print_list(rna_to_amino(dna_transcription(dna_string)))

    dna_reverse_comp = dna_reverse_complement(dna_string)
    print_list(rna_to_amino(dna_transcription(dna_reverse_comp)))

main()
