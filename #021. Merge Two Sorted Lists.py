class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        ptr = l_pre = ListNode(0)
        
        ptr1, ptr2 = l1, l2
        
        while True:
            if ptr1 is None:
                ptr.next = ptr2
                break
            if ptr2 is None:
                ptr.next = ptr1
                break
            if ptr1.val < ptr2.val:
                val0 = ptr1.val
                ptr1 = ptr1.next
            else:
                val0 = ptr2.val
                ptr2 = ptr2.next

            ptr.next = ListNode(val0)
            ptr      = ptr.next
            
        return l_pre.next
