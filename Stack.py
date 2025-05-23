class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def getsize(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def peek(self):
        if self.isempty():
            return None
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isempty():
            return -1
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.value

if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

top_value = stack.pop()
print(f"Pop: {top_value}")
print(f"Stack: {stack}")