class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        h = [0] * (c + 1) 
        area = 0
        
        for row in matrix:
            for i in range(c):
                h[i] = h[i] + 1 if row[i] == '1' else 0
            s = []
            for i in range(len(h)):
                while s and h[i] < h[s[-1]]:
                    ht = h[s.pop()]
                    wt = i if not s else i - s[-1] - 1
                    area = max(area, ht * wt)
                s.append(i)
        return area