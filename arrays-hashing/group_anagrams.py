# Group Anagrams: https://leetcode.com/problems/group-anagrams/
# Pattern: arrays and hashing
# Time: O(n · k log k)   Space: O(n · k)   (n = words, k = longest word)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        group = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in group:
                group[key] = []

            group[key].append(word)
        
        return list(group.values())