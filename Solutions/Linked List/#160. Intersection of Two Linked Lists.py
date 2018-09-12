class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptr1 = headA
        ptr2 = headB
        
        if ptr1 is None or ptr2 is None:
            return None
        
        # find tail node
        while True:
            if ptr1 is ptr2:                # length of list1 and list2 are equal 
                return ptr1
            if ptr1.next is None:           # ptr1 reach at tail node 
                tail = ptr1
                pre_ptr = ptr2
                post_ptr = headB
                scout_ptr = headA
                break
            elif ptr2.next is None:         # ptr2 reach at tail node 
                tail = ptr2
                pre_ptr = ptr1
                post_ptr = headA
                scout_ptr = headB
                break
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        # find whether two lists intersect with each other
        while True:
            if pre_ptr.next is None:
                if pre_ptr is not tail:
                    return None
                else:
                    break
            pre_ptr = pre_ptr.next
            post_ptr = post_ptr.next
        
        # find intersection
        while post_ptr is not scout_ptr:
            post_ptr = post_ptr.next
            scout_ptr = scout_ptr.next
        
        return scout_ptr
