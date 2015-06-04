__author__ = 'shirleyyoung'


from collections import deque

def levelOrder(root):
    """
    level order traversal
    :param root:
    :return:
    """
    rst = []
    if not root:
        return rst
    q = deque([root])
    while q:
        size = len(q)
        level = []
        for i in range(size):
            curr = q.popleft()
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
            level.append(curr.val)
        rst.append(level)
    return rst
