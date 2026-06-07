"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        N = len(intervals)
        res = 1

        intervals.sort(key = lambda x: x.end)

        rooms = [[] for i in range (N + 1)]

        rooms[1].append(intervals[0])

        prev_start, prev_end = intervals[0].start, intervals[0].end

        for i in range (1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if start >= prev_end:
                rooms[res].append(intervals[i])
            else:
                added = False
                for j in range (1, N + 1):
                    if rooms[j] and start >= rooms[j][-1].end:
                        rooms[j].append(intervals[j])
                        added = True
                        break
                if not added:
                    res += 1
                    rooms[res].append(intervals[i])
            prev_start, prev_end = start, end
        
        return res
                
                        



        


        