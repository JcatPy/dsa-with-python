from collections import deque
def levelOrder(root):
    if not root:
        return []

    res = []
    q = deque([root])

    while q:
        level_size = len(q)      # number of nodes in this level
        level = []               # collect values for this level

        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        res.append(level)        # one level done

    return res
