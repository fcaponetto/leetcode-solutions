# 739. Daily Temperatures (8/28/56524)
# Runtime: 915 ms (20.66%) Memory: 30.57 MB (70.75%) 

# [73,69,68,70,70]
#     i
#           j               
# [73,69,68,70] # the idea is to build a monotonic stack
# [,,1,]

# Time complexity O(n)
# Space complexity O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair{temperature, idx}
        stack.append((temperatures[0], 0))

        for i in range(1, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                idx = stack[-1][1]
                res[idx] = i-idx
                stack.pop()

            stack.append((temperatures[i], i))

        return res
        