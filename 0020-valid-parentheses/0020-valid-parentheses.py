class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        try:
            for b in s:
                if (b=='(' or b=='{' or b=='['):
                    stack.append(b)
                elif (b==')'):
                    t=stack.pop()
                    if t!='(':
                        return False
                elif (b=='}'):
                    t=stack.pop()
                    if t!='{':
                        return False
                elif (b==']'):
                    t=stack.pop()
                    if (t!='['):
                        return False
            if (len(stack)!=0):
                return False
            return True
        except:
            return False