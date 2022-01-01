# Find a Median String
## Problem
Given a k-mer Pattern and a longer string Text, we use d(Pattern, Text) to denote the minimum Hamming distance between Pattern and any k-mer in Text,

d(Pattern,Text)=minall k-mers Pattern' in TextHammingDistance(Pattern,Pattern′).

Given a k-mer Pattern and a set of strings Dna = {Dna1, … , Dnat}, we define d(Pattern, Dna) as the sum of distances between Pattern and all strings in Dna,

d(Pattern,Dna)=∑i=1td(Pattern,Dnai).

Our goal is to find a k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern, the same task that the Equivalent Motif Finding Problem is trying to achieve. We call such a k-mer a median string for Dna.

Median String Problem
Find a median string.

Given: An integer k and a collection of strings Dna.

Return: A k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern. (If multiple answers exist, you may return any one.)


```python
from itertools import product

def HammingDistance(p, q):
    distance = 0
    for i, j in zip(p, q):
        if i!=j: distance +=1
    return distance


def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for strand in Dna:
        HD = 1e9
        for i in range(len(strand)-k+1): HD = min(HD,HammingDistance(Pattern,strand[i:i+k]))
        distance += HD
        
    return distance

def MedianString(Dna, k):
    distance = 1e9
    patterns = []
    median = ''
    
    for i in product('ATGC', repeat=k): patterns.append(''.join(i))
        
    for pattern in patterns:
        temp = DistanceBetweenPatternAndStrings(pattern, Dna)
        if distance > temp:
            distance = temp
            median = pattern
    
    return median

I = input().split()
print(MedianString(I[1:],int(I[0])))
```

    6 AGCTAGTGCTGACATTAGCTTTAGATTACTAACATCCCAGAT GGAATACTAGATCAAATAGCTATCTGACGCACAGTTCGGCGC CAATAGCCAGATGCAGAAACTTAAGAGCTCTGCTGAATCGAT CTAGATCCGTGAAGTAAAAAAAGCCTTCTCAGGGGAGTAGAA GGACCCCCAGATTGCGGTGTCGGCACTTATGTGAGTCGGCTG TCTATATAGCCGTGACGGAATTGCCGAGATCGTCATGGTACC AATCTCCGGCGGCCAGATATTAATGTCCAAACCGGGGATGTA GGGAATACGATTGGCTACATCATACCTCACCCAGATTCAACA GCAGGGACAGGTGAGGGGGTAAAACCATGGAGAAGCCGAGAT TGGCTATTTGATCACAGGCCCTAGCTAGATGACTGCCGCACG
    CCAGAT


## Usage of Itertools.product


```python
from itertools import product

patterns = []
k=3
for i in product('ATGC',x repeat=k):
    patterns.append(''.join(i))
    
print(patterns)
```

    ['AAA', 'AAT', 'AAG', 'AAC', 'ATA', 'ATT', 'ATG', 'ATC', 'AGA', 'AGT', 'AGG', 'AGC', 'ACA', 'ACT', 'ACG', 'ACC', 'TAA', 'TAT', 'TAG', 'TAC', 'TTA', 'TTT', 'TTG', 'TTC', 'TGA', 'TGT', 'TGG', 'TGC', 'TCA', 'TCT', 'TCG', 'TCC', 'GAA', 'GAT', 'GAG', 'GAC', 'GTA', 'GTT', 'GTG', 'GTC', 'GGA', 'GGT', 'GGG', 'GGC', 'GCA', 'GCT', 'GCG', 'GCC', 'CAA', 'CAT', 'CAG', 'CAC', 'CTA', 'CTT', 'CTG', 'CTC', 'CGA', 'CGT', 'CGG', 'CGC', 'CCA', 'CCT', 'CCG', 'CCC']



```python

```
