# 5. Longest Palindromic Substring (8/24/57384)
# Runtime: 331 ms (48.19%) Memory: 18.03 MB (22.63%) 


# The key is to start from the center. But which center?
# A solution could be to use the "standard" two-pointers approach
# by starting from each character and expanding outwards.

# Doing this way we need consider that when the lenght is even, the start
# has to be +1

# Odd-case
# xabay -> aba
#   ^
#   L     <- both start from the center
#   R     <- both start from the center

# Even-case
# bb
# LR      <- R has to start one position ahead

class Solution:
    def longestPalindrome(self, s: str) -> str:
        startIdx = 0
        maxLength = 0

        def expand(L, R):
            # This allows the inner function to modify the outer function's variables
            nonlocal startIdx, maxLength

            # if within range and palindrome
            while L >= 0 and R < len(s) and s[L] == s[R]:
                # update if longest
                current_length = R - L + 1
                if current_length > maxLength:
                    startIdx = L
                    maxLength = current_length
                L -= 1
                R += 1

        for i in range(len(s)):
            # odd-case
            L, R = i, i
            expand(L, R)

            # even-case
            L, R = i, i+1
            expand(L, R)

        
        return s[startIdx : startIdx + maxLength]