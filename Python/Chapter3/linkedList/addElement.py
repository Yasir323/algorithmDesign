class Node:

    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:

    def __init__(self, data):
        self._head = Node(data)
        self._count = 1

    def __len__(self):
        return self._count
    
    def prepend(self, data):
        """Insert element at the start of the Linked List -> O(1)"""
        # If list is empty? Node becomes the head
        if not self._head:
            self._head = Node(data)
        else:
            # New node points to where head was pointing
            new_node = Node(data)
            new_node.next = self._head
            # Now new node becomes the head
            self._head = new_node
        # Increase the length
        self._count += 1

    def append(self, data):
        """Insert element at the end of the Linked List -> O(n)"""
        # If list is empty? Node becomes the head
        if not self._head:
            self._head = Node(data)
        else:
            # Traverse to the end O(n)
            curr = self._head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
        # Increase the length
        self._count += 1

    def insert_after(self, data, prev_data):
        """Insert after a given element -> O(n)"""
        # Find the element O(n)
        new_node = Node(data)
        curr = self._head
        while curr.value != prev_data:
            if not curr.next:
                break
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self._count += 1

    def __repr__(self):
        ls = []
        curr = self._head
        while curr:
            ls.append(curr.value)
            curr = curr.next
        return str(ls)


if __name__ == '__main__':
    ll = LinkedList(2)
    ll.append(4)
    ll.append(56)
    ll.prepend(7)
    ll.insert_after(5, 7)
    ll.insert_after(34, 4)
    ll.insert_after(9, 56)
    print(ll)
    print(len(ll))