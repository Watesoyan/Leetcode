def Merge(pHead1, pHead2):
    p = pHead_pre = ListNode(0)
    p1, p2 = pHead1, pHead2
    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
            p = p.next
        else:
            p.next = p2
            p2 = p2.next
            p = p.next
    if p1 is None:
        p.next = p2
    else:
        p.next = p1
    return pHead_pre.next
