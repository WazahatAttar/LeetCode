class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        maxsum=0
        for i in range(k):
            sum+=nums[i]
        maxsum=sum
        for i in range(1,len(nums)-k+1):
            sum=sum-nums[i-1]+nums[i+k-1]
            maxsum=max(maxsum,sum)
        return(maxsum/k)
