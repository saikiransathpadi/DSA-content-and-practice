# 28 July

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        temp = head
        curr = None
        while temp:
            nxt = temp.next
            temp.next = curr
            curr = temp
            temp = nxt
        return curr
