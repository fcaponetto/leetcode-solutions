# 167. Two Sum II - Input Array Is Sorted (4/1/57338)
# Runtime: 7 ms (20.03%) Memory: 18.76 MB (0.00%) 


# We are looking for two elements
# Data structure is an array
# The array is sorted
# Two index

# [2,7,11,15]
#  L       R

# a[L] + a[R] > target -> R--
# a[L] + a[R] < target -> L++

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                break
        
        return [L+1, R+1]