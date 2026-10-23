   # Two Sum: https://leetcode.com/problems/two-sum/
   # Pattern: arrays and hashing
   # Time: O(n) avarage   Space: O(n) avarage

class Solution:
    def twoSum(self, nums: list[int], target: int):
        seen = {}

        for i, num in enumerate (nums):
            possible_num = target - num
            
            if possible_num in seen:
                return [seen[possible_num], i]

            else:
                seen[num] = i
    
        return[]