class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.front = self.rear = None

    def isempty(self):
        return  self.front == None and self.rear == None

    def enQueue(self, value):
        new_Node = Node(value)

        if self.isempty():
            self.front = self.rear = new_Node
            return
    