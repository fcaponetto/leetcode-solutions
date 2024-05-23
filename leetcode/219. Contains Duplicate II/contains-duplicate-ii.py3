# 219. Contains Duplicate II (8/10/56360)
# Runtime: 451 ms (16.56%) Memory: 28.04 MB (71.08%) 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        if k == 0:
            return False

        for R in range(len(nums)):
            if nums[R] in window:
                return True

            if (R - L) >= k:
                window.remove(nums[L])
                L += 1

            window.add(nums[R])

        return False
        