import sys


class Node:

    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def left_rotate(self, x):
        y = x.right
        temp = y.left
        y.left = x
        x.right = temp
        x.height = 1 + max(self.get_height(x.left),
                          self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left),
                          self.get_height(y.right))
        return y

    def right_rotate(self, x):
        y = x.left
        temp = y.right
        y.right = x
        x.left = temp
        x.height = 1 + max(self.get_height(x.left),
                          self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left),
                          self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def balance_factor(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_minvalue(self, root):
        if root is None or root.left is None:
            return root
        return self.get_minvalue(root.left)

    def preorder(self, root):
        if not root:
            return
        print(root.val, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def print_tree(self, curr_pointer, indent, last):
        if curr_pointer != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(curr_pointer.val)
            self.print_tree(curr_pointer.left, indent, False)
            self.print_tree(curr_pointer.right, indent, True)

    def insert_node(self, root, key):
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)
        root.height = 1 + max(self.get_height(root.left), 
                              self.get_height(root.right))
        # Update the balance factor and balance the tree
        bf = self.balance_factor(root)
        if bf > 1:
            if key < root.left.val:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        elif bf < -1:
            if key < root.right.val:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def delete_node(self, root, key):
        # Locate the target node
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:  # Found
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_minvalue(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp.val)

        if root is None:
            return root
        # Update the balance factor
        root.height = 1 + max(self.get_height(root.left),
                             self.get_height(root.right))
        bf = self.balance_factor(root)
        # Balance the tree
        if bf > 1:
            if self.balance_factor(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        elif bf < -1:
            if self.balance_factor(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root


myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]

for num in nums:
    root = myTree.insert_node(root, num)

myTree.print_tree(root, "", True)
myTree.preorder(root)
print()
key = 13
root = myTree.delete_node(root, key)
print("After Deletion: ")
myTree.print_tree(root, "", True)
