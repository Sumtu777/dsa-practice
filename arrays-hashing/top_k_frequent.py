# Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/
# Pattern: arrays and hashing
# Time: O(n log n) worst case   Space: O(n)

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_count = sorted(count.items(), key = lambda p:p[1], reverse = True)

        top_count = sorted_count[:k]

        return [i[0] for i in top_count]