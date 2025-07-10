class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return x
        rev=0
        s= x//abs(x)
        x=abs(x)
        while x>0:
            rev=rev*10+(x%10)
            x=x//10
        if rev<pow(2,31):
            return rev*s
        return 0