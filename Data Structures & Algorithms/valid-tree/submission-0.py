from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # must be connected
        # cannot be any cycles
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def isConnected(node):
            visited = set()
            stack = [(node, -1)]

            while stack:
                cur, parent = stack.pop()
                if cur in visited:
                    return False
                visited.add(cur)
                for neighbour in adj[cur]:
                    if parent != neighbour:
                        stack.append((neighbour, cur))

            return len(visited) == n

        return isConnected(0)