def ReverseList(pHead):
    if pHead is None or pHead.next is None:
        return pHead
    p1 = pHead
    p2 = pHead.next
    p1.next = None    # tail node establish
    while p2 is not None:
        tmp = p2
        p2 = tmp.next
        tmp.next = p1
        p1 = tmp
    return p1
