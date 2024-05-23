# 875. Koko Eating Bananas (11/9/56293)
# Runtime: 480 ms (18.78%) Memory: 12.98 MB (28.58%) 

class Solution(object):
    # The maximum k (number of bananas-per-hour) would be the max integer within the piles
    # Eg, piles = [3,6,7,11] the max bananas shw could eat in one hour would be
    # k = 11, but it will take only 4 hours and she actually can slow down since 
    # the guard will return in 8 hours.Thus, while aiming to eat 11 bananas in the
    # first 3 piles the (3, 6, 7) she will spend most of the time not eating.
    #
    # We are interested to the minimum (number of bananas-per-hour) such that Koko can 
    # eat all the available bananas.

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        # The range would be from the min and max.
        # The goal is to find the right value among the min and max
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2 # floor division

            hours_to_complete = 0
            for bananas_in_pile in piles:
                hours_to_complete += math.ceil(bananas_in_pile / float(mid))

            if hours_to_complete > h:
                low = mid + 1
            else:
                high = mid - 1

        return low


        