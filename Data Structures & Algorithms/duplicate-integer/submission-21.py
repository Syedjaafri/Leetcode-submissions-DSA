class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # optimized using hashset

        jaafri = set()

        for j in nums:
            if j in jaafri:
                return True
            jaafri.add(j)
        return False