# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if(head is None or head.next is None):
            return None

        temp = head
        length = 0
        while(temp is not None):
            temp = temp.next
            length += 1

        curr = head
        prev = head
        count = 0

        if(length == n):
            return head.next

        else:
            while(count < (length-n)):
                prev = curr
                curr = curr.next
                count += 1
        
        # deleted_node = curr
        prev.next = curr.next
        # del deleted_node
        return head