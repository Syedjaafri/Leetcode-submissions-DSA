class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hash map 

        dictionary = {}  # val : index  -> 

        for i , n in enumerate(nums):
            difference  = target - n
            if difference  in dictionary:
                return [dictionary[difference] , i]
            dictionary[n] = i # if no differnce was = to the previously added element
        return

