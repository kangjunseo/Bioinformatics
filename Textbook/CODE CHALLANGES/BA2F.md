# Implement RandomizedMotifSearch
## Problem
We will now turn to randomized algorithms that flip coins and roll dice in order to search for motifs. Making random algorithmic decisions may sound like a disastrous idea; just imagine a chess game in which every move would be decided by rolling a die. However, an 18th Century French mathematician and naturalist, Comte de Buffon, first proved that randomized algorithms are useful by randomly dropping needles onto parallel strips of wood and using the results of this experiment to accurately approximate the constant π.

Randomized algorithms may be nonintuitive because they lack the control of traditional algorithms. Some randomized algorithms are Las Vegas algorithms, which deliver solutions that are guaranteed to be exact, despite the fact that they rely on making random decisions. Yet most randomized algorithms are Monte Carlo algorithms. These algorithms are not guaranteed to return exact solutions, but they do quickly find approximate solutions. Because of their speed, they can be run many times, allowing us to choose the best approximation from thousands of runs.

A randomized algorithm for motif finding is given below.

    RANDOMIZEDMOTIFSEARCH(Dna, k, t)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string
            from Dna
        BestMotifs ← Motifs
        while forever
            Profile ← Profile(Motifs)
            Motifs ← Motifs(Profile, Dna)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
            else
                return BestMotifs
Implement RandomizedMotifSearch
Given: Positive integers k and t, followed by a collection of strings Dna.

Return: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1000 times. Remember to use pseudocounts!


```python
import random

def MakeProfile(motifs):
    code_dict = {'A':0,'C':1,'G':2,'T':3}
    prof = [[1 for col in range(4)] for row in range(len(motifs[0]))]
    L = len(motifs)
    for motif in motifs:
        for idx, i in enumerate(motif):
            prof[idx][code_dict[i]]+=1
    
    for i in range(len(prof)):
        for j in range(len(prof[0])):
            prof[i][j]/=(L+4)
            
    return prof

def ProfileMostProbable(Text, k, Profile):
    max_score = -1
    target = ''
    code_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    for i in range(len(Text)-k+1):
        score = 1
        for j, base in enumerate(Text[i:i+k]):
            score*=float(Profile[j][code_dict[base]])
        
        if score>max_score:
            max_score = score
            target = Text[i:i+k]
            
    return target

def score(motifs):
    score = 0
    for i in range(len(motifs[0])):
        j = [motif[i] for motif in motifs]
        score += (len(j) - max(j.count("A"), j.count("C"), j.count("T"), j.count("G")))
    return score


def RandomizedMotifSearch(Dna, k, t):
    Motifs = []
    Best = []
    for i in Dna:
        rand_idx = random.randrange(len(Dna[0])-k+1)
        Motifs.append(i[rand_idx:rand_idx+k])
    Best = Motifs
    
    while(1):
        Profile = MakeProfile(Motifs)
        Motifs = []
        for i in Dna: Motifs.append(ProfileMostProbable(i,k,Profile))
        
        if score(Motifs) < score(Best): Best = Motifs
        else: return Best, score(Best)
```


