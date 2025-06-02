# 268. Missing Number (6/10/57390)
# Runtime: 0 ms (94.92%) Memory: 18.48 MB (92.00%) 

# Time Complexity O(n log n)
# Space Complexity O(1)

# A simple solution could be to sort the array
# then iterate while checking if nums[i] - i >= 1

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()

#         for i in range(len(nums)):
#             if nums[i] - i >= 1:
#                 return i
#         return len(nums)


# Time Complexity O(n)
# Space Complexity O(1)

# A better solution is to use math
# sum of n elements = n*(n+1)/2
# sum(n) - sum(nums) = missing number

# [3,0,1]
# sumN = 3*4/2 = 6
# sumNums= (3+0+1) = 4
# missing = 6 - 4 = 2

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumN = (n * (n + 1)) // 2
        sumNums = sum(nums)

        missing = sumN - sumNums
        return missing

