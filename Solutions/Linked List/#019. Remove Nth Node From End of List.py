class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if ptr1.next is None:        # handling single-element list
            return None
        
        ptr1 = ptr2 = head           # ptr2 follows ptr1, separation by (n-1) elements 
        
        for i in range(n - 1) :      # ptr1 points to the (n-1) th node
            ptr1 = ptr1.next
        
        if n == 1:                   # handling tail node
            while ptr1.next.next is not None: 
                ptr1 = ptr1.next
                ptr1.next = None
        
        else:
            while ptr1.next is not None: 
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            ptr2.val = ptr2.next.val
            ptr2.next = ptr2.next.next

        return head
