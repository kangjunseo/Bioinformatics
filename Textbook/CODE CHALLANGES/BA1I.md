# Find the Most Frequent Words with Mismatches in a String
## Problem
We defined a mismatch in “Compute the Hamming Distance Between Two Strings”. We now generalize “Find the Most Frequent Words in a String” to incorporate mismatches as well.

Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as the total number of occurrences of Pattern in Text with at most d mismatches. For example, Count1(AACAAGCTGATAAACATTTAAAGAG, AAAAA) = 4 because AAAAA appears four times in this string with at most one mismatch: AACAA, ATAAA, AAACA, and AAAGA. Note that two of these occurrences overlap.

A most frequent k-mer with up to d mismatches in Text is simply a string Pattern maximizing Countd(Text, Pattern) among all k-mers. Note that Pattern does not need to actually appear as a substring of Text; for example, AAAAA is the most frequent 5-mer with 1 mismatch in AACAAGCTGATAAACATTTAAAGAG, even though AAAAA does not appear exactly in this string. Keep this in mind while solving the following problem.

Frequent Words with Mismatches Problem
Find the most frequent k-mers with mismatches in a string.

Given: A string Text as well as integers k and d.

Return: All most frequent k-mers with up to d mismatches in Text.


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

def FrequentWordsWithMismatches(Text, k, d):
    Patterns = []
    freqMap = {}
    n = len(Text)
    
    for i in range(n-k+1):
        neighborhood = Neighbors(Text[i:i+k],d)
        for neighbor in neighborhood:
            if neighbor not in freqMap: freqMap[neighbor]=1
            else : freqMap[neighbor]+=1
        
    m = max(freqMap.values())
    for key in freqMap:
        if freqMap[key]==m: Patterns.append(key)
        
    return Patterns

Text, k, d = input().split()
for i in FrequentWordsWithMismatches(Text,int(k),int(d)):
    print(i,end=' ')
    
```

    TTACTTCTTGCCGTTACTGGCCGTTACTTGCCTTTAGCCGCTGGCCGGCCTGCCTTTAGCCTCTTCTGGCCGCTGGCCTTTACTTGCCTGCCTGCCTGCCGCTGGCCGGCCGTTAGCCTGCCGCTTCTGGCCGCTTCTGCTTCTGGCCGTTACTTCTGTTACTGCTGGCCGGCCGTTAGCCTGCCGTTATTACTTGCCTCTGCTGCTTTTAGCCGCTGTTACTGGCCTTTACTTTTACTTCTTCTGCTTCTTGCCGTTAGCCTGCCTCTGCTTCTGGCCTCTGCTGGCCTGCCTGCCTCTTGCCGGCCGGCCTGCCGGCCGGCCTGCCGCTTCTGCTTCTGGCCGCTTGCCTGCCGGCCTGCCTCTGGCCTCTTCTTGCCT 5 3
    CCCCC 


```python

```
