# 209. Minimum Size Subarray Sum (9/30/56363)
# Runtime: 189 ms (4.54%) Memory: 30.10 MB (76.76%) 

# [2,3,1,2,4,3] 7
#          L
#            R

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums) + 1
        sumOfNums = 0
        L = 0

        for R in range(len(nums)):
            sumOfNums += nums[R]
            while sumOfNums >= target:
                length = min(R - L + 1, length)
                sumOfNums -= nums[L]
                L += 1
        return length if length != len(nums) + 1 else 0

        