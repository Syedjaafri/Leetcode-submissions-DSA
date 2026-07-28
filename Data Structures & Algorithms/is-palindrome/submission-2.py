class Solution:
    def isPalindrome(self, s: str) -> bool:

        #brute force(non using of two pointer , using built-in functions)
        newstr = ""

        for char in s:
            if char.isalnum():
                newstr = newstr + char.lower()
        return newstr == newstr[::-1]
