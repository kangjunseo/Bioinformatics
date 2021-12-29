# Generate the d-Neighborhood of a String
## Problem
The d-neighborhood Neighbors(Pattern, d) is the set of all k-mers whose Hamming distance from Pattern does not exceed d.

Generate the d-Neighborhood of a String
Find all the neighbors of a pattern.

Given: A DNA string Pattern and an integer d.

Return: The collection of strings Neighbors(Pattern, d).


```python
def HammingDistance(p, q):
    distance = 0
    for i, j in zip(p, q):
        if i!=j: distance +=1
    return distance

def Neighbors(Pattern, d):
    if d==0 : return {Pattern}
    if len(Pattern)==1 : return {'A','T','G','C'}
    
    Neighborhood = set()
    Suffix = Neighbors(Pattern[1:],d)
    
    for i in Suffix:
        if (HammingDistance(Pattern[1:],i) < d):
            for x in ['A','T','G','C']: Neighborhood.add(x+i)
        else: Neighborhood.add(Pattern[0]+i)
            
    return Neighborhood

P,d=input().split()

for i in Neighbors(P,int(d)):
    print(i)
```

    TGTGTTAA 2
    TGGGGTAA
    TGGGTTTA
    TGTGTTTC
    TGGGTTAG
    CGTGTTCA
    TCTGTTAC
    CGTGTTAT
    TCTATTAA
    TGTGATAA
    TGCGCTAA
    TGTGTTCA
    TGCGTCAA
    TTTGTTAA
    TGTGATGA
    TGTTTGAA
    GGTGGTAA
    TCTGTTCA
    TTTCTTAA
    TGTGTGAC
    TGTGTTAG
    GGTGTTTA
    TTTGTTGA
    CGTATTAA
    TATCTTAA
    GATGTTAA
    GGTGTAAA
    TGTGCTCA
    TGTTTAAA
    TGTGCTAC
    TCTGTTTA
    ACTGTTAA
    CGTGTTAA
    TGTATCAA
    AGTGCTAA
    TATGTTAC
    TGTCTTCA
    TATGGTAA
    TTGGTTAA
    TGTGTTAA
    TGTCTGAA
    TTTGGTAA
    TGTGTGGA
    CGCGTTAA
    TGGGATAA
    GGTATTAA
    CGAGTTAA
    AGAGTTAA
    TGTGGTTA
    CGTGTTTA
    CGTGTGAA
    CGTGTTGA
    TGTAGTAA
    TGGGTGAA
    TGTGTTTG
    TGCGTTAG
    TGTGTTAT
    TGTGGTAG
    GGTGTTAA
    TGTATTTA
    AGTGTTTA
    TTTTTTAA
    TGCATTAA
    TGTGTCAC
    TGTGATAT
    TGTGTGAA
    GGTGTCAA
    TGTGTTGC
    CGTGTTAG
    TCTGTGAA
    TAGGTTAA
    TGTATGAA
    TGAGCTAA
    TACGTTAA
    TGTTTTCA
    TGTGTTTT
    TGTGAAAA
    TGTGATAG
    TGTGTAAC
    TGTGTATA
    TGTGTCGA
    TGTGCAAA
    TGTGTAGA
    TGTGTAAT
    TGGGTTGA
    TGGGTTCA
    TGTCTTTA
    TGTGTAAA
    AGTCTTAA
    TGTTTTAA
    TCTCTTAA
    AGTGTTAT
    CGTGCTAA
    TGTGATTA
    AGTGTTAC
    TGTATTGA
    TGTATTAG
    TGTGCGAA
    GGTGTTAG
    AGTGTTGA
    TGTCCTAA
    TTTATTAA
    TGTTTTAT
    TTTGTAAA
    TCTGTTAA
    TGTCTTAT
    TTTGTTAG
    AATGTTAA
    TGTGTCAT
    TATATTAA
    TTAGTTAA
    TATTTTAA
    TATGTAAA
    TGTGGTCA
    TGCGTAAA
    TGTCTTGA
    TCTGTCAA
    TGAGTTAT
    AGTGTCAA
    CCTGTTAA
    TGTGGTGA
    TGTTTTAC
    TGGGTTAT
    TGTGATAC
    TGTTTTAG
    TGAGTAAA
    TATGCTAA
    TGTGTCTA
    TTTGTGAA
    TGTATAAA
    TGTGTCAA
    AGTGTAAA
    TGAGTGAA
    TTTGATAA
    TGACTTAA
    GGTGTTGA
    TGTGGTAA
    GCTGTTAA
    TGTGGTAT
    TGTGATCA
    TGTTCTAA
    TGTATTAC
    TGTGTGTA
    TATGATAA
    TGTGTCCA
    TGGGCTAA
    TATGTTCA
    TGGGTTAA
    TGTATTAT
    TGTGTTAC
    TTTGTTTA
    TGAGTTAA
    TGCTTTAA
    TGTGCTTA
    TGAGTTCA
    TGAATTAA
    TGTGTAAG
    TGTATTAA
    TGCGATAA
    TGAGATAA
    GGTGTTCA
    TGGGTAAA
    TGTGTTTA
    TGTCTTAA
    TGTGCTAA
    TGTGCTGA
    GGCGTTAA
    TCTGTAAA
    TCTGTTAT
    TATGTTAT
    TTTGTTAT
    TGTGGGAA
    TGTGTTCC
    TTCGTTAA
    TATGTTAA
    TGTCTTAG
    TGTGTGAG
    TGTTTTTA
    TATGTGAA
    TGCGGTAA
    AGTTTTAA
    TCTGTTAG
    TGCGTTAC
    CGTGTAAA
    GGTGATAA
    TCTTTTAA
    GTTGTTAA
    AGGGTTAA
    TATGTCAA
    TGCGTTGA
    TATGTTAG
    TCAGTTAA
    TCGGTTAA
    TATGTTGA
    TGAGTTAC
    TCTGTTGA
    TGTGCTAG
    TGTGGCAA
    GGGGTTAA
    TCTGCTAA
    AGCGTTAA
    TGGGTTAC
    CGTGGTAA
    CGTGATAA
    TGTCATAA
    TGTGTTCG
    TGGATTAA
    TGGTTTAA
    TGTCTAAA
    ATTGTTAA
    GGAGTTAA
    TTTGTCAA
    CGTGTTAC
    TATGTTTA
    TTTGTTAC
    TCCGTTAA
    AGTGGTAA
    TGGCTTAA
    TGCGTTCA
    TCTGGTAA
    TGTGTTGG
    TGTGTTGT
    AGTATTAA
    AGTGTTAA
    TGTGACAA
    GGTGCTAA
    GGTGTTAC
    CGTCTTAA
    TGATTTAA
    TAAGTTAA
    TGTGCTAT
    CTTGTTAA
    TGTGAGAA
    TGTCTTAC
    TGTGCCAA
    AGTGTGAA
    CGGGTTAA
    TGCGTTTA
    TGTATTCA
    TGTGTACA
    AGTGATAA
    CATGTTAA
    TCTGATAA
    TGGGTCAA
    TGTGGTAC
    GGTGTTAT
    AGTGTTAG
    TGAGTCAA
    TGAGTTAG
    TTTGCTAA
    CGTTTTAA
    TGCGTTAA
    TGTGTTGA
    AGTGTTCA
    TGTGTCAG
    TGTCGTAA
    TTTGTTCA
    TGCCTTAA
    GGTTTTAA
    TGAGTTGA
    TGCGTGAA
    TGTTTTGA
    TGAGTTTA
    TGTTATAA
    GGTGTGAA
    CGTGTCAA
    TGTGTGAT
    TGCGTTAT
    TGTGGAAA
    TGAGGTAA
    TGTGTGCA
    TGTAATAA
    TGTCTCAA
    TGTTGTAA
    TGTACTAA
    TGTTTCAA
    GGTCTTAA
    TGTGTTCT



```python

```
