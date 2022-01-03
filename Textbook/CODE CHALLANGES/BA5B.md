# Find the Length of a Longest Path in a Manhattan-like Grid
## Problem
Length of a Longest Path in the Manhattan Tourist Problem
Find the length of a longest path in a rectangular city.

Given: Integers n and m, followed by an n × (m+1) matrix Down and an (n+1) × m matrix Right. The two matrices are separated by the "-" symbol.

Return: The length of a longest path from source (0, 0) to sink (n, m) in the n × m rectangular grid whose edges are defined by the matrices Down and Right.


```python
def InputParsing(I):
    n, m = int(I[0]), int(I[1])
    Down = []
    Right = []
    for i in range(n): Down.append(list(map(int,I[2+i*(m+1):2+(i+1)*(m+1)])))
    for j in range(n+1): Right.append(list(map(int,I[3+n*(m+1)+j*m:3+n*(m+1)+(j+1)*m])))

    return n, m, Down, Right

def ManhattanTourist(n, m, Down, Right):
    graph = [[0 for _ in range(m+1)]for _ in range(n+1)]
    
    for i in range(1,n+1): graph[i][0] = graph[i-1][0] + Down[i-1][0]
    for j in range(1,m+1): graph[0][j] = graph[0][j-1] + Right[0][j-1]
    
    for i in range(1,n+1):
        for j in range(1,m+1): 
            graph[i][j] = max((graph[i-1][j] + Down[i-1][j]),(graph[i][j-1] + Right[i][j-1]))
    
    return graph[n][m]

```


```python
n, m, Down, Right = InputParsing(input().split())
print(ManhattanTourist(n,m,Down,Right))
```

    8 13 4 1 0 4 3 2 0 3 0 4 0 4 4 0 4 1 1 4 4 4 1 4 0 3 4 0 1 3 3 2 0 3 1 1 2 2 1 3 4 2 1 2 3 1 1 3 4 2 2 4 4 1 0 0 0 4 0 1 2 2 2 4 2 1 4 2 0 0 4 0 3 4 3 1 2 1 0 2 4 3 4 0 2 0 0 3 0 0 4 2 1 3 4 1 3 0 3 0 1 0 3 3 3 4 0 1 3 1 1 3 4 0 - 4 3 3 3 1 0 3 3 0 2 3 3 0 3 2 2 0 3 4 3 3 0 4 0 4 3 3 2 0 2 3 4 4 0 4 1 3 2 2 1 3 4 1 1 0 3 2 1 2 2 4 0 0 2 3 0 2 0 2 3 1 2 4 4 3 1 2 4 4 4 2 3 3 2 1 4 3 1 0 1 2 4 2 4 1 2 4 4 3 0 1 2 2 2 1 2 2 2 2 0 1 3 1 3 1 4 3 0 3 3 4 3 4 0 1 4 0
    69



```python

```
