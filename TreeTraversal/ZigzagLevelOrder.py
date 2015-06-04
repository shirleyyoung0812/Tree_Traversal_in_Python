__author__ = 'shirleyyoung'

def zigzag(root):
    """
    zigzag level order traversal
    1
    23
    4567
    89
    will output
    1
    32
    4567
    98
    :param root:
    :return:
    """
    rst = []
    if not root:
        return rst
    thisLevel = [root]
    reverse = True
    while thisLevel:
        nextLevel = []
        level = []
        while thisLevel:
            curr = thisLevel.pop()
            level.append(curr.val)
            if reverse:
                if curr.left is not None:
                    nextLevel.append(curr.left)
                if curr.right is not None:
                    nextLevel.append(curr.right)
            else:
                if curr.right is not None:
                    nextLevel.append(curr.right)
                if curr.left is not None:
                    nextLevel.append(curr.left)

        thisLevel = nextLevel
        reverse = not reverse
        rst.append(level)
    return rst


