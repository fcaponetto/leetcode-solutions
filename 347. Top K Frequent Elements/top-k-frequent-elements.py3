# 347. Top K Frequent Elements (4/17/57097)
# Runtime: 10 ms (22.91%) Memory: 21.10 MB (82.67%) 

# [1,1,1,2,2,3]

# 1. define a map < value, occurences> and determine the occurences.
# 2. copy the keys and values to a "struct" iteratio
# 2. sort the array in an descrending order using as the 'num of occurrences' as sorting criteria
# 3. retrieve the first k elments

class Value:
    def __init__(self, value, occurrences):
        self.value = value
        self.occurrences = occurrences

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elems = {}

        for elem in nums:
            if elem in elems:
                elems[elem] += 1
            else:
                elems[elem] = 1

        sorted_elements = []

        for elem in elems:
            sorted_elements.append(Value(elem, elems[elem]))

        sorted_elements.sort(key=lambda x: x.occurrences, reverse=True)

        # ret = sorted_elements[:k]
        return [elem.value for elem in sorted_elements[:k]]

