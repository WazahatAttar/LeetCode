class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ns = ''.join([str(ord(i)-96) for i in s])
        print(ns)
        for i in range(k):
            sum = 0
            for x in ns:
                sum = sum + int(x)
            ns = str(sum)
        return(int(ns))    