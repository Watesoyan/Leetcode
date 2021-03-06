class Solution(object):
    # using fast-slow strategy
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast_ptr = slow_ptr = head
        
        while True:
            
            if fast_ptr is None or fast_ptr.next is None:
                return False
            
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            
            if fast_ptr is slow_ptr:
                return True
