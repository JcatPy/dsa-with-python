class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(self, list1, list2):
    if not list1:
        return list2
    elif not list2:
        return list1

    dummy = ListNode(0)
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # One of them is empty, append the rest
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return dummy.next
