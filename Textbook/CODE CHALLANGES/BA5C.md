# Find a Longest Common Subsequence of Two Strings
## Problem
Longest Common Subsequence Problem
Given: Two strings.

Return: A longest common subsequence of these strings.



```python
def LCSBackTrack(v, w):
    graph = [[0 for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    BackTrack = [['' for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            match = 0
            if v[i-1] == w[j-1] : match = 1
            
            graph[i][j] = max(graph[i-1][j],graph[i][j-1],graph[i-1][j-1]+match)
            
            if graph[i][j]==graph[i-1][j]: BackTrack[i][j]+='d'
            elif graph[i][j]==graph[i][j-1]: BackTrack[i][j]+='r'
            elif graph[i][j]==graph[i-1][j-1]+match: BackTrack[i][j]+='m'
                
    return BackTrack

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0: return ""
    
    if backtrack[i][j]=='d': return OutputLCS(backtrack, v, i-1, j)
    elif backtrack[i][j]=='r': return OutputLCS(backtrack, v, i, j-1)
    else: return OutputLCS(backtrack, v, i-1, j-1) + v[i-1]
```


```python
v, w = input().split()
print(OutputLCS(LCSBackTrack(v, w), v, len(v), len(w)))
```

    ATGGAATGCATCCCACCAAGGCACTGGAACCGTAAATTGGAGCCGACTGCTAGGTTTTGCTCGAAACCGATTGTCGGGACAGATGAGCAATTTGTTTTCGGACTGATTTCGCGAGTTGCCGGGACATGTCTTTTAACGTCTCACTTCTAATAAATGTGATCCAGAAATTGGACGTAATCCAGACGCACAGCACCGGCGAGCAGGAGCTGGAGGTGGATTAGCCGAAAACCGACTAGCAGTCTGTAACATTTGACTATCACGAGTTTAACGATGAACATGCACCGCGGGGGAGTTAGGAGGTGCGGACGCTGCTTGCCTGGACTCAGATTAACGATTCACGATCCCTGGCCGGCAAGATCAAGAATTGACGGCGGCAAATATTTCCCAATACCAATGTATAACATACTAGAAGTCGTGCCATACTTATAGACTAGTGAGACAAGATATCTGAGTTCCACCCTGCGCCTTATGCTGTGACGTACTCGAGAAGTTCATCCTGCATGAGTCGGGGCGCCAGACTTGACGCGCCAAATCGTTGTGTCATAGGAAGTGGGCAATTGGGTAGCAGTATCCTATCGCCACGACATCGCGCGGTACAGTTACCCCGCAGTAGCGTCGTCTATCATAGGCTTATAGAATTTTAAGCACAGAGTTGTGCGGTCTAGTCCGGCTACTGGAGTGTTCAAACCATTAGCAGAAAGCAGTGTCAATCCACTTTATACTTGTCAGTCTTCCCAGCGCTGGTGCGTCTACTCGGATTTTCCGAGGGACGCAGAGGGGCCTATCTAGCACTATTAAGTAGCAGGGAATGGTCATCAAGTCAGTACCCTGTTCAGCTCGTTCTCTATCAGTATCGTCCAGCATTTTAGTCGGTAGTAAGTCTCCCTAGCA TTATACCATGCATTTCTTTATTTGCTGAGTTGGTACACCTGGGAATAGCATTAAGAGCTGACGAACGCGAAGGAAGTCACATCACTCAAGTCGTAACGGGAAGGTGACAAAAGTTTTCGCTCCAAAGTAGCGAGACCGGGCTAGCGAGGTCTCCTGCACACTGGGACTATGTCTCTTTCTCCTGACCACCCAATGTTAGCCAATCCGGGAACCTCATACAACAGGAAAGGGCTTAACGTAGCACAGCGACCCCCCCCAAATCTCAACTCAGTAAATTGTTCATTTCATGGTCTCTGCTTACACCACCGCGCACAGCTCAATCCCAGCTGCCAGGACTGGGGTGCAAGATTTGCGCCAGCGGTGAATCCGATCCACATTCCAGCCACAACGTCCGAAGGGACCCACAGTCCGACGATTCACGAACCTATCTCACATGATAACAACGGACGTTGTTCCGGATACCTCTTTTGGCTAGCTGACATTTTCTGGATCGTCCAGGCTTGGGATGTGCCCACTCGAACTTAAAAAATTGATGCCAGGCCGTGCACCGCAGACGACTCGACGGGGACGTAATGTCGACAATGGATGGCCCCTCTTTATCTGAAGCAAACTAAGTGTCCTTGGAGGCAACACATCGGAGATAACTCGGCGGGTACTTCCAGGCTGGGCACGCGGTCTTCGACGTGCTCGGGGTGCTTTTAGGCCATCGGTAAGTCTTTGCGTCCTTATGCTGCGCTCCATACGCCTGGTACGTCAGTGAGCAGAGACTGACGTTGCATCTTTTCCACTTTTATGAACGAGCTGTATCCTAGCCTGAACGCTCCAACAAATTTCCTTAGCTTGTTGGTACCAATTCAGGAAACTCTATAAACTTTCGTTGACGTAGATTGGCTGACTCGACACAATAGGCAGGGCCCGTATCTTAAGT
    ATAATGCATCACAGGCACTGGAATAATTGAGCCGACGCAGGGTCAAACCGTGTCGGGAAGTGACAAGTTTTCGGACGACGCGAGTTGCCGGGACATGTCTTTTCTCTCACCAATGTGCCAATGGGAATCAACAACAGGAAGGGCTAGTGAAGCGAAAACCACTCAGTAAATTGTTCACAGTTTCTACACACCGCGAGTTAGGAGGTGGGGTGCTTGCGCCAGTAACGATCACATCCGCCCAAGTCGAAGGGCCAATATTCCAATACCAATGATAACAACGAGTGTCCATACTTTGCTAGTGACATTCTGAGTCCAGGCTTATGTGTGACTATGAGAGTCACCGCAGAGTCGGGGGCGATTGACGGCCTCTTTTCTAGAAGTGCTTGGAGCAACCATCGAGACTCGGCGGTACTTCCGCTGCGCGTCTTCATGCTTGTTTTAGCACGAGTTTGCGTCTAGTCGCTATAGTGTACCATAGCAGAAACGTGCATCCACTTTATACGAGCTTCCAGCCTGCGCTCCATTTCCAGCGGGTACCAATTCAGGAATTATAAACTTTCGTCGTTTCTATCGACACATAGCGGGTATCTTAG



```python

```