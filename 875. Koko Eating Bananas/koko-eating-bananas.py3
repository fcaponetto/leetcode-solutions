# 875. Koko Eating Bananas (11/28/56293)
# Runtime: 262 ms (59.40%) Memory: 18.20 MB (43.09%) 

# Time Complexity O(log(max(n)) * n) | n = piles
# Space Complexity O(1)

class Solution(object):
    # The maximum possiblle k (number of bananas-per-hour) would be the max integer 
    # within the piles.
    # Eg, piles = [3,6,7,11] the max bananas shw could eat in one hour would be
    # k = 11, but it will take only 4 hours and she actually can slow down since 
    # the guard will return in 8 hours.Thus, while aiming to eat 11 bananas in the
    # first 3 piles the (3, 6, 7) she will spend most of the time not eating.
    #
    # We are interested to the minimum (number of bananas-per-hour) such that Koko can 
    # eat all the available bananas.
    # The lowest possible is 1, but it might exeed the hours...

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
                hours_to_complete += math.ceil(bananas_in_pile / mid)

            # If the total hours are more than h, we need a higher speed
            if hours_to_complete > h:
                low = mid + 1
             # If we can do it in less or equal hours, try a smaller speed 
             # to see if there's a more efficient rate
            else:
                high = mid - 1

        # After completing the binary search loop, the value of `low` becomes
        # the minimum banana-eating speed `k` at which Koko can consume all the
        # bananas across the piles within the given time limit `h` hours. 
        # If the hours exceed `h`, it indicates that `mid` is too slow, prompting 
        # an increase in the lower bound `low` to `mid + 1`.
        # Conversely, if Koko can finish eating in `h` hours or less at speed `mid`,
        # we explore potentially lower speeds by adjusting the upper bound `high`
        # to `mid - 1`. The loop exits when `low` surpasses `high`, at which point
        # `low` is positioned at the smallest speed just beyond the largest confirmed
        # "too slow" speed, ensuring it is the minimal speed at which Koko can
        # finish eating all bananas within `h` hours without exceeding the time
        # limit.
        return low


        