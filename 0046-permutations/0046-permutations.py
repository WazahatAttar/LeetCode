class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if(n<=1):
            return [nums]
        else:
            a = nums[0]
            res = []
            for elem in self.permute(nums[1:]):
                for i in range(0,n):
                    new_elem = elem[:]
                    new_elem.insert(i, a)
                    res.append(new_elem)
            return res