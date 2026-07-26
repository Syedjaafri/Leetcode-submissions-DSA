class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using prefix and postfix  method(o(1) , o(n))

        # 2 steps-> 
        # step 1: prefix , 1st pass from start to end of the array 

        res = [1] * (len(nums))  # result list must be same as len of the input array

        prefix = 1  #initially it's 1 , so we first insert the prefix to the array in 0th index

        for i in range(len(nums)):
            res[i] = prefix  # 1st iteration [1 , , , ]

            prefix = prefix * nums[i]  # multiply the initial prefix with the current index, to get new prefix
        # finally we 're inserting the prefix values to the result list , as the first pass

        # step 2: postfix , 2nd pass , from end to the start of the array

        postfix = 1

        for i in range(len(nums) - 1, -1 , -1):
            # we gonna update the res list to get the output list
            # multiply the result values (prefix in 1st pass) with the input array from the last

            res[i] *= postfix # multiplying happens between theres list and the postfix

            # we need to update the postfix on each iterations

            postfix = postfix * nums[i] # 2nd iteration , postfix = 4 , so 4 * 3 = 12 -> 12 is the new postfix
        return res 

         