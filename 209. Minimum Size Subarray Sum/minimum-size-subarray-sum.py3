# 209. Minimum Size Subarray Sum (03/10/56363)
# Runtime: 185 ms (5.13%) Memory: 30.20 MB (54.58%) 

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
                length = min(length, R - L + 1)
                sumOfNums -= nums[L]
                L += 1
        return length % (len(nums) + 1)

        