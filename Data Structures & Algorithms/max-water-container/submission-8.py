class Solution:
    def maxArea(self, height: List[int]) -> int:
        # goal to find the maximum amount of water a container can store 
        # using optimized approach (two pointers)

            res = 0  # output 

            l = 0
            r = len(height) - 1

            while l < r:

                # to find the area --> width x height(formula)

                area = (r - l) * min(height[l] , height[r])
                res = max(res , area)

                if height[l] < height[r]: #if left pointer wall len is smaller , water will spill out
                    l = l + 1

                else:
                    r = r - 1

            return res
                
