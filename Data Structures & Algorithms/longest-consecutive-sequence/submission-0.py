class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Handle the edge case where the array is empty
        if not nums:
            return 0
            
        # Step 1: Sort the array. This takes O(n log n) time.
        nums.sort()
        
        # Initialize variables to keep track of the sequences
        longest = 1
        current_longest = 1
        
        # Step 2: Iterate through the sorted array starting from the second element
        for i in range(1, len(nums)):
            
            # Ignore duplicates: If the current number is the same as the previous, just skip it
            if nums[i] == nums[i - 1]:
                continue
                
            # Step 3: Check if consecutive. If it is exactly 1 greater than the previous number...
            if nums[i] == nums[i - 1] + 1:
                # ...add 1 to our current sequence count
                current_longest += 1
            else:
                # The sequence broke! 
                # Update our overall 'longest' record if the 'current_longest' is bigger
                longest = max(longest, current_longest)
                # Reset the current sequence counter back to 1 for the new number
                current_longest = 1
                
        # Return the maximum between the longest sequence found during the loop 
        # and the final sequence that was being counted when the loop ended.
        return max(longest, current_longest)