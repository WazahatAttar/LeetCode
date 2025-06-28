class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        ans = 1
        temp = 0
        for i in nums:
            if(i == m):
                temp = temp + 1
            else:
                temp = 0
            ans = max(temp,ans)
        return ans