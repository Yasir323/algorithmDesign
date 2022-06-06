from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


def insert(root, new_data):
    if not root:
        root = Node(new_data)
        return
    queue = Queue(maxsize=50)
    queue.put_nowait(root)
    while not queue.empty():
        temp = queue.get_nowait()
        if temp.lchild:
            queue.put_nowait(temp.lchild)
            break
        else:
            temp.lchild = Node(new_data)
        if temp.rchild:
            queue.put_nowait(temp.rchild)
            break
        else:
            temp.rchild = Node(new_data)


def inorder(temp):
    if not temp:
        return
    inorder(temp.lchild)
    print(temp.data)
    inorder(temp.rchild)


def delete(root, target):
    # If tree is empty, return
    if not root:
        return
    # If root is the only node
    if root.lchild is None and root.rchild is None:
        # if the root data is the target, return
        if root.data == target:
            return
        else:
            return root
    key_node = None
    temp = None
    last = None
    queue = Queue(maxsize=50)
    queue.put_nowait(root)
    while not queue.empty():
        temp = queue.get_nowait()
        if temp.data == target:
            key_node = temp
        if temp.lchild:
            last = temp
            queue.put_nowait(temp.lchild)
        if temp.rchild:
            last = temp
            queue.put_nowait(temp.rchild)
    if key_node:
        key_node.data = temp.data # Swap target node with the rightmost node
        if last.rchild == temp:
            last.rchild = None
        else:
            last.lchild = None
    del temp
    return root


# Driver code
if __name__ == '__main__':
    root = Node(10)
    root.lchild = Node(11)
    root.lchild.lchild = Node(7)
    root.rchild = Node(9)
    root.rchild.lchild = Node(15)
    root.rchild.rchild = Node(8)
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root)
 
    key = 12
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)
    root = delete(root, 9)
    print("After deleting 9.")
    inorder(root)
