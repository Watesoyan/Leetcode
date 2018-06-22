class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast_ptr = slow_ptr = head
        stack = []
        
        while fast_ptr is not None:
            
            fast_ptr = fast_ptr.next
            
            if fast_ptr is not None:
                stack.append(slow_ptr.val)
                fast_ptr = fast_ptr.next
            
            slow_ptr = slow_ptr.next
        
        while slow_ptr is not None:
            if slow_ptr.val != stack.pop(): # list[i] != list[n-i-1] 
                return False
            slow_ptr = slow_ptr.next
        return True
