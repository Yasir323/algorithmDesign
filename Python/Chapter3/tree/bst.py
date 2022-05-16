class EmptyTreeError(Exception):
    """Raised when tree is empty."""

    def __init__(self, message="Tree is empty") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class BST:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def is_empty(self):
        if self.data is None:
            return True
        else:
            return False

    def insert(self, new_data):
        if self.data is None:
            self.data = new_data
            return
        if self.data == new_data:
            return
        if new_data < self.data:
            if self.left:
                self.left.insert(new_data)
            else:
                self.left = BST(new_data)
        else:
            if self.right:
                self.right.insert(new_data)
            else:
                self.right = BST(new_data)

    def print_preorder(self):
        """In-order traversal of BST."""
        print(self.data, end=' ')
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def search(self, data):
        if self.data:
            if self.data == data:
                print('Found!')
                return
            elif data < self.data:
                # Look to the left
                if self.left:
                    self.left.search(data)
                else:
                    print('Not Found!')
            else:
                # Look to the right
                if self.right:
                    self.right.search(data)
                else:
                    print('Not Found!')

    def delete(self, target, curr_data):
        if self.data is None:
            print("Tree is empty.")
            return
        # Find the target node
        if target < self.data:
            if self.left:
                self.left = self.left.delete(target, curr_data)
            else:
                print(f"{target} not found in tree.")
        elif target > self.data:
            if self.right:
                self.right = self.right.delete(target, curr_data)
            else:
                print(f"{target} not found in tree.")
        else:  # self._data == target
            # If found, we have 3 cases
            # If the target node is a leaf, just delete it
            # If the target node has 1 child, replace the node with the child
            if self.left is None:
                temp = self.right
                if target == curr_data:
                    self.data = temp.data
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp
            if self.right is None:
                temp = self.left
                if target == curr_data:
                    self.data = temp.data
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp
            # If the target node has 3 children, replace the target node with
            # Either the greatest node on the left or smallest node on the right
            curr = self.right  # Go to the right
            while curr.left:  # Traverse to the smallest element
                curr = curr.left
            self.data = curr.data
            self.right = self.right.delete(curr.data, curr_data)
        return self

    def count(self) -> int:
        if self.data is None:
            return 0
        left_count = 0 if self.left is None else self.left.count()
        right_count = 0 if self.right is None else self.right.count()
        return 1 + left_count + right_count


if __name__ == '__main__':
    import random
    array = [12, 33, 4, 53, 36, 84]
    print(array)
    bst = BST(35)
    print(bst.count())
    for element in array:
        bst.insert(element)
    bst.print_preorder()
    print()
    print(bst.count())
    # Search
    bst.search(36)
    # Delete
    bst.delete(36, 35)
    bst.print_preorder()
    print()
    print(bst.count())
    bst.delete(35, 35)
    bst.print_preorder()
    print()
    print(bst.count())
