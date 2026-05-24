"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}
        
        def dfs(curNode):
            if curNode: 
                nodes[curNode.val] = nodes.get(curNode.val, Node(curNode.val))
                for neighborNode in curNode.neighbors:
                    if neighborNode.val not in nodes:
                        newNode = dfs(neighborNode)
                    else:
                        newNode = nodes[neighborNode.val]
                    nodes[curNode.val].neighbors.append(newNode)
                
                return nodes[curNode.val]

        return dfs(node)

        