# Find a Topological Ordering of a DAG
## Problem
Topological Ordering Problem
Find a topological ordering of a directed acyclic graph.

Given: The adjacency list of a graph (with nodes represented by integers).

Return: A topological ordering of this graph.




```python
def Topology(adj, pred, indeg):
    queue = []
    
    for i in adj:
        if i not in indeg: queue.append(i)
    
    while (len(queue)!=0):
        front = queue.pop(0)
        print(front,end=', ')
        
        if front in adj: 
            for i in adj[front]: indeg[i] -= 1
            
        for i in indeg:
            if indeg[i]==0: 
                queue.append(i)
                indeg[i]=-1

adj = {}
pred = {}
indeg = {}
I = input().split()

for i in range(0,len(I),3):
    preds = I[i+2].split(',')
    adj[I[i]] = preds
    
    for j in preds:
        if j not in pred: pred[j] = [j]
        else: pred[j].append(j)

for i in pred: indeg[i] = len(pred[i])

Topology(adj,pred,indeg)
        
```

    0 -> 21,27,28,29 1 -> 15,17,19,2,23,31,5 10 -> 21,22,27,32 11 -> 14,17,32 12 -> 24,29 13 -> 22,31,33 14 -> 17,20,26,32 15 -> 17,18,22,24,25,32,33 16 -> 19,21,27,31 17 -> 20,25,26,27 18 -> 22,23,26,27,31 19 -> 23,24,26,32 2 -> 28,29,32,4,9 20 -> 24,28,31 21 -> 27 23 -> 29 25 -> 26,33 28 -> 30 29 -> 30 3 -> 12,13,29,9 32 -> 33 4 -> 13,6 5 -> 11,13,15,17,24,33 6 -> 20,21 7 -> 17,23,24,8,9 8 -> 23,30,32 9 -> 13,24,25,33
    0, 1, 10, 16, 3, 7, 2, 5, 19, 12, 8, 4, 9, 15, 11, 6, 13, 18, 14, 21, 23, 22, 17, 32, 29, 27, 20, 25, 28, 31, 24, 33, 26, 30, 


```python

```
