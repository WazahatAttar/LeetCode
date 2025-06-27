class Solution:
    def trap(self, height: List[int]) -> int:
        tot=0
        left,leftMax,right,rightMax = 0,0,len(height)-1,0
        while left<=right:
            if height[left]<height[right]:
                if height[left]<leftMax:
                    tot+= leftMax-height[left]
                else:
                    leftMax=height[left]
                left+=1
            else:
                if height[right]<rightMax:
                    tot+= rightMax-height[right]
                else:
                    rightMax=height[right]
                right-=1
        return tot