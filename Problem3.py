# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        fast = head
        while slow !=fast:
            slow = slow.next
            fast = fast.next
        return slow