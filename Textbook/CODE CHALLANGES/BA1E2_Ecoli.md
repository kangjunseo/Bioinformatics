## Advanced Problem
If you think your solution is efficient enough, try it out on the E. coli genome, the workhorse of bacterial genomics.

Exercise Break: How many different 9-mers form (500,3)-clumps in the E. coli genome? (In other words, do not count a 9-mer more than once.)


```python
def FrequencyTable(Text, k):
    frequencyTable = {}
    
    for i in range(len(Text)-k+1):
        if(Text[i:i+k] in frequencyTable): 
            frequencyTable[Text[i:i+k]][0]+=1
            frequencyTable[Text[i:i+k]].append(i)
        else:  frequencyTable[Text[i:i+k]]=[1,i]

    return frequencyTable

file = open("Ecoli_genome.txt",'r')
Text = file.read()
k,L,t = 9, 500, 3

FT = FrequencyTable(Text,k)

clumps = 0
for i in FT:
    if(FT[i][0]>=t):
        flag = False
        for idx in range(1,len(FT[i])-t+1):
            if(FT[i][idx+t-1]-FT[i][idx]<=L-k): flag = True
        if(flag): clumps+=1
            
print(clumps)
file.close()
```

    1904



```python

```
