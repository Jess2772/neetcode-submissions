class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        # also, best case is you want the smaller intervals anyways.
        res = [intervals[0]]
        counter = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                counter += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        
        return counter