from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using defaultdict to avoid key errors
        anagrams = defaultdict(list)

        for string in strs:
            # Initialize a list with 26 zeros for each letter in the alphabet
            letters = [0] * 26
            for letter in string:
                # Update the count for each letter in the string
                letters[ord(letter) - ord('a')] += 1
            
            # Use the tuple of counts as the key in the map
            anagrams[tuple(letters)].append(string)
        
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())
