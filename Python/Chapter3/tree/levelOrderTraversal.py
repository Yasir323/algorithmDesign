"""
Level Order traversal of a Binary Tree.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def height(node):
    if not node:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def print_current_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=' ')
    elif level > 1:
        print_current_level(root.left, level - 1)
        print_current_level(root.right, level - 1)


def print_level_order(root):
    h = height(root)
    for i in range(1, h + 1):
        print_current_level(root, i)
    print()


"""
Time Complexity: O(n^2) in worst case. For a skewed 
tree, printGivenLevel() takes O(n) time where n is 
the number of nodes in the skewed tree. So time 
complexity of printLevelOrder() is O(n) + O(n-1) + 
O(n-2) + .. + O(1) which is O(n^2). 
Auxiliary Space:  O(n) in the worst case. For a 
skewed tree, printGivenLevel() uses O(n) space for 
call stack. For a Balanced tree, the call stack uses 
O(log n) space, (i.e., the height of the balanced 
tree). 
"""

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is -")
print_level_order(root)
