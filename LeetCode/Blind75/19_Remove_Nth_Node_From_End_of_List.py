# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp=head
        offset = ListNode()
        offset.next = head
        head = offset
        for i in range(n-1):
            temp = temp.next
        
        while temp and temp.next:
            temp = temp.next
            offset = offset.next

        offset.next = offset.next.next if offset.next else None
        return head.next
