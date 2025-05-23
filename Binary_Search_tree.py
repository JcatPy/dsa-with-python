class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root == None:
        return Node(value)

    if root.value == value:
        return root

    if root.value < value:
        root.right = insert(root.right, value)

    else:
        root.left = insert(root.left, value)

    return root

def search(root, value):
    if root is None or root.value == value:
        return root

    if root.value < value:
        return search(root.right, value)

    return search(root.left, value)

def get_successor(root):
    curr = root.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def del_node(root, value):
    if root is None:
        return root

    if root.value>value:
        root.left = del_node(root.left, value)

    elif root.value<value:
        root.right = del_node(root.right, value)

    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        succ = get_successor(root)
        root.value = succ.value
        root.right = del_node(root.right, succ.value)

    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value, end = " ")
        inorder(root.right)

r = Node(15)
r = insert(r, 10)
r = insert(r, 18)
r = insert(r, 4)
r = insert(r, 11)
r = insert(r, 16)
r = insert(r, 20)
r = insert(r, 13)

# Print inorder traversal of the BST
inorder(r)
print()
s1 = search(r, 19)
s2 = search(r, 20)
print(f"{s1.value} Found" if s1 else f"Not Found")
print(f"{s2.value} Found" if s2 else "Not Found")
