# Valid Anagram: https://leetcode.com/problems/valid-anagram/
# Pattern: arrays and hashing
# Time: O(n)   Space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not isinstance (s, str) or not isinstance (t, str):
            raise TypeError(" Input must be string.") 

        count_s = {}
        count_t = {}

        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1  

        return count_s == count_t

# Version 2: Counter 

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not isinstance (s and t, str):
            raise TypeError(" Input must be string.") 
        
        if len(s) != len(t):
            return False   

        return Counter(s) == Counter(t)
             
        