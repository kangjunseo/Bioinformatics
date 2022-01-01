# Find a Profile-most Probable k-mer in a String
## Problem
Given a profile matrix Profile, we can evaluate the probability of every k-mer in a string Text and find a Profile-most probable k-mer in Text, i.e., a k-mer that was most likely to have been generated by Profile among all k-mers in Text. For example, ACGGGGATTACC is the Profile-most probable 12-mer in GGTACGGGGATTACCT. Indeed, every other 12-mer in this string has probability 0.

In general, if there are multiple Profile-most probable k-mers in Text, then we select the first such k-mer occurring in Text.

Profile-most Probable k-mer Problem
Find a Profile-most probable k-mer in a string.

Given: A string Text, an integer k, and a 4 × k matrix Profile.

Return: A Profile-most probable k-mer in Text. (If multiple answers exist, you may return any one.)




```python
def ProfileMostProbable(Text, k, Profile):
    max_score = -1
    target = ''
    code_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    for i in range(len(Text)-k+1):
        score = 1
        for j, base in enumerate(Text[i:i+k]):
            score*=float(Profile[code_dict[base]][j])
        
        if score>max_score:
            max_score = score
            target = Text[i:i+k]
            
    return target

I = input().split()
Text = I[0]
k = int(I[1])
temp = I[2:]
Profile = []
for i in range(4): Profile.append(I[2+i*k:2+(i+1)*k])

print(ProfileMostProbable(Text,k,Profile))

```

    AAATATTACAGTGTTGTGGGAAATCACTGACCTTGTACTGTAACGTTACCCGGGGTCTAACCCCATTCCGCTCGACAGCGCGGAATCGCGTGTGTCACTTCTGTGGATTGGTGTCAATCGTTTTAGCGGAAGGTCCCTCATTTTGTATGGTCCAGGCCGTTGATGGTGTCTCAGTAGTTAAGATCGGTGCTCTCAACTAGTAGAACTCTGAGTATATTCGAAGTTGTGACATTACCGTTATTATCCTAACAACAATCGATAGGACGAATGCGGATATTAACCTACAGCTAATCTAGGTTTAAAGGGAGATTGCCACGGGGACTCGGCGACACCTAGTGGGGGACTCATGCCCTGCTGACCAACTTCTATCAAGGGGGAATTCAACGCGAGTAAGGGCCTTAATCAAGACTGCTTAATTAGCTTGGGCTCCACTACTTGAGTGTACGAGCGGTTTTACTCGAGATGACTCATGGATTGTCAAAACATAAGGTATAGTGGTCCACTAGTCGTATAACTTGTTCTTGGGTAATTAGGTGCGTAAGAATCGGAGAGTCGTGTACAAGAAGTAACAATTCTGCCACCGCTATCGCCACAGGCGTCGGAGATGTATACGGGGCATCAATGCGACTATACGCAAGTCCCATATCCCCTGGGACGTTTTTCAGGTTCACATCTGATTATTCTTAGGGGGAGACCTCCGCTAAAATAGCTGGAAATGAACCGTGCGTTAGAACGTAGGCAGTACAGATGAGCCAAGTCTCTATCAGGTGCCTTGCCAGTCACACCTGGAAATCTACGTGCTCAGTGCGTGGAACCTGGGTAAGTCGTACCGCTAGCTGCAGCATACTAGCCTAAATGGCGTTCCGAGCTATCGGTGGTGAAGTAGCTAGAGGAGATAAGCTTCAGGGTAATTATAAGTCGAAGGCAAACATAATGAGCTGTTCGCGCGAGTCGACTATCGACAATGTTTACAAGCGCACCTGCGATGAGCTAACTCCCT 15 0.288 0.197 0.197 0.303 0.303 0.197 0.303 0.227 0.318 0.333 0.288 0.288 0.303 0.242 0.212 0.197 0.273 0.303 0.288 0.197 0.273 0.227 0.212 0.212 0.197 0.273 0.136 0.197 0.318 0.197 0.182 0.258 0.242 0.273 0.242 0.288 0.227 0.303 0.106 0.242 0.197 0.318 0.227 0.152 0.258 0.333 0.273 0.258 0.136 0.258 0.242 0.242 0.258 0.364 0.227 0.242 0.258 0.273 0.288 0.333
    ACTAGTCGTATAACT



```python

```


```python

```