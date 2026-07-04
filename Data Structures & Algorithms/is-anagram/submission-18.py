class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # counter function in python
        
        return Counter(s) == Counter(t)