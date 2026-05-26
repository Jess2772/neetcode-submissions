from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # must be connected
        # cannot be any cycles
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def isConnected(cur, prev):
            if cur in visited:
                return False
            
            visited.add(cur)
            for neighbour in adj[cur]:
                if neighbour == prev:
                    continue
                if not isConnected(neighbour, cur):
                    return False

            return True

        return isConnected(0, -1) and len(visited) == n