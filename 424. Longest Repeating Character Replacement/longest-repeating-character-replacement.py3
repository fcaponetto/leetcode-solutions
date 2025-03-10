# 424. Longest Repeating Character Replacement (7/10/57160)
# Runtime: 115 ms (73.44%) Memory: 18.08 MB (25.32%) 

# Time complexity O(n)
# Space complexity O(n)

# 1. Given a window (contiguous char), calculate the frequency of each char 
# 2. Int he given window, we want to substitute the less frequent up to k
# 3. When we run out out substitution, we shrink the window
# 4. Maintain the max lenght as the max window size encountered

# k = 2
# ADACDB
#    R
# ^^^^
# count = {A:2, D:1}
# window - max freq < 2
#   4    -     2    < 2 (no)
# max lenght = 4
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        L = 0
        max_freq_w = 0
        length = 0
        count_freq = {}

        for R in range(len(s)):
            if s[R] not in count_freq:
                count_freq[s[R]] = 0
            count_freq[s[R]] += 1

            max_freq_w = max(max_freq_w, count_freq[s[R]])

            if (R - L + 1) - max_freq_w > k:
                count_freq[s[L]] -= 1
                L +=1

            length = max(length, R - L + 1)

        return length
