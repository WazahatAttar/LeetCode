# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr, fw =head, head.next
        while fw:
            if curr.val==fw.val:
                curr.next=fw.next
            else:
                curr=curr.next
            fw=fw.next
        return head