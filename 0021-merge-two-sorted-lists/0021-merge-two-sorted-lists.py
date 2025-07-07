# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        nl = temp
        while (list1 and list2):
            if (list1.val<list2.val):
                nl.next = list1
                list1=list1.next
            else:
                nl.next = list2
                list2=list2.next
            nl=nl.next
        while(list1):
            nl.next = list1
            nl=nl.next
            list1=list1.next
        while(list2):
            nl.next = list2
            nl=nl.next
            list2=list2.next
        return temp.next