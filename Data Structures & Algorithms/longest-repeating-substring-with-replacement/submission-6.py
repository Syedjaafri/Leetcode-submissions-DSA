class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the question is if we a change one variable to most repeating duplicate value , what's the  final long repeating length , but we can change based on what k is ?

    # brute force using hash map 
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r] , 0)

            while(r - l+1)  - max(count.values()) > k: # ws - max count
                count[s[l]] -= 1   # we are just decrementing the count , not the character , since  window size -  max f exceeds the k , so we decrement the existing count
                l = l+1
            res = max(res , r- l+1)
        return res