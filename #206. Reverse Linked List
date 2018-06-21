class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None: # handling null or single-elment list
            return head
        
        ptr1 = head
        ptr2 = head.next  # ptr1 follows ptr2
        
        head.next = None  # reverse next
        
        while ptr2 is not None:
            ptr3, ptr2.next = ptr2.next, ptr1  # reverse next
            ptr1, ptr2= ptr2, ptr3             # step to right
        
        return ptr1
