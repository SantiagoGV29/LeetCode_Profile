class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        distances = [0] * n  
        tree = [[] for _ in range(n)]
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])  
        for num,t in enumerate(tree):
            tree[num] = sorted(t)    
        for i in range(n):
            distances[i] = self.distance(i, tree, n)
        return distances
    
    def distance(self, i, tree, n):
        distance = 0
        for j in range (n):
            if j == i:
                continue
            else:
                distance += self.dist(i, j, tree,set())
        return distance
                    
    def dist(self, S, T, tree,memo):
        if T in tree[S]:
            return 1
        else:
            for child in tree[S]:
                if child not in memo:
                    memo.add(S)
                    memo.add(child)
                    return 1 + self.dist(child, T, tree,memo)
        return 1
# Not optimized, but works
from collections import deque

class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        distances = [0] * n  
        tree = {}
        for e in range (n):
            tree[e] = []
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])           
        for i in range(n):
            sum = self.dijkstra(tree,i)
            for s in sum:
                distances[i] += sum[s]            
        return distances

    def dijkstra(self, graph, start):
        distances = {node: float('inf') for node in graph}
        
        distances[start] = 0
        queue = deque([start])

        while queue:
            current_node = queue.popleft()

            for neighbor in graph[current_node]:
                if distances[neighbor] == float('inf'):
                    distances[neighbor] = distances[current_node] + 1
                    queue.append(neighbor)

        return distances

# Optimized
class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        tree = {}
        for e in range (n):
            tree[e] = []
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])  
            
        distances = [0] * n  
        nodes = [1]*n
        self.First = 0
        def Count(source,root,level):
            NumNode = 1
            for node in tree[source]:
                if node != root:
                    NumNode += Count(node,source, level+1)
                    self.First += (level + 1)
            nodes[source] = NumNode
            return NumNode
        Count(0,-1,0)
        def TraverseDfs(source,root,NumNodes):
            distances[source] = NumNodes
            for node in tree[source]:
                if node !=  root:
                    Next = NumNodes + (n-nodes[node]) - nodes[node]
                    TraverseDfs(node,source,Next)
        TraverseDfs(0,-1,self.First)
        return distances      