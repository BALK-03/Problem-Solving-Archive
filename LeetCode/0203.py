# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode()
        tail = dummy

        while head:
            if head.val != val:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return dummy.next