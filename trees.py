class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.leftNode = None
        self.rightNode = None


node1 = TreeNode("Ancestor")
node2 = TreeNode("first leftgrandpa")
node3 = TreeNode("first rightgrandpa")
node4 = TreeNode("tope")
node5 = TreeNode("dupe")
node6 = TreeNode("emma")
node7 = TreeNode("Jennifer")
node8 = TreeNode("Monica")
# Creating a binary tree with the following structure:
#
#               "Ancestor"
#              /          \
#  "first leftgrandpa"   "first rightgrandpa"
#         /       \             /       \
#    "tope"    "dupe"      "Jennifer"   "Monica"
#
# The root of the tree is "Ancestor".


node1.leftNode = node2
node1.rightNode = node3
node2.leftNode = node4
node2.rightNode = node5
node3.leftNode = node7
node3.rightNode = node8


def preOrdertraverse(root: TreeNode):
    if root == None:
        return
    print(root.value)
    preOrdertraverse(root=root.leftNode)
    preOrdertraverse(root=root.rightNode)


preOrdertraverse(node1)
