# 561. Array Partition (9/4/55796)
# Runtime: 241 ms (0.28%) Memory: 19.12 MB (86.10%) 

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) < 2:
            return 0
        
        i = 0
        j = len(nums) - 2
        
        sum = 0
        while (j-i) > 0:
            sum += nums[i]
            sum += nums[j]
            i += 2
            j -= 2

        # if we have a odd pairs, add the missing one
        if (len(nums)/2) % 2 == 1:
            sum += nums[i]
            
        return sum
            