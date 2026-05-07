from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        counts = defaultdict(int)
        buckets = [[] for i in range (len(nums) + 1)]
        res = []

        for n in nums:
            counts[n] += 1

        for num in counts:
            buckets[counts[num]].append(num)

        for i in range (len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if k == 0:
                    return res
                res.append(num)
                k -= 1
        return res

            
        