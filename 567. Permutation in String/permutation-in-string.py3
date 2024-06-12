# 567. Permutation in String (26/04/56418)
# Runtime: 52 ms (95.00%) Memory: 16.52 MB (86.02%) 

# eidbaooo
#  L
#   R

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #  must have same character frequencies, if one is permutation of another
        def charFrequencies(ss, data):
            for s in ss:
                if s in data:
                    data[s] += 1
                else:
                    data[s] = 1

        chars = {}
        charFrequencies(s1, chars)

        L = 0
        R = len(s1)
        charsSub = {}
        
        for R in range(len(s2)):
            if s2[R] in charsSub:
                charsSub[s2[R]] += 1
            else:
                charsSub[s2[R]] = 1

            if R - L + 1 == len(s1):
                if charsSub == chars:
                    return True

                charsSub[s2[L]] -= 1
                if charsSub[s2[L]] == 0:
                    del charsSub[s2[L]]
                L += 1
                    

        return False
        