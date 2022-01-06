# Align Two Strings Using Affine Gap Penalties
## Problem
A gap is a contiguous sequence of spaces in a row of an alignment. One way to score gaps more appropriately is to define an affine penalty for a gap of length k as σ + ε · (k − 1), where σ is the gap opening penalty, assessed to the first symbol in the gap, and ε is the gap extension penalty, assessed to each additional symbol in the gap. We typically select ε to be smaller than σ so that the affine penalty for a gap of length k is smaller than the penalty for k independent single-nucleotide indels (σ · k).

Alignment with Affine Gap Penalties Problem
Construct a highest-scoring global alignment of two strings (with affine gap penalties).

Given: Two amino acid strings v and w (each of length at most 100).

Return: The maximum alignment score between v and w, followed by an alignment of v and w achieving this maximum score. Use the BLOSUM62 scoring matrix, a gap opening penalty of 11, and a gap extension penalty of 1.


```python
BLOSUM62 ={'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 
           'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 
           'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 
           'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 
           'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 
           'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 
           'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 
           'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 
           'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 
           'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 
           'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 
           'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 
           'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 
           'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 
           'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 
           'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 
           'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 
           'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 
           'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 
           'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}

def GPBackTrack(v, w):
    
    # Init the 3 graphs and Backtrack
    M = [[0 for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    L = [[0 for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    U = [[0 for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    BackTrack = [[['','',''] for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    
    for i in range(1,len(v)+1): M[i][0], L[i][0], U[i][0] = -(10+i), -(10+i), -1e9
    for j in range(1,len(w)+1): M[0][j], L[0][j], U[0][j] = -(10+j), -1e9, -(10+j)
    
    
    # Populate values of graphs and Backtrack
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            L[i][j] = max(L[i-1][j]-1, M[i-1][j]-11)
            U[i][j] = max(U[i][j-1]-1, M[i][j-1]-11)
            M[i][j] = max(L[i][j], U[i][j], M[i-1][j-1]+BLOSUM62[v[i-1]][w[j-1]])
            
            if L[i][j]==L[i-1][j]-1: BackTrack[i][j][1]+='d'
            else: BackTrack[i][j][1]+='m'
                
            if U[i][j]==U[i][j-1]-1: BackTrack[i][j][2]+='r'
            else: BackTrack[i][j][2]+='m'
            
            if M[i][j]==L[i][j]: BackTrack[i][j][0]+='d'
            elif M[i][j]==U[i][j]: BackTrack[i][j][0]+='r'
            else: BackTrack[i][j][0]+='m'
    
    print(M[len(v)][len(w)])
    
    return BackTrack


def OutputLA(backtrack, v, i, j, f):
    if(i==0 and j==0): return ''
    
    if f==0:
        if backtrack[i][j][f]=='d': return OutputLA(backtrack, v, i, j, 1)
        elif backtrack[i][j][f]=='r': return OutputLA(backtrack, v, i, j, 2)
        else: return OutputLA(backtrack, v, i-1, j-1, 0) + v[i-1]
    
    elif f==1:
        if backtrack[i][j][f]=='d': return OutputLA(backtrack, v, i-1, j, 1) + v[i-1]
        else: return OutputLA(backtrack, v, i-1, j, 0) + v[i-1]
            
    else:
        if backtrack[i][j][f]=='r': return OutputLA(backtrack, v, i, j-1, 2) + '-'
        else: return OutputLA(backtrack, v, i, j-1, 0) + '-'


def OutputLA2(backtrack, v, i, j, f):
    if(i==0 and j==0): return ''
    
    if f==0:
        if backtrack[i][j][f]=='d': return OutputLA2(backtrack, v, i, j, 1)
        elif backtrack[i][j][f]=='r': return OutputLA2(backtrack, v, i, j, 2)
        else: return OutputLA2(backtrack, v, i-1, j-1, 0) + v[j-1]
    
    elif f==1:
        if backtrack[i][j][f]=='d': return OutputLA2(backtrack, v, i-1, j, 1) + '-'
        else: return OutputLA2(backtrack, v, i-1, j, 0) + '-'
            
    else:
        if backtrack[i][j][f]=='r': return OutputLA2(backtrack, v, i, j-1, 2) + v[j-1]
        else: return OutputLA2(backtrack, v, i, j-1, 0) + v[j-1]
    

v, w = input().split()
BT = GPBackTrack(v, w)

print(OutputLA(BT,v,len(v),len(w),0))
print(OutputLA2(BT,w,len(v),len(w),0))
```

    KLTLYDPELKRLLWYPWITMWWHMLYLPRRREWGKYLQPLYTEMNVRRTYWERHYVAPRETDTVLAKMYWNNIY KQIQTLLDPELKRKLWYPWITMWWHMLYLQTWHHCRRREWGKWHLQPFYTEMNVYRTYWERHSAFDANRTDIVLAKSYWNNIY
    293
    KL--TLYDPELKRLLWYPWITMWWHMLYLP-----RRREWGKY-LQPLYTEMNVRRTYWERH--YVAPRETDTVLAKMYWNNIY
    KQIQTLLDPELKRKLWYPWITMWWHMLYLQTWHHCRRREWGKWHLQPFYTEMNVYRTYWERHSAFDANR-TDIVLAKSYWNNIY



```python

```
