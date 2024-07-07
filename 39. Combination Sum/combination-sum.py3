# 39. Combination Sum (4/7/56486)
# Runtime: 64 ms (11.57%) Memory: 16.59 MB (51.94%) 

# Time Complexity O(2^n * k)
# Space Complexity O(n)

class Solution:
    def helper(self, i, candidates, target, curComb, combinations):
        if sum(curComb) == target:
            combinations.append(curComb.copy())
            return

        if i >= len(candidates) or sum(curComb) > target:
            return

        # branch where we include candidates[i]
        curComb.append(candidates[i])
        # i instead of i+1 for including current element multiple times
        self.helper(i, candidates, target, curComb, combinations)
        curComb.pop()

        # branch where we don't include candidates[i]
        self.helper(i+1, candidates, target, curComb, combinations)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curComb = []
        combinations = []
        self.helper(0, candidates, target, curComb, combinations)
        return combinations