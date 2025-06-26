class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diff =start ^ goal
        flip = 0
        while(diff!=0):
            flip+=diff%2
            diff = int(diff/2)
        return flip