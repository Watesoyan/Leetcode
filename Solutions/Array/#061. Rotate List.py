class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        
        ptr = head
        cnt = 0          # index of node
        
        while ptr.next is not None:
            ptr = ptr.next
            cnt += 1
        
        ptr.next = head  # construct cycle list
        
        n = cnt + 1      # length of list   
        m = k % n        # effective offset
        
        ptr = head
        
        for cnt in range(n - m - 1):
            ptr = ptr.next
        
        head = ptr.next  # reconstruct list
        ptr.next = None
        
        return head
