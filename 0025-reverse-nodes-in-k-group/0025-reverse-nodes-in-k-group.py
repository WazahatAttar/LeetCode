# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        curr = head
        new_head = None
        tail = None

        while curr:
            temp = curr
            count = 0
            while temp and count < k:
                temp = temp.next
                count += 1
            if count < k:
                if tail:
                    tail.next = curr
                break
            group_head = curr
            prev = None
            next_node = None
            count = 0
            while curr and count < k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                count += 1
            if not new_head:
                new_head = prev
            if tail:
                tail.next = prev
            tail = group_head
        return new_head if new_head else head