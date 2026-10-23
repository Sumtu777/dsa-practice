# Contains Duplicate: https://leetcode.com/problems/contains-duplicate/
# Pattern: arrays and hashing
# Time: O(n) average   Space: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
            
        