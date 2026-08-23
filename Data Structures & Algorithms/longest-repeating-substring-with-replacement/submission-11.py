class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # optimized approach using the maxf variable 
        count = {} #dictionary for storing the count
        res = 0
        l = 0
        maxf = 0  # external variable for storing the count of string when replacement and giving it to the res variable

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r] , 0)
            maxf = max(maxf , count[s[r]])  #storing the count seperately

            while(r - l + 1 ) - max(count.values()) > k:  # but it should be < k:
                count[s[l]] = count[s[l]] - 1  # we need to decrement the count
                #because we need to check for nxt elemtn window , only k is 2
                l = l + 1
            res = max(res , r - l + 1)
        return res

                

        