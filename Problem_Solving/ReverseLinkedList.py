def reverseList(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if head is None:
        return None

    poin1 = head
    poin2 = head.next
    poin1.next = None  # Make sure the original head becomes the tail

    while poin2:
        temp = poin2.next
        poin2.next = poin1
        poin1 = poin2
        poin2 = temp

    return poin1



