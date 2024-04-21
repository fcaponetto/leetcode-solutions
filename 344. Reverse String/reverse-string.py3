# 344. Reverse String (7/12/55796)
# Runtime: 181 ms (4.29%) Memory: 20.49 MB (94.69%) 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # represents first pointer
        i = 0;

        # represents second pointer
        j = len(s)-1
        
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1