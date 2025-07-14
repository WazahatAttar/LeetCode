class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dir={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        lst=[]
        def backtrack(i:int, c:str):
            #base case
            if i == len(digits):
                lst.append(c)
                return
            for char in dir[digits[i]]:
                backtrack(i + 1, c + char)
        backtrack(0, "")
        return lst