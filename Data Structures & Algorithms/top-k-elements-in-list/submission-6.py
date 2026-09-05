from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # mapping = {}
        # for num in nums:
        #     mapping[num] = 1 + mapping.get(num, 0)

        # counts_arr = []
        # for num, count in mapping.items():
        #     # counts_arr.append([count, num])
        #     counts_arr.append([-count, num]) # to max-heapify
        # # counts_arr.sort() n*logn
        # # res = []
        # # for item in counts_arr[-k:]:
        # #     res.append(item[-1])

        # res = []
        # heapify(counts_arr) # O(m) where m, is the distinct number of elements
        # for i in range(0, k):
        #     res.append(heappop(counts_arr)[1]) # O(logm)
        # return res

    # Bucket sort
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for num, count in counts.items():
            buckets[count].append(num)
        
        res = []
        while len(res) < k:
            res.extend(buckets.pop())
        return res
            