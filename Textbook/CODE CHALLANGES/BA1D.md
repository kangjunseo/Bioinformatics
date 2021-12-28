# Find All Occurrences of a Pattern in a String
## Problem
In this problem, we ask a simple question: how many times can one string occur as a substring of another? Recall from “Find the Most Frequent Words in a String” that different occurrences of a substring can overlap with each other. For example, ATA occurs three times in CGATATATCCATAG.

Pattern Matching Problem
Find all occurrences of a pattern in a string.

Given: Strings Pattern and Genome.

Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.


```python
Pattern, Genome = input().split()
indices = []
for i in range(len(Genome)-len(Pattern)+1):
    if Genome[i:i+len(Pattern)]==Pattern: indices.append(i)
        
for i in indices: print(i, end=' ')
```

    GCCGTACGC GCCGTACGCCGTACTGGCTGTTGCCGTACGGTGGCAAGGCCGTACAAGAGCCGTACGCCGTACGCCACCCAGGGCCGTACAGCCTCTGGGCCGTACGTGCCGTACTGAGCCGTACGCCGTACGCCGTACGTATTAGCCGTACGGACTGCCGTACTATGCCGTACGCCGTACAGAGCGCCGTACGCCGTACGACATCATGCCGTACGCCGTACGCCGTACGAGTGGCCGTACGCCGTACGCGCCGTACGCCGTACGCCGTACAGCCGTACGCCGTACCTGCCGTACAAGTAGCCGTACGGCCGTACACAGCCGTACTGCCGTACTGCCGTACGCCGTACCCCGCGCCGTACTGAGCCGTACCGATGTGCTATCGCCGTACTGCCGTACAGCCGTACTATGCCGTACGTAAGCCGTACTGCCGTACTTTTAAAGGCCGTACTCGCCGTACGCCGTACCGCCGTACGGCCGTACCTAAGCCGTACCCCGCTTATCGGCCGTACTAGCCGTACGAGGCCGTACGGCCGTACGCCGTACCCGAGAAGTGCCGTACCGCCGTACTATAGAAATAATATCCCGGTGGCCGTACGGGTGGGCCGTACTGAGGAGCCGTACGCCGTACGCCGTACCGCCGTACGACGCGCCCAGTGCGCCGTACCGCGGCCGTACCCGCCGTACAGTACAGGCCGTACCGCCGTACGCCGTACCGCATCTCCGCCGTACAGTAGCCGTACGACGGCCGTACGGCCGTACCGCCGTACAGCCATCGCCGTACTGGCCGTACGGCGGCCGTACGCCGTACTGCCGTACGGCCGTACGCCGTACGTTGCCGTACTTTAGCCGTACGGCCGTACAAAGCCGTACCGCCGTACGTAGAGTCAGCGCCGTACAGTTTGATTCGCCGTACGGAACGCCGTACTAGCCGTACAGCCGTACGAGAATGCCGTACTTCACTTGGTTGGCCGTACGCATGGCCGTGCCGTACGAAGCCGTACAGCCGTACTCTAGGGCCGTACGTCGGCCGTACTAGCCGTACAGGCCGTACTTGCCGTACGCCGTACGTGCCGTACCCGTAGCCGTACCTGCCGTACGCCGTACGCCGTACAGCCGTACGCCGTACTAGCCGTACCAGCCGTACGGCCGTACGCCGTACTCCGCCGTACCAAGCCGTACTCCGCCGTACTAGCCGTACGCCGTACGATCAGCCGTACCAGGGCCGTACGCAATGCCGTACGCCGTACGATGGGCCGTACGCCGCCGTACTCGCCGTACGCCGTACTGGCCGTACGCCGTACTGCCGTACCGCCGTACTGGTGATGCCGTACCACCGGCCGTACGCCGTACGCCCAGCCGTACCGCCGTACAGGTAGCCGTACGCCGTACCTGCCGTACTAGCCGTACGAGCCGTACACCCGCCGTACCAACGGCCGTACTCGCGGCCGTACCGATAACCATGGCCGTACGCCGTACAGCCGTACGATAGCCGTACGCCGTACTATGCCGTACGCCGTACCCGGCCGTACAGCCGTACGGCCGTACGCCGTACGGCGGCAATGCCGTACGCTGATCCCCGCCGTACATAAGCCGTACAGCCGTACCAAAGAGCCGTACGTTAAGCCGTACGCCGTACGCAGCCGTACGCGCCGTACACGTGCCGTACGTCGCCGTACCGCCGTACCGGCCGTACCGAAGCCGTACATTCGGCCGTACAAGCCGTACCTGCCGTACTTATTCAGCCGTACAGCCGTACCGCCGTACCTGTAGGTTTGCCGTACCAGGCCGTACTCGCAACGCCGTACCAAGCCGTACGCCGTACGCCGTACAGGAGCGCCGTACCGGGCCTGCCGTACGCCGTACGCCGTACGCCGTACCGCGACTGCCGTACCAGTAAGCCGTACCCGCAGCCGTACTCAGACACGCCGTACTCGCCGTACTGCCGTACTCGTTGCCGTACCTGCCGTACGCCGTACGATTAGCCGTACGCCGTACGCCGTACGCATTGCCGTACGGATGGCCGTACGTTAGTAAGCCGTACCGTTGGTCGCCGTACGTGCCGTACAGCCGTACAAGGCCGTACGACACGCCGTACGCCGTACTGATGAACAGCCGTACTTTGGCCGTACAAGCCGTACGGCCGTACGGCCGTACTCGCTGTATCTGCCGTACCGCCGTACAGGCCGTACTGCCGTACGGCCGTACGCAGGGGCCGTACCTCCCGCCGTACGTGCCGTACACGCCGTACCAAGCCGTACGGGCCGTACTCGCCGTACCGAGCCGTACGCGGCCGTACTCGAGGGCCGTACGAACGCCGTACTCGCCGTACTCAGGCCGTACGCGGGCCGTACAGCCGTACGCCGTACTTCAATTCACCAAGAACGGCCGTACGCCGTACAGCCGTACTTTAACGGAGTAGCGCCGTACGCCGTACGCCGTACGCCGTACAGCCGTACCGTACGCCGTACGCCGTACCGCCGTACTAGCCGTACCGCCGTACGCCGTACGCCGTACGCCGTACGGCCGTACGGCCGTACCTGCCGTACGCCGTACCTCTCAGCCGTACCTGCCGTACTTCGCCGTACTCGCCGTACATCTCCGAGCCGTACGCCGTACTTGGCGCCGTACGCCGTACTGGGGCCGTACGCCGTACGCCGTACCGCCGTACCTTTCGCCGTACGCCGTACCGGTGAGCCGTACAGAGGTCCTAGCCGTACATGTGCCGTACGCCGTACTTGCCGTACCTGCCGTACAGCGCCGTACCATGCCGTACCTTCGCCGTACTTAGCGGCCGTACGCCGTACCTGCCGTACAATGGATTGGGTGCATCAGCCGTACGCCGTACTCGCCGTACTGAGCCGTACCCCGCCGTACGCCGTACTAGAGCCGTACTGCCGTACAGCCGTACGGCCGTACTCCGCCGTACGTTGCACCGCCGTACGCCGTACTGCCGTACAGCCGTACTGGCCGTACGCCGTACACAATCACTAACTGGTGATACGCCGTACATTCGGGAATGCCGTACCCTCGCCGTACGTATGCCGTACCCGAGCCGTACGCCGTACAGCCGTACGTATCGGCCGTACGCCGTACGGGGACATCACCGGTGGCCGTACGGCCGTACTGCCGTACCGCCGTACCACGCAAGGCCGTACGCCGTACGCCGTACGCCGTACACGGGCCGTACGAGCCGTACGCCGTACGGCCGTACAGCCGTACGGCCGTACGCCGTACTTGCCGTACGGGATTGCCGTACAAGCCGTACCGATGCCGTACGCCGTACGCCGTACCCCCAGAGCCGTACGCGCCGTACTGCCGTACGCCGTACTGTAAAGGACGGTCTCGCCGTACCGTAGCCGTACAACAGTGCCGTACGGCCGTACTCGCCGTACGCCGTACTCCTGCCGTACGCCGTACGCGGCCGTACAGCCGTACACATGGCCGTACTAGTAAGCCGTACCTCGCCGTACAGCCGTACAGCCGTACGCCGTACGGCGCCGTACTGGCCGTACAACAGCCGTACGGCCGTACCTGTAGCCGTACGCCGTACGCCGTACGCCGTACTCAAGCCGTACCCGGCCGTACACGGCCGTACGTGCCGTACGCCGTACGCCGTACGCCGTACGAGCCGTACGCCGTACTGCCGTACGCCGTACGCGACCGCCGTACAACAGCACCGGCTGCCGTACGCCGTACTGTAGCCGTACGCACCAAGCCGTACGGGACCGCCGTACAGCCGTACACAGTCGCCGTACTAGCCGTACACGCCGTACGGCCGTACGTCAGCCGTACCGCCGTACGGCCGTACTCACTAGCCGTACTGCGTTCTGATCAGGCCGTACCGAAGGGCCGTACGTTGCCGTACGCCGTACGCCGTACGCCGTACGTTCGCCGTACCGCCGTACGTGCCGTACGCCGTACAGCCGTACTGCCGTACACGCCGTACGCCGTACTGCCGTACCGGGGCCGTACGCCGTACGCCGTACAAAGAGGTGCCGTACGCCGTACGTACCAGGCCGTACGCCGTACCTCGGGGCCGTACGCCGTACTACTATGGCCGTACGCCGTACGGCCGTACCGGGTGGCCGTACGCCGTACGCCGTACGCCGTACGCCGTACGCCGTACCACGCCGTACGCCGTACATGGGCCGTACCGCCGTACGCCGTACCTGCCGTACTAAATCCAGCAGCCGTACAGCCGTACCTTATCAGCCGTACAGTCCTGCATCACCTGCCGTACAGCCGTACTACATGCCGTACAGCCGTACTCGCCGTACCGGCCGTACGCGCCGTACCGGCCGTACTGCCGTACAGCCGTACGCCGTACCGCCGTACGGCCGTACCGCCGTACTCCCAATAGCCGTACCTATTAGAAGCCGTACAGCCGTACGCCGTACTTGCCGTACTGTTGAGCTGCCGTACAAGCCGTACACCACACCTTTGGCCGTACAAGCCGTACCTCGCCGTACGCCGTACATATCGCCGTACTATCGCCGTACGGGAGCCGTACGGTTGAGCCGTACGTGCCGTACATCGCCGTACTAGCCGTACGCCGTACGCCGTACAGCTAATCTCGCCGTACTAAGCCGTACCCGGGCCGTACGCCGTACGCCGTACGCCGTACGCCGTACTAGCCGTACGGTCGAGTGCGCGCCGTACCCAATGGTGCCGTACTAAATGGCCGTACGAAGCCGTACGCCGTACGCCGTACAAGGAGCCGTACGCCGTACTTGCTGCCGTACGACCGGGCCGTACTGGCCGTACGCCGTACCATGCCGTACGTGCCGTACTGCCGTACGGGAGAGAGCCGTACACTATGCCGTACTGCCGTACTATTGCCGTACTAGTATCGCCGTACCGGCCGTACTGTTTAGCCGTACCGCGGCCGTACATGCCGTACGCCGTACGCCGTACCGCCGTACTTGCCGTACGCCGTACTGCCGTACGCAGCCGTACTATAGCCGTACGCCGTACCGGCCGTACGCCGTACCCGGCCGTACGCCGTACCTGCCGTACTTGAGCCGTACAGTAGCCGTACGCCGCCGTACCAGGCCGTACCAGCCGTACCGTGCCGTACACTTGCCGTACGAGGCCGTACTGCCGTACAGCCGTACCGCCGTACGCCGTACCTATTTGCCGTACTGGCCGTACGCCGTACACGCCGTACGGAGGCCGTACGTGCCGTACAGCCGTACCAGCCGTACTGCCGTACTGATCTGCCGTACTCGGCCGTACATGCTGCCGTACTACATAGAAGCCGTACGGCGCCGTACGCCGTACAAACGGTGCCGTACGCCGTACGCCGTACGCCGTACCAGCCGTACGCGCCGTACCGCCGTACTGCTCGACGCCGTACGGCCGTACGCCGTACGGCCGTACACGCCGTACCTTGGCCGTACGGGCCGTACCGGCCGTACTATGCCGTACAAGCCGTACGCCGTACCGGCCGTACGCACACTTTTCCCGCCATTTACTGCCGTACCTTGGCCGTACAGGGCCGCGCGCCGTACAACGCCGTACGCCGTACAAGGCCGTACGCCGTACGCCGTACGCCGTACCCAGCCGTACAGTTAAAGCCGTACTTGGCCGTACCGGCCGTACCGCCGTACTTGCAGTCGCCGTACATATGCCGTACCCCACTTTACGCCGTACGTTTTGTTGCCGTACACAGCCGTACAATAACATGCCGTACGCCGTACCTACGCCGTACCTCGCAGCCGTACTCGCCGTACTTTCCTGCCGTACAGCCGTACGCTGCCGTACGCCGTACAGGCCGTACAGCCGTACTCGCCGTACTAGCCGTACTGTGCCGTACCGAAGCCGTACGCCGTACTCGCCGTACCGCCGGCCGTACACGCCGTACTTGCCGTACCAGCCGTACGAAAGCCGTACCGCCGTACCAATATTGGGCCGTACTATGAGTTACCCGCCGTACGATGACTAAGCCGTACTGATTAGCCGTACTGCCGTACCAGCGTGCCGTACTCAGCCGTACGCCGTACGCCGTACGCTAGCCGTACAAGCCGTACGCCGTACTTTCAACGGCCGTACCGCCGTACAAACGGGCCGTACCTAGCCGTACGTAGCCGTACCTTTTGGCCGTACTGCGCTGGCCGTACGGCCGTACAGCCGTACCCGCCGTACTCTGAGCCGTACGATTTAACCTTATATTGCCGTACCGGCCGTACTGCCGTACGCCGTACGCCGTACTGGCCGTACGCCGTACAAAGCCGTACTAGCCGTACGCCGTACGCCGTACGTAAAGCCGTACACGCCGTACCCGCCGTACGGGCCGTACGAGTAGCCGTACTTTAGCCGTACGGGCCGTACAGGCCGTACGTGCCGTACTGCCGTACGCCGTACGCCGTACGCCGTACGCCGTACGCCGTACGCCGTACCACGCCGTACGGTTGGCCGTACGCCGTACTCGCCGTACTGCGCCGTACACGCCGTACGCCGTACGGCCGTACACCAGCCGTACAGACCGTGCCGTACTAAGCCGTACGGCCGTACGCCGTACGCCGTACGCCGTACGCCGTACCAGCCGTACAAGGCCGTACTGCTGCCGTACGCCGTACCTGCCGTACCGCCGTACGCCGTACGCCGTACCCAGGCCGTACCGCCGTACGTCCGCCGTACAATCGCCGTACATAGTCGCCGAAGCGTGCCGTACATTTGCCGTACACTGAGCCTGGGCCGTACGCCGTACGCCGTACCCGTCGCCGTACATCCGTCCGCCGTACAGGAGGGCTCCAGCCGTACAGCGCCGTACGCGCCGTACCCATGGCCGTACGCCGTACGCCGTACGGCCGTACAGACGCCGTACAGGCCGTACCGCCGTACCGGGCCGTACTCGCCGTACGGCCGTACGCAAACACGCCGTACGCCGTACGCCGTACGCCGTACGCGCCGTACGCCGTACGCCGTACGCGGCCGTACCAGCCGTACAGCCGTACGCCGTACCGCAGCCGTACTGCGCCGTACGCCGTACGGCCGTACGGGCCGTACAATGCCGTACACTATGCCGTACCAGCGTCGCCGTACTTTGCCGTACGCCGTACGCCGTACGCCGTACAAATAGCCGTACGCCGTACAGCGCCGTACGGCCGTACAGCCGTACGGCACAGCCGTACTAGGCCGTACACAGGCCGTACCACAGCGCATATGCCGTACGCCGTACTGGCCGTACGGCCGTACAAGGCAGCCGTACGTGCCGTACGCCGTACGGCCGTACCACCAGCCGTACGCCGTACAGCCGTACCCGCCGTACGTCGCCGTACGGCCGTACGCCGTACTGCCGTACAGTTCGCCGTACGCCGTACGCCGTACGCCGTACAGGCCGTACGCCGTACTGTGCCGTACGTGACAATGTTGCCGTACCGGCCGTACGAGCCGTACAGCCGTACGAGCCTGGCCGTACGCCGTACGCCGTACTCTCGGAACCGCGCCGTACGCCTGCCGTACGCCGTACTGCCGTACCGCCGTACGCCGTACATCGCCGTACGCAGCCGTACGCCGTACTGGCCGTACCGCCGTACAAAAGCCGTACGGCCGTACTGCCGTACGAGGCGCCGTACTAAGCCGTACCGCCGTACAGGCCGTACCCACGGCCGTACGGCCGTACGGGCCGTACGGATGCCGTACGCCGTACGCCGTACGCCGTACGCCGTACCACTCCGCCGTACGCCGTACATCCGTCGTGCCGTACGTTGGCCGTACGCCGTACGCCGTACATTGCCGTACCTAGGCCGTACTCGCCGTACTTGCCGTACGAGCCGTACTTAGAGCCGTACGGGTGGGAGCCGTACCCGGCCTGTAGGCCGTACTAGCCGTACCGCCGTACGCCGTACTCTCGGCCGTACGGCCGTACTCCCGCTTTGTGCAGCCGTACGTCGAAGCCGTACTATATAGCCGTACGTGCACATTCAGGCCGTACACGCCGTACCTGCCGTACCGCCGTACTAGAGCCGTACCGCCGTACTTTCGCTCAGCAGCCGTACGCCGTACGCCGCCGTACCAGGTGGCCGTACAGCCGTACTACAAGGCCGTACGCCGTACCCGCCGTACACAGCGGCCGTACTGCCGTACTCCAGCCGTACGCAAGCCGTACGCCGTACAGCCGTACGCCGTACCCGACGCTAGCCGTACGCCGTACGCCTAGCCGTACAACGCCGTACGCCGTACAGCCGTACGCCGTACGCCGTACGCCGTACGCCGTACAGCCGTACTTGCCGTACATAGCCGTACTGCCGTACGCCGTACCTTATGCCGTACGCCGTACCGCCGTACGCCGTACGAGGGCCGTACGGCCGTACGCCGTACACGCCGTACGGCCGTACGCCGTAC
    0 49 56 108 115 157 176 198 205 224 231 240 247 262 324 441 520 605 612 690 785 808 958 1044 1081 1088 1103 1136 1182 1212 1224 1243 1262 1278 1327 1334 1366 1453 1479 1496 1529 1552 1613 1620 1630 1799 1806 1840 1847 1854 1953 1972 1979 1986 2079 2189 2270 2324 2343 2375 2411 2418 2425 2452 2484 2491 2498 2530 2593 2612 2630 2637 2664 2712 2781 2822 2858 2925 2957 3042 3070 3139 3146 3153 3180 3211 3260 3267 3288 3305 3376 3394 3401 3470 3527 3534 3541 3588 3595 3602 3618 3633 3640 3673 3691 3849 3856 3863 3898 3930 3956 3963 3985 4006 4026 4047 4075 4082 4089 4096 4103 4120 4146 4270 4304 4374 4453 4535 4542 4587 4594 4601 4608 4681 4688 4707 4748 4884 4891 4915 4930 4951 4967 4984 5022 5106 5135 5257 5278 5285 5292 5308 5348 5420 5436 5504 5521 5528 5535 5676 5737 5747 5810 5979 5986 5993 6013 6180 6187 6203 6229 6236 6340 6347 6354 6361 6368 6375 6404 6439 6497 6504 6511 6518 6555 6579 6586 6686 6693 6756 6777 6784 6854 6869 6876 6883 6890 6899 6906 6913 6940 6968 7038 7045 7052 7071 7157 7203 7230 7272 7299 7306 7313 7329 7404 7411 7437 7448 7471 7488 7498 7628 7635 7642 7649 7669 7703 7710 7827 7984 7991 8035 8083 8094 8109 8132 8139 8161 8176 8183 8190 8197 8239 8258 8273 8299 8323 


```python

```