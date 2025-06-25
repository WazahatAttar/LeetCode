class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x=m+n-2
        y=m-1
        res=1.0
        for i in range(1,y+1):
            res= res * (x-y+i)/i
        return int(res)