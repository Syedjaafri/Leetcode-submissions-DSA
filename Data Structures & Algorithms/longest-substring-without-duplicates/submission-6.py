class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # optimized solution (sliding window) -> two pointer having boudaries

        res = 0
        l = 0
        hey_set = set()

        for r in range(len(s)):
            while s[r] in hey_set:  # which means duplicates , traversing element aldready added to the set
                # we need to remove from both the set and the window
                hey_set.remove(s[l])  # removing the first element inthe outerloop
                l += 1 # increamenting the outerloop (left pointer)
            hey_set.add(s[r])  #not duplicate so add the left pointer as first answer substring 

            res = max(res , r - l+1)



        return res