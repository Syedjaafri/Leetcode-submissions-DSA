class Solution:
    def isValid(self, s: str) -> bool:
        # using stack

        stack = []

        closetoopen = {')':'(' , ']':'[' , '}':'{'}  # dictionary

        for c in s:
            if c in closetoopen:
                if stack and stack[-1] == closetoopen[c]:  # 1st , check stack contains anything , 2nd if last ele addedi n stack is equalt to the c
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:  # stack was"" empty
            return True
        else:
            return False