# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1 for _ in range(n)] for _ in range(m)]
        dir = 'r'
        cell = [0,0]
        while(head):
            if(mat[cell[0]][cell[1]] == -1):
                mat[cell[0]][cell[1]] = head.val
                print(head.val,cell,dir)
                if(dir == 'r'):
                    if(cell[1]+1>=n):
                        dir = 'd'
                        cell[0]+=1
                    else:
                        cell[1]+=1
                elif(dir =='d'):
                    if(cell[0]+1>=m):
                        dir = 'l'
                        cell[1]-=1
                    else:
                        cell[0]+=1
                elif(dir =='l'):
                    if(cell[1]-1<0):
                        dir = 'u'
                        cell[0]-=1
                    else:
                        cell[1]-=1
                else:
                    if(cell[0]-1<0):
                        dir = 'r'
                        cell[1]+=1
                    else:
                        cell[0]-=1
            else:
                if(dir =='r'):
                    dir = 'd'
                    cell[0]+=1
                    cell[1]-=1
                    mat[cell[0]][cell[1]] = head.val
                    cell[0]+=1
                elif(dir=='d'):
                    dir='l'
                    cell[0]-=1
                    cell[1]-=1
                    mat[cell[0]][cell[1]] = head.val
                    cell[1]-=1
                elif(dir=='l'):
                    dir='u'
                    cell[0]-=1
                    cell[1]+=1
                    mat[cell[0]][cell[1]] = head.val
                    cell[0]-=1
                else:
                    dir='r'
                    cell[0]+=1
                    cell[1]+=1
                    mat[cell[0]][cell[1]] = head.val
                    cell[1]+=1
                print(head.val,cell,dir)
            head = head.next
        return(mat)