# Find Frequent Words with Mismatches and Reverse Complements
## Problem
We now extend “Find the Most Frequent Words with Mismatches in a String” to find frequent words with both mismatches and reverse complements. Recall that Pattern refers to the reverse complement of Pattern.

Frequent Words with Mismatches and Reverse Complements Problem
Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.

Given: A DNA string Text as well as integers k and d.

Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.


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
    complement = str.maketrans('ATGC','TACG')
    RC = Text.translate(complement)[::-1]
    
    Patterns = []
    freqMap = {}
    n = len(Text)
    
    for i in range(n-k+1):
        neighborhood = Neighbors(Text[i:i+k],d)
        for neighbor in neighborhood:
            if neighbor not in freqMap: freqMap[neighbor]=1
            else : freqMap[neighbor]+=1
                
    for i in range(n-k+1):
        neighborhood = Neighbors(RC[i:i+k],d)
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

    ATAATACCGAGTCGTCCCGTCATAATAATACCGACTCCGTCGTCGACCATAGAGAGAATAGAGAGTCCTCTCCGTCGAGACTCCATACCATACTCCGTCGAGACTGTCATAATAGTCATACTATAGTCATAGTCCTATAGTCCCCTATAGACTATAGTCATACCGTCATAGAATAATAATAGAGTCGTCGTCCCGAATAGAGTCCCGTCATAGACCCTCCCCATACTCT 5 2
    ATATA TATAT 


```python

```
