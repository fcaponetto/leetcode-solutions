# 70. Climbing Stairs (8/5/56546)
# Runtime: 25 ms (90.39%) Memory: 16.49 MB (38.31%) 

# n = 3 cache = [3,2,1]

class Solution:
    def climbStairs(self, n: int) -> int:
        
        def memoization(stepsSoFar, cache):
            if stepsSoFar > n:
                return 0
            if stepsSoFar == n:
                return 1

            if stepsSoFar in cache:
                return cache[stepsSoFar]

            cache[stepsSoFar] = memoization(stepsSoFar + 1, cache) + memoization(stepsSoFar + 2,cache)

            return cache[stepsSoFar]

        cache = {} # improved
        # cache = [None] * n
        return memoization(0, cache)