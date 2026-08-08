class Solution:
    def isPalindrome(self, s: str) -> bool:

        # USING BRUTE FORCE METHOD (TWO POINTER)

        #initiating 2 pointer
        l = 0 
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphanum(s[l]):
                l = l + 1  #increment when l's character is not alpha num 
            while r > l and not self.alphanum(s[r]):
                r = r - 1  # decrement when r's character is not alpha num

            # actual comparision

            if s[l].lower() != s[r].lower():
                return False

            l = l + 1
            r  = r - 1

        return True

        # helper function
        # to ignore the non-alphanuerics characters on both pointers
        # ord() built in func , will extract the ascii val of a character 

    def alphanum(self , char): # return false if the char is not alphanum
        return (ord('A') <= ord(char) <= ord('Z')or
                ord('a') <= ord(char) <= ord('z')or
                ord('0') <= ord(char) <= ord('9'))
        