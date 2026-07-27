class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setnums = set(nums)

        count = 0

        for n in nums:
            if (n - 1) not in setnums:
                length = 0

                while(n + length) in setnums:
                    length = length + 1
                count = max(length , count)
        return count