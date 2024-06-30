# 78. Subsets (25/03/56467)
# Runtime: 36 ms (57.76%) Memory: 16.66 MB (61.26%) 

# subsets [[1, 2, 3], [1,2], [1, 3], ....]
# curSet [1]

class Solution:
    def constructSubset(self, i, nums, subsets, curSet):
        if i == len(nums):
            subsets.append(curSet.copy())
            return

        # include num at i-th pos
        curSet.append(nums[i])
        self.constructSubset(i+1, nums, subsets, curSet)
        curSet.pop()

        # don't # include num at i-th pos
        self.constructSubset(i+1, nums, subsets, curSet)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curSet = []
        self.constructSubset(0, nums, subsets, curSet)
        print(subsets)
        return subsets