# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None

        prev = None
        cur = l2

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        l1 = head
        l2 = prev

        res = cur = ListNode()
        whichOne = True
        while l1 and l2:
            if whichOne:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            whichOne = not whichOne

        cur.next = l1 or l2

