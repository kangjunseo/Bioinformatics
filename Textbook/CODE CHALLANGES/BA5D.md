# Find the Longest Path in a DAG
## Problem
Longest Path in a DAG Problem
Find a longest path between two nodes in an edge-weighted DAG.

Given: An integer representing the source node of a graph, followed by an integer representing the sink node of the graph, followed by an edge-weighted graph. The graph is represented by a modified adjacency list in which the notation "0->1:7" indicates that an edge connects node 0 to node 1 with weight 7.

Return: The length of a longest path in the graph, followed by a longest path. (If multiple longest paths exist, you may return any one.)


```
def LongestPath(adj, predecessors, start, end, indegrees):
    graph = {start:(0,0)}
    queue = [start]
        
    while (len(queue)!=0):
        front = queue.pop(0)
        
        if front != end and front in adj:
            for i in adj[front]: indegrees[i] -= 1
            
            for i in indegrees:
                if indegrees[i]==0: 
                    queue.append(i)
                    indegrees[i]=-1
                    
        if front != start and front in predecessors:
            max_ = -1
            max_pred = None
            for i in predecessors[front]:
                if i not in adj: continue
                prev = 0
                if(front in adj[i]): prev = adj[i][front]
                if(max_ < graph[i][0] + prev):
                    max_ = graph[i][0] + prev
                    max_pred = i
                    
            graph[front] = (max_, max_pred) 
        
    print(graph[end][0])
    
    return graph


def InputLP(I):
    start, end = int(I[0]), int(I[1])
    adj_graph = {}
    predecessors = {}
    indegrees = {}

    for i in I[2:]:
        v, w, weight = map(int,i.replace('->',':').split(':'))
    
        if v not in adj_graph: adj_graph[v] = {w:weight}
        else: adj_graph[v][w]=weight
        
        if w not in predecessors: predecessors[w] = [v]
        else: predecessors[w].append(v)

    for i in predecessors: 
        indegrees[i] = len(predecessors[i])

    dummies = []
    for i in adj_graph:
        if i not in predecessors and i != start: dummies.append(i)
    for i in dummies:
        for j in adj_graph[i]: indegrees[j]-=1
        del adj_graph[i]

    for i in indegrees:
        if i in adj_graph and indegrees[i]==0 and i!=start:
            for j in adj_graph[i]: indegrees[j]-=1
            indegrees[i] = -1
            del adj_graph[i]
    
    return adj_graph, predecessors, start, end, indegrees


def OutputLP(graph, start, current):
    if(current == start): return str(start)
    return OutputLP(graph,start,graph[current][1]) + '->' + str(current)


I = input().split()
adj_graph,predecessors,start,end,indegrees = InputLP(I)
print(OutputLP(LongestPath(adj_graph,predecessors,start,end,indegrees),start,end))
```

    0 49 0->5:20 5->12:13 12->29:1 29->49:5 29->36:11 47->48:7 4->31:8 15->34:4 32->36:12 40->49:18 20->47:15 20->24:15 9->26:2 2->49:12 23->26:14 22->25:12 45->49:10 17->40:4 17->27:11 11->39:2 1->36:13 23->31:18 14->24:9 45->46:14 4->30:15 33->34:7 46->47:3 30->32:20 43->48:16 22->41:19 8->28:14 35->47:17 6->41:3 38->39:14 6->21:8 21->24:15 40->47:20 21->31:8 7->28:2 48->49:17 25->39:8 4->16:12 31->40:14 26->32:3 27->30:20 46->49:13 19->45:17 47->49:1 34->35:13 23->38:9 5->10:17 4->40:2 24->36:9 34->39:17 13->37:19 37->41:16 14->31:5 42->45:9 41->44:9 31->41:7 12->42:10 15->46:14 9->29:3 33->39:12 32->40:4 29->45:12 6->28:6 44->47:10 12->47:10 42->44:10 9->33:11 32->34:19 40->41:4 24->38:17 7->23:3 44->46:2 8->16:18 34->45:13 9->27:10 14->48:20 12->49:15 36->39:20 40->46:1 11->21:11 16->28:5 4->48:7 23->34:13 36->47:8 0->36:14 0->1:19 1->2:5 2->4:19 4->6:10 6->7:9 7->8:17 8->9:10 9->11:11 11->13:1 13->14:19 14->15:16 15->17:3 17->19:10 19->20:16 20->22:15 22->43:8
    263
    0->1->2->4->6->7->8->9->11->13->14->15->17->27->30->32->34->45->46->47->48->49



```

```
