class Node:

    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, new_data):
        # Make a node
        new_node = Node(new_data)
        # If list is empty, this node becomes the head
        if not self.head:
            self.head = new_node
            return
        # Otherwise Traverse to the previous node
        curr = self.head
        while curr.next:
            curr = curr.next
        # Current node's next is new node
        curr.next = new_node
        # New node's prev is current node
        new_node.prev = curr

    def prepend(self, new_data):
        # Make a node
        new_node = Node(new_data)
        # If list is empty, new node becomes the head
        if not self.head:
            self.head = new_node
            return
        # Otherwise, head's prev points to new_node
        self.head.prev = new_node
        # New node's next becomes current head
        new_node.next = self.head
        # New Node becomes the head
        self.head = new_node

    def insert_after(self, target, new_data):
        # Traverse to the target node
        curr = self.head
        while curr and curr.value != target:
            curr = curr.next
        # If node not found, raise
        if curr is None:
            raise ValueError("Target node not found in the list.")
        else:
            # Otherwise, make a new node
            new_node = Node(new_data)
            # New node's next points to where target node was pointing
            new_node.next = curr.next
            # New node's prev points to target node
            new_node.prev = curr
            # Next node's prev points to new node
            curr.next.prev = new_node
            # Target node's next points to new node
            curr.next = new_node
            

    def delete(self, target):
        # Traverse to the target node
        curr = self.head
        while curr and curr.value != target:
            curr = curr.next
        # If node not found, raise
        if curr is None:
            raise ValueError("Target node not found in the list.")
        else:
            prev_node = curr.prev
            next_node = curr.next
            # Previous node's next points to next node
            prev_node.next = next_node
            # Next node's prev points to previous node
            next_node.prev = prev_node
            # Cleanup
            curr.next = curr.prev = curr.data = None
            del curr
    
    def reverse(self):
        curr = self.head
        while curr:
            next_ = curr.next
            curr.next, curr.prev = curr.prev, curr.next
            if next_ is None:
                self.head = curr
            curr = next_
        

    def __str__(self):
        curr = self.head
        data = []
        while curr:
            if curr:
                data.append(curr.value)
            curr = curr.next
        return str(data)


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.prepend(3)
    dll.append(2)
    dll.append(45)
    dll.append(7)
    dll.prepend(33)
    dll.insert_after(2, 5)
    dll.delete(45)
    print(dll)
    dll.reverse()
    print(dll)
