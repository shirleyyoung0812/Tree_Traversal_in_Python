__author__ = 'shirleyyoung'


def preOrder(root):
    """
    iterative version
    :param root:
    :return:
    """
    rst = []
    if not root:
        return rst
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
        rst.append(curr.val)
    return rst

def preOrderRec(root):
    """
    recursive version
    :param root:
    :return:
    """
    rst = []
    preorderHelper(root, rst)
    return rst

def preorderHelper(root, rst):
    if root is not None:
        rst.append(root.val)
        preorderHelper(root.left, rst)
        preorderHelper(root.right, rst)


def preOrderRec2(root):
    """
    nested inner recursive function
    :param root:
    :return:
    """
    rst = []

    def recursion(root):
        if root:
            rst.append(root.val)
            recursion(root.left)
            recursion(root.right)
    recursion(root)
    return rst
