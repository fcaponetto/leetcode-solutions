# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold (4/28/56366)
# Runtime: 432 ms (81.42%) Memory: 29.78 MB (65.26%) 

# [2,2,2,2,5,5,5,8]
#            L
#            R
# average/3

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        numOfSub = 0
        currSum = 0

        for R in range(len(arr)):
            currSum += arr[R]
            if R - L + 1 == k:
                if currSum/k >= threshold:
                    numOfSub += 1
                currSum -= arr[L]
                L +=1
        return numOfSub

            