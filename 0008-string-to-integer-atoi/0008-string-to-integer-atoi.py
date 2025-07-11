class Solution:
    def myAtoi(self, s: str) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        n, d, si, sign = 0, False, False, 1
        for c in s:
            if not d and not si and c==" ":
                continue
            if not d and not si and c in ["+","-"]:
                if c=="-":
                    sign=-1
                si=True
                continue
            if c.isdigit():
                d=True
                t=int(c)
                n=n*10 + t
                if n*sign<MIN:
                    return MIN
                elif n*sign>MAX:
                    return MAX
                continue
            return n*sign
        return n*sign
            