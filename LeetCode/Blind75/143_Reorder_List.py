from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Try O(1) space solution next time
        if not head: return head
        arr = []
        temp = head
        while temp:
            nxt = temp.next
            temp.next = None
            arr.append(temp)
            temp = nxt
        i,j = 0, len(arr) - 1
        curr = None
        while i <= j:
            if i != j:
                arr[i].next = arr[j]
            
            if curr:
                curr.next = arr[i]
            curr = arr[j]

            i += 1
            j -= 1

