__author__ = 'shirleyyoung'
from TreeTraversal import TreeNode, ZigzagLevelOrder, InOrder, PostOrder, PreOrder, LevelOrder

def main():
    n1 = TreeNode.TreeNode(1)
    n2 = TreeNode.TreeNode(2)
    n3 = TreeNode.TreeNode(3)
    n4 = TreeNode.TreeNode(4)
    n5 = TreeNode.TreeNode(5)
    n6 = TreeNode.TreeNode(6)
    n7 = TreeNode.TreeNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    #root = None
    #rst = LevelOrder.levelOrder(root)
    #rst = PreOrder.preOrderRec2(n1)
    #rst = PostOrder.postOrder(n1)
    #rst = InOrder.inOrder(n1)
    rst = ZigzagLevelOrder.zigzag(n1)

    for node in rst:
        print(node, end='\t')


if __name__ == "__main__":
    main()