class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         
        result = []   # output 

        nums.sort()  # [-4 , -1, -1 , 0 , 1 , 2]

        for i , a in enumerate(nums):

            if i > 0 and a == nums[i - 1]: # elimnate the duplicates , i.e  the different
            # lists have same number again
                continue

            l = i + 1
            r = len(nums) - 1

            while(l < r):
                threesum = a +  nums[l] + nums[r]

                if threesum > 0:
                    r -= 1

                elif threesum < 0:
                    l += 1

                else:
                    result.append([a , nums[l] , nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1    # if same numbers in l pointer for the two differn t , iteration , the output , will be the same 
        return result
                    

                    

