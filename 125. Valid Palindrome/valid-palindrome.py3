# 125. Valid Palindrome (6/29/57034)
# Runtime: 7 ms (76.10%) Memory: 18.20 MB (39.19%) 

# A man, a plan, a canal: Panama
#   L                         
#                             R
# We don't want compare R with the 'space' character
# So we keep going
class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1

        while L < R:
            if not s[L].isalnum():
                L += 1
            elif not s[R].isalnum():
                R -= 1
            else:
                if s[L].lower() != s[R].lower():
                    return False
                
                L += 1
                R -= 1

        return True
        