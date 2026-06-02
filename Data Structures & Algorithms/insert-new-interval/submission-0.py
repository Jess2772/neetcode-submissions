class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        res = []

        cur = 0
        while cur < N and newInterval[0] > intervals[cur][1]:
            res.append(intervals[cur])
            cur += 1

        res.append(newInterval)

        # starting from cur ... N, do normal merge interval

        for i in range (cur, N):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][0] = min(intervals[i][0], res[-1][0])
                res[-1][1] = max(intervals[i][1], res[-1][1])

        return res
        