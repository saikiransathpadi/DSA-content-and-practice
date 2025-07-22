# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while list1 and list2:
            if list1.val < list2.val:
                res.append(list1.val)
                list1 = list1.next
            else:
                res.append(list2.val)
                list2 = list2.next
        while list1:
            res.append(list1.val)
            list1 = list1.next
        while list2:
            res.append(list2.val)
            list2 = list2.next
        
        head = None
        temp = head
        for i in res:
            if temp is None:
                temp = ListNode(i)
                head = temp
            else:
                temp.next = ListNode(i)
                temp = temp.next
        return head
        
        