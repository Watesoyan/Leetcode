class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        ptr1 = head
        ptr2 = ptr3 = head.next        # ptr3 points to second node
        
        while True:
            if ptr2.next is None:
                break
            else:
                ptr1.next = ptr2.next
            ptr1 = ptr2.next
            if ptr1.next is None:
                break
            else:
                ptr2.next = ptr1.next
            ptr2 = ptr1.next
        
        ptr2.next = None
        ptr1.next = ptr3
        
        return head
