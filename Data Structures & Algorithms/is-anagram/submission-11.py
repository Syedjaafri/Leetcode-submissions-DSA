class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #   BRUTE FORCE METHOD

        # checking length 
        if len(s) != len(t):
            return False
        
        # for checking all the characters in both strings are same 

        # counting each character in both the strings and checking if they are same

        # creating dictionaries/ hashmaps
        counts , countt  = {} , {}
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i] , 0) # counts the characters in s
            countt[t[i]] = 1 + countt.get(t[i] , 0)  # counts characters in t

        for j in counts:
            if counts[j] != countt.get(j , 0):
                return False
        return True
    

