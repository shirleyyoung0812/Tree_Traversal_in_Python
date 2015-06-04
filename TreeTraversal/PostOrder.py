__author__ = 'shirleyyoung'


def postOrder(root):
    """
    iterative way, using two stacks
    :param root:
    :return:
    """
    rst = []
    if not root:
        return rst
    stack1 = [root]
    stack2 = []
    while stack1:
        curr = stack1.pop()
        if curr.left is not None:
            stack1.append(curr.left)
        if curr.right is not None:
            stack1.append(curr.right)
        stack2.append(curr)
    while stack2:
        rst.append(stack2.pop().val)
    return rst


