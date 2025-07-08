class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def validSubtring(substring):
            tw = words[:]
            i = 0
            while i < p:
                cw = substring[i: i + m]
                if cw in tw:
                    tw.remove(cw)
                i += m
            return tw == []
        ret, initWindow, notValid, valid = [], [], set(), set()
        n, k, m = len(s), len(words), len(words[0])
        p = m * k 
        if n < p:
            return []
        for i in range(p):
            l = s[i]
            initWindow.append(l)
        if validSubtring("".join(initWindow)):
            ret.append(0)
        i = p
        while i < n:
            l = s[i]
            initWindow.pop(0)
            initWindow.append(l)
            ts = "".join(initWindow)
            if ts not in notValid:
                if ts in valid or validSubtring(ts):
                    ret.append(i - p + 1)
                    valid.add(ts)
                else:
                    notValid.add(ts)
            i+=1
        return ret