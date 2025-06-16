# 139. Word Break (8/31/57428)
# Runtime: 3 ms (65.96%) Memory: 18.12 MB (7.00%) 

# Time Complexity without cache O(2^n), where n = LENGTH OF STRING s
# Time Complexity with cache O(n^2)
# Space Complexity O(m)

# - At position i, we try all possible endings j (from i to n-1)
# - For each valid word found, we make a recursive call
# - In worst case: every substring is a valid word -> eg s=abc wordList=[a,b,c]
#
# T(n) = T(n-1) + T(n-2) + T(n-3) + ... + T(1) + T(0)
# This gives us T(n) = O(2^n)


# Example:
# s = "aaaaaaa", wordDict = ["aaaa", "aaa"]
#
#                    findWords(0)
#                    "aaaaaaa"
#                        |
#               +--------+--------+
#               |                 |
#         findWords(3)      findWords(4)
#         "aaaa" (aaa)      "aaa" (aaaa)
#              |                 |
#     +--------+--------+        |
#     |                 |        |
# findWords(6)    findWords(7)   findWords(7)
# "a" (aaa)       i==len(s)      i==len(s)
#     |               |              |
#     X               V              V

# s = # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

# cache needed in the above case

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        # dictionry for cache
        cache = {}
        def dfs(i):
            if i == len(s):
                return True

            if i in cache:
                return cache[i]
            
            for j in range(i, len(s)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        cache[i] = True
                        return True

            cache[i] = False
            return False
        
        return dfs(0)