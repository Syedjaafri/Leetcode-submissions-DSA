class Solution:
    def findMin(self, nums: List[int]) -> int:
       # using binary search approach

        mini = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            # check if the array is normal sorted or rotated sorted
            if nums[l] <= nums[r]:  #mean the arr is normally sorted
                mini = min(mini , nums[l])
                return mini

            # if the array is roted sorted 

            m = (l + r) // 2
            mini = min(mini , nums[m])

            if nums[m] >= nums[l]:  # it's roted sorted only,m is greater , check for the right portion of the array
                l = m + 1  # eliminate the left portion and check the right portion , sice mid element is greater thant the left element
            else:
                r = m-1  #eliminate the right portion and check only the left portion , sincce the middle ele is less than theleft element

        return mini


            

            

