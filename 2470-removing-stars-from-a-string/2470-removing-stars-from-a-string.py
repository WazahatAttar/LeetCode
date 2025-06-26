class Solution:
    def removeStars(self, s: str) -> str:
        st = ""
        for i in s:
            if i != '*':
                st = st+i
            else:
                st = st[:-1]
        return st