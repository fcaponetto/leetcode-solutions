# 128. Longest Consecutive Sequence (1/15/57352)
# Runtime: 46 ms (71.69%) Memory: 34.24 MB (48.77%) 

# Time Complexity O(n)
# Space Complecity O(n)


# The sequence starts from a given element if the previous is the previous is not in the list
# given x -> if x -1 is not present in list so it's the start of the sequence

# Note: duplicate are part of the sequence
# In [0,1,1,2] the longest consecutive sequence is [0,1,2] with length 3.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums) # O(n)

        best = 0
        for x in nums:
            if x - 1 not in nums:
                length = 1
                while (x + length) in nums:
                    length += 1
                best = max(best, length)

        return best