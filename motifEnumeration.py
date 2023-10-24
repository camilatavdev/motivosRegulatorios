#Enumeração de motivos regulatórios

def hamming_distance(seq1, seq2):

    """

    Calculates the Hamming distance between two sequences of equal length.

    """

    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))



def find_neighbors(pattern, d):

    """

    Finds all k-mers that differ from 'pattern' by at most 'd' mismatches.

    """

    if d == 0:

        return {pattern}



    if len(pattern) == 1:

        return {'A', 'C', 'G', 'T'}



    neighborhood = set()



    suffix_neighbors = find_neighbors(pattern[1:], d)



    for neighbor in suffix_neighbors:

        if hamming_distance(pattern[1:], neighbor) < d:

            for nucleotide in 'ACGT':

                neighborhood.add(nucleotide + neighbor)

        else:

            neighborhood.add(pattern[0] + neighbor)



    return neighborhood



def is_motif_in_dna(motif, dna, d):

    """

    Checks if a motif appears in all DNA strings with at most 'd' differences.

    """

    k = len(motif)

    for sequence in dna:

        found = False

        for i in range(len(sequence) - k + 1):

            kmer = sequence[i:i+k]

            if hamming_distance(kmer, motif) <= d:

                found = True

                break

        if not found:

            return False

    return True



def motif_enumeration(dna, k, d):

    patterns = set()

    for sequence in dna:

        for i in range(len(sequence) - k + 1):

            kmer = sequence[i:i+k]

            kmer_neighbors = find_neighbors(kmer, d)

            for neighbor in kmer_neighbors:

                if is_motif_in_dna(neighbor, dna, d):

                    patterns.add(neighbor)

    return list(patterns)



# Sample Input

k = 5

d = 1

Dna = ["TGTTGATGATTTAGCTGACCTGTTG ", "ATTGCCGCGTCGGAGTGTGGTGCGC ", "ATTGTTTGGTCTCCCCTGCGTGTAG", "GACCCACCCATGTTGTGACGGACCA", "TCAAATCGGTCACCTTGTCGGATGG", "TGTCGTTTCTCTGCCCTTCAGTCTG"]



result = motif_enumeration(Dna, k, d)

print(" ".join(result))
