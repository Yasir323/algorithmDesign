from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


def inorder(temp):
    if not temp:
        return
    inorder(temp.lchild)
    print(temp.data)
    inorder(temp.rchild)


def insert(root, new_data):
    if not root:
        root = Node(new_data)
        return
    queue = Queue(maxsize=50)
    queue.put_nowait(root)
    while not queue.empty():
        temp = queue.get_nowait()
        if not temp.lchild:
            temp.lchild = Node(new_data)
            break
        else:
            queue.put_nowait(temp.lchild)
        if not temp.rchild:
            temp.rchild = Node(new_data)
            break
        else:
            queue.put_nowait(temp.rchild)


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
