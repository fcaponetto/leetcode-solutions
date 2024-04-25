# 242. Valid Anagram (11/24/56286)
# Runtime: 26 ms (75.35%) Memory: 12.88 MB (37.17%) 

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        