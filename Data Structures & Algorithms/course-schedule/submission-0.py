from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {}
        for i in range (numCourses):
            indegree[i] = 0

        prereqs = defaultdict(list)
        numVisited = 0

        for a, b in prerequisites:
            indegree[a] += 1
            prereqs[b].append(a)
        
        q = deque()
        for n in indegree:
            if indegree[n] == 0:
                q.append(n)

        while q:
            n = q.popleft()
            numVisited += 1
            for a in prereqs[n]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    q.append(a)

        return numVisited == numCourses 

                   
