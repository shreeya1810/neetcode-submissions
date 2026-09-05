class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for string in strs:
            alphabet = [0] * 26
            for letter in string:
                alphabet[ord(letter) - ord('a')] += 1
            alphabet = str(alphabet)
            if alphabet not in mapping:
                mapping[alphabet] = [string]
            else:
                mapping[alphabet].append(string)
        return list(mapping.values())
            