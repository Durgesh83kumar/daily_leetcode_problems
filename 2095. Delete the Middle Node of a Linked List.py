# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if(head is None or head.next is None):
        #     return None
        # count = 0
        # temp = head
        # while(temp is not None):
        #     temp = temp.next
        #     count += 1

        # middle = count//2
        # index = 0
        # curr = head
        
        # while(index < middle-1):
        #     curr = curr.next
        #     index = index + 1

        # deleted_node = curr.next
        # curr.next = curr.next.next
        # del deleted_node

        # return head 

        # by slow fast method
        if(head is None or head.next is None):
            return None

        slow = head
        fast = head
        prev = None

        while(fast is not None and fast.next is not None):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # deleted_Node = slow  
        prev.next = slow.next
        # del deleted_Node  # as python automatically delete the garbage value by garbage collector

        return head 

