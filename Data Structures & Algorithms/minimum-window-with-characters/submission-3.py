class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # optimized approach , 
        # by creating 2 dictionaries , 
        # if have == need , one ans
        # if the if the len(t) is equal to the length of our have (window)
        # then we will get 1 possible solution
        # to find the exact minimum solution 
        # we traverse through the loop 

     #STEP 1 : THE INITIALIZATIONS |  # the 2 dictionaries
        countT , window = {} , {}  # window dict stores the each characters in the window

        for c in t:  # count has the characters of t 
            countT[c] = 1 +  countT.get(c , 0)

        # initialize have and need , if they're equal we found an possible min window substring

        have = 0
        need = len(countT) # this countT has the count of each char in string "t""
        res = [-1 , -1]  # output string's indices

        reslen = float("infinity")

# STEP 2: POINTERS AND COUNTING
    
        left = 0

        for right in range(len(s)):
            r = s[right]  # storing each in r(shortcut / simplicity)
            window[r] = 1 + window.get(r , 0)

# STEP 3 : OPERATION , FINDING A MINIMUMM WINDOW SUBSTRING

        # checking the characters in the window[r] == countT[r]

            if r in countT and window[r] == countT[r]:
                have += 1   # s having the char of t , so add the have 

        # while loop , if have is equal to the need , found 1 poss solution

            while have == need:
                if right - left+1 < reslen:# only win size is less than the res len
                #updating the res and it's len , since found one poss ans
                    res = [left , right]
                    reslen = right - left+1

                # now the reslen was updated with the prev win size

                # if win size is not less than the reslen , we remove/pop the left pointer

                window[s[left]] -= 1 #popping out

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -=1 # decrementing the have
                left += 1

        left , right = res

        return s[left:right+ 1] if reslen != float("infinity")  else ""



        

        
