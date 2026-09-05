class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs:
            letters = [0]*26
            for c in str:
                index = ord(c) - ord('a')
                letters[index]+=1
            if tuple(letters) in map:
                map[tuple(letters)].append(str)
            else:
                map[tuple(letters)] = [str]
        return map.values()
            