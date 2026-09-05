class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for num in nums:
            mapping[num] = 1 + mapping.get(num, 0)

        counts_arr = []
        for num, count in mapping.items():
            counts_arr.append([count, num])
        counts_arr.sort()

        res = []
        for item in counts_arr[-k:]:
            res.append(item[-1])
        
        return res