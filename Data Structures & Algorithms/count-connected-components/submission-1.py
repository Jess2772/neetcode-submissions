from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # just try to reach as many components as you can. mark the nodes as visited. 
        # keep looping until all are visited
        #visiting versus visited
        res = 0
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(node):
            if node in visited:
                return 1

            visited.add(node)

            for neighbour in adj[node]:
                dfs(neighbour)


        for i in range (n):
            if i not in visited:
                dfs(i)
                res += 1

        return res





        
        