class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=0
        temp=x
        while (temp!=0):
            num=(num*10) + temp%10
            temp=int(temp/10)
        if (num==x):
            return True
        else:
            return False