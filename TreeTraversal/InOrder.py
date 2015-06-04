__author__ = 'shirleyyoung'

def inOrder(root):
    """
    in order traversal, iterative
    use a stack
    :param root:
    :return:
    """
    rst = []
    if not root:
        return rst
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            rst.append(root.val)
            root = root.right
    return rst
