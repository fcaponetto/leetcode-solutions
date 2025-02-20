# 238. Product of Array Except Self (4/19/57111)
# Runtime: 11 ms (94.37%) Memory: 23.15 MB (87.89%) 

# Time complexity O(n)
# Space complexity O(1) 

# Case 1 normal case:
# [1,2,3,4]
# 1. Multiply all elements by first iteration
# 2. Iterate again the array and divide the i-th element from the sum

# Sum = 1 * 2 * 3 * 4 = 24
# 24/1=24, 24/2=12, 24/3=8, 24/4=6

# Case 2 normal case with negative still works:
# [-1,1,1,-3,3]
# Sum = -1 * 1 * 1 * -3 * 3 = 9
# 9/-1=-9, 9/1=9, 9/1=9, 9/-3=-3, 9/3=3

# Case 3 one zero:
# [-1,1,0,-3,3]
# Sum = -1 * 1 * -3 * 3 = 9
# 0/-1=0, 0/1=0, 9, 0/-3=-0, 0/3=0

# Case 3 double zero:
# [0,1,0,-3,3]
# With double zero everything would be zero

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        totSum = 1
        single_zero = False
        double_zero = False
        zero_idx = -1
        for i in range(len(nums)):
            if nums[i] != 0 :
                totSum *= nums[i]
            else:
                if not single_zero:
                    single_zero = True
                    zero_idx = i
                else:
                    double_zero = True
                    break # More than one zero, all elements will be zero

        ret = []
        # If zero is present, result is all zeros...
        if single_zero:
            ret = [0] * len(nums)
            # However, if single zero, only that index gets totSum, rest are 0
            if not double_zero:
                ret[zero_idx] = totSum
            
            return ret

        for n in nums:
                ret.append(totSum // n)

        return ret