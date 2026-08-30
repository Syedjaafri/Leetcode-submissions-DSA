class Solution:
    def isValid(self, s: str) -> bool:
        # using stack
        # storing the parathesis , in close as key and open as value , 
        # to match it with the further iteration , to become empyt stack

        stack = []

        closetoopen = {')':'(' , ']':'[' , '}':'{'}  # dictionary

        for c in s:
            if c in closetoopen:
                if stack and stack[-1] == closetoopen[c]:  # 1st , check stack contains anything , 2nd if last ele added in stack is equalt to the c
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:  # stack was"" empty
            return True
        else:
            return False