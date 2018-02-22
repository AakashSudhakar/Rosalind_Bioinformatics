"""
NAME:               Transcribing DNA into RNA (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
                    
                    Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed 
                    by replacing all occurrences of 'T' in t with 'U' in u.

DATASET:            A DNA string t having length at most 1000 nt.
OUTPUT:             The transcribed RNA string of t.

SAMPLE DATASET:     GATGGAACTTGACTACGTAAATT
SAMPLE OUTPUT:      GAUGGAACUUGACUACGUAAAUU

STATUS:             Submitted.
"""


def main():
    """ Returns new string with Ts converted to Us """
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P2-TDiR_rosalind_rna.txt"
    FILEPATHWRITE = "./outputs/P2-TDiR_output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        nucleotides = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write("\n{}\n".format("".join([[nucleotide, "U"][nucleotide == "T"] for nucleotide in nucleotides])))

    return print("\nThe RNA dataset has been processed and the appropriate output has been saved to {}/{}.\n".format(FILEPATHWRITE.split("/")[1], FILEPATHWRITE.split("/")[2]))


if __name__ == "__main__":
    main()