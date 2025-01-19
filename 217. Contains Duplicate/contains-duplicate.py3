# 217. Contains Duplicate (12/31/57022)
# Runtime: 3 ms (93.22%) Memory: 31.65 MB (14.71%) 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        processed = set()

        for num in nums:
            if num in processed:
                return True
            processed.add(num)

        return False