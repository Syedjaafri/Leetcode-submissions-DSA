class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # USING TOTAL PRODUCT DIVISION METHOD , 

        total_pro = 1  #initially
        zero_count = 0 # initially , we need to count how many zeros in the array
                        # reason: if more than or =to 2 0's in array all the num are 0

        #step 1:

        for num in nums:
            if num == 0:
                zero_count += 1   # just increasing the count of zero , when we found a num as 0
            else:
                total_pro *= num  # for calculatin the total product of that array 

        res = [] # for storing the final list


        #step 2:

        # it has total 3 cases

        # case 1: if arr has more than or equal to two 0s then , the whole arr is 0
        for num in nums:
            if zero_count > 1:
                res.append(0)

        # case 2: if arr has only one 0 , then expect that 0 num , all other value wil become 0

            elif zero_count == 1:
                if num == 0:
                    res.append(total_pro) # except that 0 , other values will be producted
                # so , we append the total_pro , and we ignore the zero's in the array , whil total pr

                else:  # if the current num is non zero , we append 0 to res
                    res.append(0)

        # case 3 : if no zeros in the array , then very easily 

            else: # if zero_count == 0
                res.append(total_pro // num) # we can easily divide the num with total pro , to get the ans

        return res



        