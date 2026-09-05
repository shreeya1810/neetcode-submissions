class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        map = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            map[value].append(key)
        
        res = []
        for i in range(len(map) - 1, 0, -1):
            for num in map[i]:
                res.append(num)
            if len(res) == k:
                return res
