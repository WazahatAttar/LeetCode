class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        i=1
        while i in nums:
            i=i+1
        return i