class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Problem statement 
        # simple goal: to find the most repeating numbers from the array , 
        # but with one condition , if k = 2 , which numbers are repeating frequent more that 
        # 2(k) , we need to print those , if k = 3 , we need to print the numbers ,
        # repeating more than 3 i.e k.
        # using bucket sort

        count = {} # it's a dictionary that'll have that number with it's frequency count
        freq = [[]for i in range(len(nums) + 1)] # using bucket sort , 
        # it creates a len +1 , if len 6 , it creates 7 buckets to store how many times a number repeated
        for n in nums:
            count[n] = 1 + count.get(n , 0)# here where counting happens

        for n , c in count.items(): # responsible for matching a number how times it repeated
        # and match it appropriately
            freq[c].append(n) # matching of count with the number

        res= [] # result to show the which are the top k frequent elements
 
        for i in range(len(freq)-1 , 0 , -1): # backward traversal because
        # the highest frequent no only at the last?
            for n in freq[i]: # we dont append the count of the no to result
                res.append(n) # we append the actual number which is at the last , so only we do back traversal 
            if len(res) == k: # if k is 3 , the traversal till we get top 3 frequ nos of bucket
                return res  # we return only that 

                # even i understand the concept , im struggling to change  to the actual code
