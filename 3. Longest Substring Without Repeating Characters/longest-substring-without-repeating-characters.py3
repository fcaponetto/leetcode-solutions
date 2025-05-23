# 3. Longest Substring Without Repeating Characters (1/20/57363)
# Runtime: 15 ms (76.89%) Memory: 17.78 MB (69.85%) 

# Time complexity O(n)
# Space complexity O(n)


# Use a variable sliding window - reset the window if the character is already part of the window
# return the max window length

# pwwkew
# pw
#   w

# dvdf
#  vdf
# dv
#   d

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        length = 0
        L = 0

        if not s:
            return 0

        for R in range(len(s)):
            # if element in set, shrink the window 
            # by incrementing the l pointer until 
            # the window no longer contains any duplicates.
            while s[R] in window:
                window.remove(s[L])
                L += 1

            window.add(s[R])
            length = max (length, len(window))

        return length
        