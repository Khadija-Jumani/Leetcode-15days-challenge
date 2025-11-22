class Solution:
    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If it's a closing bracket
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket
                stack.append(char)

        return len(stack) == 0
