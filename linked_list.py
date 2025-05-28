# Single Linked List Implementation
from itertools import count


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#what is the time complexity of the following functions?
# O(1) for insertions at the beginning,
# O(n) for insertions at the end or at a specific index
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_at_index(head, data, index):
    if index == 0:
        return insert_at_beginning(head, data)

    current_node = head
    position = 0
    while current_node is not None and position + 1 != index:
        current_node = current_node.next
        position += 1

    if current_node is not None:
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
    else:
        print("Index out of range")
    return head


def insert_at_end(head, data):
    if head is None:
        return Node(data)

    current = head
    while current.next:
        current = current.next

    new_node = Node(data)
    current.next = new_node
    return head

#what is the time complexity of the following functions?
# O(1) for updating the first node,
# O(n) for updating a node at a specific index
def update(head, data, index):
    current = head
    position = 0
    while current is not None and position != index:
        current = current.next
        position += 1

    if current is not None:
        current.data = data
    else:
        print("Index out of range")
    return head


def remove_first_node(head):
    if head is None:
        return None
    return head.next


def remove_last_node(head):
    if head is None:
        return None

    # If only one node exists, removing it results in an empty list
    if head.next is None:
        return None

    current = head
    previous = None
    while current.next is not None:
        previous = current
        current = current.next

    if previous is not None:
        previous.next = None
    return head

def remove_at_index(head, index):
    if head == None:
        return None

    current_node = head
    position = 0

    if index == 0:
        remove_first_node(head)

    while current_node is not None and position < index -1:
        current_node = current_node.next
        position += 1

    if current_node is None or current_node.next is None:
        print("Index out of range")
        return head
    else:
        current_node.next = current_node.next.next

def remove_by_value(head, value):
    if head is None:
        return None

    if head.data == value:
        return head.next

    current = head

    while(current.next is not None):
        if current.next.data == value:
            current.next = current.next.next
            return head
        current = current.next

def len_of_linked_list(head):
    count = 0
    if head is None:
        return count
    current = head
    while(current):
        count += 1
        current = current.next
    return count

def traverse(head):
    current = head
    while current:
        print(f'{current.data} ->', end=' ')
        current = current.next
    print('None')


# Testing the linked list functions

head = None
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)

head = insert_at_end(head, 5)
head = update(head, 10, 0)  # Updates first node's data to 10
head = remove_last_node(head)  # Removes the last node
head = remove_first_node(head)  # Removes the first node
head = remove_by_value(head, 3)  # Removes node with value 3
count = len_of_linked_list(head)  # Returns the length of the linked list

print(count)
traverse(head)
