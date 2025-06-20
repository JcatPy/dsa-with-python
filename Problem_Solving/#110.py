def isBalanced(root) -> bool:
    def height(root):
        if root is None:
            return 0

        l = height(root.left)
        r = height(root.right)

        if l == -1:
            return -1
        if r == -1 or abs(l - r) > 1:
            return -1

        return 1 + max(l, r)

    return height(root) != -1