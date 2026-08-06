class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []  # output

        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and a==  nums[i - 1]: # for duplicates
                continue
             
             # assigning the 2 pointers 

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum > 0:  # note: array is sorted
            
                    r -= 1
                
                elif threesum < 0:  # it may have the negative value
                    l += 1

                else:  # threesum == 0, the answer
                    result.append([a , nums[l] , nums[r]])
                    # after appeding check for next outputs
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result 


                




