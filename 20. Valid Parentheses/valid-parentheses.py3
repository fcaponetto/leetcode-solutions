# 20. Valid Parentheses (10/20/57447)
# Runtime: 0 ms (95.97%) Memory: 17.66 MB (86.26%) 

# Time complexity O(n)
# Space Complexity O(n)

# ([])

# stack i=2
# [
# (

# when a closed pharentesis is encountered, chech the top of the stack
# return true if the stack is empty


# ])
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def checkParenthesis(p, opening, closing):
            if p == closing:
                # check if we can close it properly
                if len(stack) > 0 and stack.pop() == opening:
                    return True

            return False

        for p in s:
            if (checkParenthesis(p, '(', ')') or 
                checkParenthesis(p, '[', ']') or
                checkParenthesis(p, '{', '}')):
                continue

            stack.append(p)

        return len(stack) == 0



