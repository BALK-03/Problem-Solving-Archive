# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list = []
        curr = head

        while curr:
            list.append(curr)
            curr = curr.next
        
        return list[len(list) // 2]
        