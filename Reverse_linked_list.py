class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    current = head
    prev = None
    while(current is not None):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def printList(node):
    while node is not None:
        print(f" {node.data}", end="")
        node = node.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    printList(head)

    head = reverse(head)

    print("Reversed Linked List:", end="")
    printList(head)
