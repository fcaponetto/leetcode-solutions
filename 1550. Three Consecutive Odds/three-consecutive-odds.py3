# 1550. Three Consecutive Odds (8/23/57329)
# Runtime: 0 ms (99.68%) Memory: 17.72 MB (70.13%) 

# Time Complexity: O(n)
# Space Complexity O(1)

# Easy, just iterate over the array and count the consegutive occurences

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n_odds = 0
        
        for x in arr:
            if (x % 2 == 1):
                n_odds += 1
            else:
                n_odds = 0

            if n_odds == 3:
                return True

        return False