```python
I = input().split()
k,t = int(I[0]),int(I[1])
Dna = I[2:]

min_ = 1e9
Best = None
for i in range(1000):
    motif, loss = RandomizedMotifSearch(Dna,k,t)
    if(loss < min_):
        min_ = loss
        Best = motif
        
for i in Best:
    print(i, end=' ')
```

    15 20 GGGTCTAAAAATGCGTAATTGTACGATTTACGGATCTTGGTGGTCGCCTGAAAAACGGTTGGCGCGATCCTCCAGCCCCCATCCCGTGAGAAAGGTTATATCACGAGAGGAAGAGGACCAGCCGCTCTAGGGAGGCATACCCCTAACATGTGGGGAGAAAATAGGGCAGGGTCTAAAAATGCG TAATTGTACGATTTACGGATCTTGGTGGTCGCCTGAAAAACGGTTGGCGCGATCCTCCAGCCCCCATCCCGTGAGAAAGGTTATATCACGAGAGGAAGAGGACCAGCCGCTCTAGGGAGGCATACCCCTAACATGTGGGCCCCCCGCGTACCATGAGAAAATAGGGCAGGGTCTAAAAATGCG GTCGACGTGGGTCCCATTACGTACCATACGTCGGCTATTCGCGCCATAAGATGCCCAGTCTCAACTACCTGGCTTGATCGTCTTACAACTGATAATGGAGAACTTACTTTACGCATTACCAAGTTAAATATCTGTTCTACTCCGTCCACTTTACGGCTATCTTAGATGAGTCTTCTATTATGG TGTCGGAACCCAACAAGTACCATGTTGACCACTGTTTTTGATACCCCCAGGCATAGGGTCAGATCATCTTCAGCGGGCTGCGGTTCCGTATAAGACGCTTGGAAAAGATGCCTCTCAAACTAAGACTCAGAGTCGTTGGCATTTGGTATAAGTCTAACGGTGGCCTATCGCGCACATTCCCCG AGGTAGAGGGACGCGTCGCCCTCCTGTCTTGGTTATGTTAAAGGGCGCGTCAGCTGAGCACCCAAAGCAATCCATGGAAGGACGAAATCGATCCGCTTTTCCGCAGACGAGCGCTTAGAGGTTCGGTTCCTGGTGGCTGTATACTGTCAGACACTATTAACTCAAGCTGCATTACTAGCGATA TAGGATATACGTTCCGCAGCTGGCGGGTCCAGATTGGAGTGTTGGGTTAGGTATTTTCGGTGTAACTACGGACAAGAAGTTCATATGATTAATACTCCCTGAACTACCTACACTGTCCGTCCGACACGAGAGCCACGTTGCTACGTGTAGCCCCAAAGCGTTTTATCGAATATGGATAATTAC TCAACGGCGTGTGTACATTGGAAAGCGTACCATACAGGCCATATACCGTAACGTTCTAACTACAGTAGAACAGGGCAGTACCATTGTCATAACATAGATTTAGAAAAATCGCGTTAATTTGTTTTCTTGTAAAAACACTACCATGGAGTACAGTCACCAAACATGCGGCAGTTATTAACTGAC TCTTACAACGAAAAGACCAGATTTATCCCAAGTCAAATGATATGACTAAGACACTATGTACGAATACCCTCAACAGGGGCCTTATGCCGACAGCCACCTTCTGCATTTCAAACATATCAAAGCGTACCAGACTCCCTCGTCCATGGGTAGTCGGCCATTCACGGAGACCACGCGGTCATTAGT GGCTGCAGGCATCCTGTAACTTGTAGTATCCCACGATACGGACTTCTTACTGTGCTGTGGGTAATCTCGCCTGTCTTTGTTCCCGATCCCTTTGCAAGCACGACCATCGCAATCTACAGCGCTCGCTTCGTTTTGCCCCGTGCGTACCATAGCCGGTCATGGGCGGGCCCTGAGGCCAGGTCA CTCGAGGACAGCCCACTAGCGTACCATCTTTTAACTTATTGACTTCGCCTTAAGTTTGGGGCAGCTGTGTTTCCGATAGTACGGTCCTCACGAGAACTTGTGCGCAGCCTGTTAGTATCCGCGCTGTTTACCCTGAGAGCGCGCACTGCTTCGCTTTTCGTCCAACGGACGTTAGAACTAAAT TAGTAAAAGGCGTTTACTCGCAGGCCTAGTTATTTACTTTCCCCTCATTCGTTCAACTTTTCTGTAGGCTACCCCGTCTAGTGAGCACATTCTTTGAGGAATCCCACGCCGTACCATCTCAGTCAGTAAATTGGGGACTTCACACCTGAATCCGGCCGGAACCTTCCAGCCCTATGTGGTTTA CATGGCATACTTAGTTTGAGGGGTCACACATAAGGATAAATCATTTTTATTCGCCCCCCCAAATTATACCATAAGGCTCGACATGCCATTAACGGGAATACCTCCCTTTGGTCGGTAACAGCGGCGTCTGGCGTTACCCGTGCCGAAAGAGCGGTGTCCTCTCGGGGCATAAACGACCGCAGA ATTGGGTTGATCCTCGTGGAGTCTATTTGATAGTGTACCGTACTGGGTCGTATGGGACTTTATGGAAAAAAGTTCATTATACAAATGTGTGTGGAGACGCCCAAAGCGCCACATCAGCTATCACCTCGAAGGGCACCCCTCGAATGGAGCGTCCATGCGACAAAGCGAGGCGAAACGTTATCA CTACCAGGAAGGCGACACACTCATGTACCAGTTAGTTAGCTACGCGGAGGGTGGATTATGAAACTGAACCGCACTCCCAAAGCGTACGTGTTATGGTATGCTCCTACAAGTCTTACAACTAAAAGCAGACAACTCTAGAAACTCTTCGGGTATGTTTAAATTTCTCTGAGCAGGTAAAACCAC GTGGGGCGGCCAAAGCGTACCGCTCCTTGACAATCCACTAAACTTAAACAAATCTCGTAACTCAGGCCGTTGGGAGCGAGGTGGCGCCTGCTTGGGGTCACAAAAAGTAGCCAGCCAGCCTCGCTAGTAGGAAAAATGATATCGAGTGAAACCATCCTTGTTCGGGTTCCCCTGATCAGTGCT GAACCACGTCTAAGATGCCGAGGAATGGTGCATTGTCACGTCTCGCAGTAAAGCACGGCGGTAGAAGCTATAAATAGGTTAATCCGGGATCCCAAACACTACCATCCCTTACTGTGGGGGGAACTCTAACTTGACTGGTATTGGATTTAGTGCAACGGCTAGCGCGGCTCTTACCGGCGGCAG TCCTTGACTCGTACAGGTTAAACTCGTGAGAGTTAGCCATACGTCGCATATGAGCAGCATGTCCTACCGCCTCCCAAAGTTAACCATAAAAACTACGTTTCTCTGTTTGCCACTGCACTTTAGCATCACCTAAGCCCTTTCTCGAGGAATGTCTATCGACCCGGTGTACCCGGAACTAAAGCG GTATGGTGAGAGATCGACACTCTATCTGTGAGGCCCTCTGGGTAAGGGGTTGTGGGCCCCGGTTGGGGAGACGATCGCTCAGCTAAATCAGAACACACACCCACACGACAAGTACGCCAACCACTGGGCTAACTATAAGACGGTGGCACGGCAAGCGTACCATGATCGTCCTCCCCCAGACAT GCTTGCGCACATTCCTGAGACCCCTAAGGTTTTCGTGCGGGAGACAATCCACTAGCGACTCGCACTTAAGTTCACAAAAATACCGATACCTAGCCCAATAGGTACCATCCTATAATCGGGAGTCGATACCACAACGGAGAAACCAGACAGTACCTAATGGCAAGAAGCCCATCGCCCTTGAGT TGCGTCAGGCCCATCTTTGTTAAGGCGCGACCGACGCATGTCACCCCCAAAGCGTAGGGTCAAAAACGAGTCGTGCGGCGTTCGCGCTACGCTACAGTAATGAGGCTTGGCGTATCTATACTCCGCACTAGTCGGCATCCTTCGACTCGTGGCGCGCTAGAGGGCCCGAATTAGCCTAGTTCT
    GCGTAATTGTACGAT CCCCCCGCGTACCAT CCCATTACGTACCAT CCCAACAAGTACCAT CCCAAAGCAATCCAT CCCAAAGCGTTTTAT TGGAAAGCGTACCAT ATCAAAGCGTACCAG CCCCGTGCGTACCAT CCACTAGCGTACCAT CCCACGCCGTACCAT CCCAAATTATACCAT CCCAAAGCGCCACAT CCCAAAGCGTACGTG GCCAAAGCGTACCGC CCCAAACACTACCAT CCCAAAGTTAACCAT CGGCAAGCGTACCAT CCCAATAGGTACCAT CCCAAAGCGTAGGGT 


```python

```
