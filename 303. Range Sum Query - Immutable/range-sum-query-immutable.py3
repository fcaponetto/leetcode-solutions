# 303. Range Sum Query - Immutable (23/09/56371)
# Runtime: 53 ms (95.00%) Memory: 20.07 MB (51.63%) 

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        totalSoFar = 0
        for num in nums:
            totalSoFar += num
            self.prefix.append(totalSoFar)

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)