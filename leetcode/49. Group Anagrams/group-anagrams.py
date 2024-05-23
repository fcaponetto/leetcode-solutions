# 49. Group Anagrams (12/26/56286)
# Runtime: 75 ms (50.91%) Memory: 15.52 MB (76.83%) 

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagrams = {}
        for word in strs:
            # Sorted() returns a sorted list of the specified iterable object.
            # It's not hashable, so cast to str()
            sorted_anagram = str(sorted(word))
            if sorted_anagram not in anagrams:
                anagrams[sorted_anagram] = [word]
            else:
                anagrams[sorted_anagram].append(word)

        return anagrams.values()