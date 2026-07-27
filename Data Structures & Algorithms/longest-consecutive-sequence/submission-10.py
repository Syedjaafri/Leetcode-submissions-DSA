class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # brute force sorting method

        if not nums:
            return 0  # checking if the array is empty


        nums.sort() # sorting of nums is most important
        count = 1    # curr_count stored inside this before sequence break.total count 
        curr_count = 1  # curr_count will reset when the sequence broke 

        for i in range(0,len(nums)-1):

            # to ignore the duplicate , most important

            if nums[i] == nums[i+1]:
                continue

            if nums[i+1] == nums[i] + 1: # next num must be +1 than the previous num

                curr_count = curr_count + 1
            
            # if it's not +1 than the previous , sequencebroke

            else:
                count = max(curr_count , count)
                curr_count = 1

        return max(count , curr_count)