class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        no=0
        for i in digits:
            no=no*10+i
        no+=1
        fd=[]
        while no!=0:
            fd.append(no%10)
            no=no//10
        fd.reverse()
        return fd