# Compute the Hamming Distance Between Two Strings
## Problem
We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi. For example, CGAAT and CGGAC have two mismatches. The number of mismatches between strings p and q is called the Hamming distance between these strings and is denoted HammingDistance(p, q).

Hamming Distance Problem
Compute the Hamming distance between two DNA strings.

Given: Two DNA strings.

Return: An integer value representing the Hamming distance.


```python
def HammingDistance(p, q):
    distance = 0
    for i, j in zip(p, q):
        if i!=j: distance +=1
    return distance
        
p,q = input().split()
print(HammingDistance(p,q))
```

    GCGCTTGGGCGTTGGTAAATTGCCATCTTCACCAGCATTTAAGATTCCCGAGAGAAGTATAGACGCCAAATATATCCCGACAGATCAGCAAGACGAGCACGACCCGCCCCCGGCCGATCCGCGGGTGATGCCGCCATCACGTGGGTCCCCAGAGTAGTGCACCTGCCTGCGCCTAGCCTTAACCGGCAAGACTGGCCCTCGACTGGGTTGAAATACCAGGTCCTGGATACTGTACGAGATGCGGTCCGCGGGACTTCAAGATTGAGATACCGGGCCAGATGATGCATAACGCTTTGGGGGACTTGAGGACTCGGAACTCTACATCTGAACTTACAGTTGCGGAGCATCAACCACACGTTCCGTAGTATTGCTAAAATGCGACCACGTTTCCATTTGCGATGAAACCTACCGTGGTTGCTTCAGAGGGTCGGTAGTCGGGAATAACTTTGATATCCAACCCTTCAACGAACGTTCTCGGTGGAGTTCTATCTCGGATCGACGTTAAACATGTGCTTTGACGGTGTTCCTAGCTAAGACCTTAAAGAAGTCTGAGAGCTAGACCATCACTATGTCAAGCCGGTGGTTACAGACGCCCTTCAGGTCAGGCTGATTATAGTGGTAATCACGAAAGATAAAGGGCTTGAGAGCCGTCCTCGGACCCCTTATATCATTGGGCGCTATGCGAGGCCATGCCCGACAACTTGTTACGTGATCTACTTTATCGCAATCAACAAAGTCCGAAACGCAAGCAGATAGGTATACCTGCGAACAGCGAACGTCTCGGTTCTTGTCATTAAGTTGGCGTTTTACGGAGCCATTACGGATCGTTGGATTGTGTAATCGGTGCGCACTGCGAACCCTGTTCAACGACATATCTTAGCACCGTGTTCATGGGTAGGTACCACGGCGTAGTCCAAGATTTTGACAGCCGCGTGTGTCCGCTTCATTCGTACTGGTTTGTAGCGCCCCGTTGGAATCTATAGGAACCCTGACGTGAATCAATGCGCGTCCAGCGCATGTGGCCGGTCGTTCACTATCTCGCGGCGTGTGGAAGACCCTCGTTCCCCCCGACCACCCTAAGCCGCATCTATCGATCTTAATACGCTAGGGGCGGCGTACACGGAAAGAT TTAGGCCCTGCGCCCGATCAACCTATATACCCTAAAGTCAAGTAATTCCTCTGGACCTCTTGCACGTTTGAAAAGTGATAGCGCCGGCTACTTAAAGGACATATAAAGAAGTCTCGTTAGCCCACTGTAATCAAAGAGTGAACATCCTCTATTGCAGATCGGGCCGGAAACCAAGCCTCAGCCCCTTACGAAGACATCTCGCTTAATAACCTCCATTGTTCGTTTTCTGCGATGACTACGACTATTGCATTTTCACCTAGCAGGCCGACTTCCGCGTGTGTTGCTAGACGGCGTTGCAGTAAGTAATGAGGCGTTCTTGTAATACCCTCGTGTCGACCCGGTATTCGGGTGCAATCACAAAGAGACGGGATGTCGGGTACTGGAGGATTACGTCAAAAGTGGGCGTGCAGCCCAATCAAGGCCTCGTACGAAGGCCAGGATAGGCACTGGTACATATTGACACAAACGTTACTAATGCGAGGGCGAATATTGGCCCCAATAACGTGATGCGATTTGACGGGGTCACACGCGCATTGAGTGGTCGCGGCGACCTGTCTGTATCAGGATAAGATGACGAAGTGAATAAGATATATCTATCTTGGCAGCGAGCCGAGCAGCATTAGTAAGTCCGGATACAAAATGAGTTTGCTCGGATTTGAGTCAGCGTGTCTCGCCCATGGACGACGGACTCCTCTGGCCACCACATCGCGGATACGGCATATACGAAAACAATAAATCCGGTTAACTAGCCCCTTCATTTGTGTCACCCTGGTCGGCGGTGAAGCAAAGCTGACGTCTTCTGGCTTTGCGGGTACTAACTGGATCTATGCGTGCGTCTTACCCCCGTGAGAACGAATGTACACAGGAGGAGTGCATCGCTGGGTCCACATGGCTACCAAGCTCCCTGGCGGCATTCAATTGAACATAATCGGTTTAACGGACAGCAGAGAAGCTCTGCCTTTGACATACCATACTATATACGAATATTTTAAAGGAACCTGATAAGAATGTGGTTAGCTGTTGTCGTTCGAAGGTTTGAGTGTATTTGAGGACTCTTGAACGAAAAGCTACCTACAACATAGCAGAATCCTGATTGCGTGACTTCTGAAACCTAATGAAGTGGATGCCA
    835



```python

```
