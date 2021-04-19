from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        for h in range(len(height)-1):
            lmax = max(height[:h+1])
            rmax = max(height[h:])
            vol += (min(lmax, rmax) - height[h])
        return vol


soln = Solution()
print(soln.trap([0,1,0,2,1,0,1,3,2,1,2,1]))