"""
Level Order Traversal using a Queue.
"""

from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


def print_level_order(root):
    if root is None:
        return

    queue = Queue(maxsize=50)
    queue.put_nowait(root)
    while not queue.empty():
        node_ = queue.get_nowait()
        print(node_.data)
        if node_.lchild:
            queue.put(node_.lchild)
        if node_.rchild:
            queue.put(node_.rchild)


# Driver Program to test above function
root = Node(1)
root.lchild = Node(2)
root.rchild = Node(3)
root.lchild.lchild = Node(4)
root.lchild.rchild = Node(5)
 
print("Level Order Traversal of binary tree is -")
print_level_order(root)
