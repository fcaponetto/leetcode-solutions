# 50. Pow(x, n) (5/19/57329)
# Runtime: 0 ms (99.18%) Memory: 17.72 MB (63.68%) 

# Time complexity: O(log n) - we divide at each iteration
# Space complexity: O(1)

# binary exponentiation algorithm
# x^n = x(2/n)^2

# So, resursivily:
# n = even -> x^n = x(2/n)^2
# n = odd ->  x^n = x * x(2/n)^2

#For example, with 3^13:

# 3^13 = 3 × (3^6)^2 (applying the odd formula)
# Now we need 3^6, which is (3^3)^2 (applying the even formula)
# Now we need 3^3, which is 3 × (3^1)^2 (applying the odd formula)
# Now we need 3^1, which is 3 (base case)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        
        # handle negative case
        isNegative = False
        if n < 0:
            isNegative = True
            n = abs(n)

        while n > 0:
            # if n odd, multitply result * base 
            # note: (it might be the last operation)
            if n % 2 == 1:
                result *= x
            
            # divide exponent by 2
            n //= 2
            
            # squaring the base
            x *= x

        # if the exponent was negative, just use the reciprocal
        if isNegative:
            result = 1 / result

        return result