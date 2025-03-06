# 15. 3Sum (7/28/57149)
# Runtime: 390 ms (92.78%) Memory: 20.69 MB (63.56%) 

# Time Complexity O(n log n) + O(n^2)
# Space Complexity O(1)

# [-1,0,1,2,-1,-4]
# Sorted
# [-4,-1,-1,0,1,1,2]
#     L         R

# num[i] + num[j] = -num[k]
# -2 -1 + 2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ret = []

        def twoSum(start, target):
            L, R = start, len(nums) - 1
            while L < R:
                if nums[R] + nums[L] > target:
                    R -= 1
                elif nums[R] + nums[L] < target:
                    L += 1
                else:
                    # note nums[i] is -target
                    ret.append([nums[R], nums[L], nums[i]])
                    
                    L += 1
                    R -= 1
                    # increment two index while skipping to avoid same triplets
                    # [-5, -2, -2, 0, 2, 2, 3, 3, 5] -> [-5, 2, 3]
                    #                 L        R     -> whitout skipping we would get again [-5, 2, 3]

                    while L < R and nums[L] == nums[L-1]:
                        L += 1

                    while L < R and nums[R] == nums[R+1]:
                        R -= 1


        for i in range(len(nums)):
            # If we are in the positive side, we cannot find any negative number
            # that would make the sum equal to zero
            if nums[i] > 0:
                break

            # Skip duplicate triplets
            # E.g [-3,-3,0,1,2,3,4] 
            # first -3 -> [-3, 0, 3], [-3, 1, 2]
            # second -3 leads to the same results
            if i > 0 and nums[i] == nums[i-1]:
                continue
            

            # We need to find num[i] + num[j] + num[k] = 0 -> num[j] + num[k] = -num[i]
            target = -nums[i]
            # Two sums
            twoSum(i+1, target)

        
        return ret
        