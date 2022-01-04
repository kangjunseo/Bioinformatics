# Find a Highest-Scoring Overlap Alignment of Two Strings
## Problem
When we assembled genomes, we discussed how to use overlapping reads to assemble a genome, a problem that was complicated by errors in reads. We would like to find overlaps between error-prone reads as well.

An overlap alignment of strings v = v1 ... vn and w = w1 ... wm is a global alignment of a suffix of v with a prefix of w. An optimal overlap alignment of strings v and w maximizes the global alignment score between an i-suffix of v and a j-prefix of w (i.e., between vi ... vn and w1 ... wj) among all i and j.

Overlap Alignment Problem
Construct a highest-scoring overlap alignment between two strings.

Given: Two protein strings v and w, each of length at most 1000.

Return: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v’ of v and a prefix w’ of w achieving this maximum score. Use an alignment score in which matches count +1 and both the mismatch and indel penalties are 2. (If multiple overlap alignments achieving the maximum score exist, you may return any one.)




```python
def OverlapBackTrack(v, w):
    graph = [[0 for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    BackTrack = [['' for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    
    for i in range(0,len(v)+1): BackTrack[i][0]+='s'
        
    for j in range(1,len(w)+1): 
        BackTrack[0][j]+='r'
        graph[0][j]-=j*2
    
    # find first overlap part
    start = 0
    for idx, i in enumerate(v):
        if i == w[0]: 
            start = idx
            break
    
    for i in range(start+1,len(v)+1):
        for j in range(1,len(w)+1):
            match = -2
            if(v[i-1]==w[j-1]): match = 1
            graph[i][j] = max(graph[i-1][j]-2,graph[i][j-1]-2,graph[i-1][j-1]+match)
            
            if graph[i][j]==graph[i-1][j]-2: BackTrack[i][j]+='d'
            elif graph[i][j]==graph[i][j-1]-2: BackTrack[i][j]+='r'
            elif graph[i][j]==graph[i-1][j-1]+match: BackTrack[i][j]+='m'
    
    max_idx = 0
    for i in range(0,len(w)+1):
        if graph[len(v)][max_idx] < graph[len(v)][i]: max_idx = i
        
    print(graph[len(v)][max_idx])
    
    return BackTrack, max_idx

def OutputLA(backtrack, v, i, j):
    if backtrack[i][j]=='s': return ''
    elif backtrack[i][j]=='d': return OutputLA(backtrack, v, i-1, j) + v[i-1]
    elif backtrack[i][j]=='r': return OutputLA(backtrack, v, i, j-1) + '-'
    else: return OutputLA(backtrack, v, i-1, j-1) + v[i-1]

def OutputLA2(backtrack, v, i, j):
    if backtrack[i][j]=='s': return ''
    elif backtrack[i][j]=='d': return OutputLA2(backtrack, v, i-1, j) + '-'
    elif backtrack[i][j]=='r': return OutputLA2(backtrack, v, i, j-1) + v[j-1]
    else: return OutputLA2(backtrack, v, i-1, j-1) + v[j-1]

v, w = input().split()
BT, max_idx = OverlapBackTrack(v, w)

print(OutputLA(BT,v,len(v),max_idx))
print(OutputLA2(BT,w,len(v),max_idx))
```

    GAGAGTGGAAAACAGGCCAGGTGTTCTAATGACGCACGAGAGATAGAACCACGTCTGTGTGTCTAAGAACTGGCTGAGGCCATAAAAAGGGACTTGTGGGGGTACGAAGTGTGTGTAGTTCCGCGTCCGCATTATCCGTTAGTGCTATGGGTCCCCTCTCTCATTACACCGGGACCACGGTCCCTACATTTTCCATGCAGTCTTAAAGGTGAATGCTAGTGGACGGAGCCATTACAAATGGTATCCATACTTTTTAAACAACGCACTCCACTTTGACACCGAATAGCTTGGATCTACTGAAGCATTTCCAAGTGGAGCATGACATTTATCCTCTTCATCTGACGACCGGCAACAACCCGCACTTTTACCTTACAGCGACCTAGATACACCACCAATGTGAGCGCCGGGCTTGAACGTGGGGATCAATAGGGCCATTGAAGAGCTAAGGGAAATAGGCCGTGTCGAAACAAAATGGGCATGCCGATTGCAATCAATACAGCTTGTTTAATATCTCCGTTTTTAAAGTCAAGCACGGGGATCACCCGTCCATCGAGCTGACACACTTTGATGCTTGCTTGGGTCTAGTCTAAGGCTAAAGTCGGTTCAGCGGTAACCCTACGCCGACCATTCCCGCACAAAGGCAAATCCGGTGCGAGCTCCGATGTCACCGCTCAATCGGTGCCGACTGCGGTTCCTCGGAATCGTGCAAATGTGCTTCCATCATCGGACTACTCATCAACATGACTAAGAGCTTTTCCGTGCATGGTCCTCGATGCACCGGCTATCGCTTGTCACTTACTTTCCGCCACCCTGTGCGGCCTATACAGAAAGCATTCCAAACGAATATTAATACTTACGACTAATGGACAGACCCTTGCCCGGCCAATACGCTTCCTGGATGGGTTTGACGGCGGA TAACACCAACGGAATACGGTCCAACGGTGTTCTTCTCGATTCGGTGCAAATTGTCTCCATCGCGGACTTGCTCATCAACATGCTAAGATCTTCGTCCACGCATGGTTCGATTATGCATACGGATTGTTCGGCTTGTCCGCCTACCTTTCCGCCACTTTGCGGCCATTAGAAGACACTTCCAAACGTAACATTAATACTTAGCACTATCGACAGTCCCCTTGTTTGGCCAATATTGCTTCTGATGTGCTTTAACGGCGGGTCGCACTGACGTCTCTTAGTTCGCAAGTTCAGGATTGTACCAAATTGGAGCATTCACGGTAAAGGTCGGACAAGGAAGTCACAGATCCCATCCCTCGGACGCAGCTACCGATAAGTTTACGAACCCCTAGTCATCAAGGACCTGCGATAAACACTCTAGGTTCAACGCAAATCTCGCAGTTGGAGTTATTGCTCGATTACGCACAGAGATCAGCGCGGAGCTAAACTCAACTGGGATGACGTTGGAGCATGCTCTGCACCTACTTAAAGGCGGGCCGGATGGTCGCGTCTGCAGGATCGTTAAGATTATTAAGCGAGAACAAAGTGCCCCTTATATTCGCCTGTAATGCGACTATACGCTTGGCAATCGTACATATCTTCTAATGTCCTTGGAAAGGCCCTCCGCTTCGATTGAAATTAGGTCCAAACATATTTGAGGCCTTCCGCGTCGAAGGCCGTTTTATCTGCTATATTGCGTCATTTAGGTTTACTTGGACCTTGAGCCGCTCGTATTGAGCAAATATGGCAAGTGGCCTAGCAAACCAAGCAGCTCAGAAAGATTATGTTGGAAACTATAGTCGGTTTCCAGGCCCTATTTGCGCGCGATGTCACGCAGCCTCGAGAATCGATTT
    56
    T--CACCG-CTCAAT-CGGTGCCGACTGCG-GTTC--CTCGGAATCG-TGCAAAT-GTGCTTCCATCATCGGACTA-CTCATCAACATGACTAAGAGCTTT-TCCGTGCATGGTCCTCGAT---GCAC-CGGCTA-T-CG-CTTGTCA-CTTAC-TTTCCGCCACCCTGTGCGGCCTATACAGAA-AGCA-TTCCAAACG-AATATTAATACTTA-CGACTAATGGACAGACCC-TTGCCCGGCCAATAC-GCTTCCTGGATGGG-TTTGACGGCGGA
    TAACACCAACGGAATACGGT-CCAAC-G-GTGTTCTTCTCG-ATTCGGTGCAAATTGT-CT-CCATCG-CGGACTTGCTCATCAACATG-CTAAGATCTTCGTCCACGCATGGT--TCGATTATGCATACGGATTGTTCGGCTTGTCCGCCTACCTTTCCGCCACT-T-TGCGGCC-ATT-AGAAGA-CACTTCCAAACGTAACATTAATACTTAGC-ACTA-TCGACAGTCCCCTTGTTTGGCCAATATTGCTTC-TG-ATGTGCTTTAACGGCGG-



```python

```
