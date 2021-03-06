"""
NAME:               Finding a Shared Motif (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            A common substring of a collection of strings is a substring of 
                    every member of the collection. We say that a common substring is 
                    a longest common substring if there does not exist a longer 
                    common substring. For example, "CG" is a common substring of "ACGTACGT" 
                    and "AACCGTATA", but it is not as long as possible; in this case, 
                    "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

                    Note that the longest common substring is not necessarily unique; 
                    for a simple example, "AA" and "CC" are both longest common substrings 
                    of "AACC" and "CCAA".

DATASET:            A collection of k (k≤100) DNA strings of length at most 1 kbp each 
                    in FASTA format.

OUTPUT:             A longest common substring of the collection. 
                    (If multiple solutions exist, you may return any single solution.)

SAMPLE DATASET:     >Rosalind_1
                    GATTACA
                    >Rosalind_2
                    TAGACCA
                    >Rosalind_3
                    ATACA

SAMPLE OUTPUT:      AC

STATUS:             Submission successful.

NOTE:               Look into compiling Python code for efficiency.
"""

from supplements import SUPP_STree as STree

def _parse_fasta_data(raw_data):
    line_data, elements = list(), raw_data.strip().split(">")
    for el in elements:
        if len(el) == 0:
            continue
        parts = el.split()
        line_data.append("".join(parts[1:]))
    return line_data

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FILEPATHREAD = "./datasets/P14_LCSM-dataset.txt"
    FILEPATHWRITE = "./outputs/P14_LCSM-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Creates generalized Suffix tree (GST) to hold genomic text structure
    generalized_suffix_tree = STree.Suffix_Tree(_parse_fasta_data(data))

    # Creates output file and writes appropriate response to file and notifies user
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(generalized_suffix_tree.determine_LCS()))

    return print("\nThe Shared Motif dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE[2:]))

if __name__ == "__main__":
    main()