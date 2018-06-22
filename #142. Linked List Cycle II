class Solution(object):
    # using fast-slow strategy
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast_ptr = slow_ptr = head
        
        while fast_ptr is not slow_ptr:
            if fast_ptr is None or fast_ptr.next is None:
                return None
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        
        slow_ptr2 = head
        
        while slow_ptr2 is not slow_ptr:
            slow_ptr  = slow_ptr.next
            slow_ptr2 = slow_ptr2.next
        return slow_ptr
