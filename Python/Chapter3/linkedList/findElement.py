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

    def find(self, data):
        curr = self._head
        index = 0
        try:
            while curr.value != data:
                curr = curr.next
                index += 1
        except AttributeError:
            return -1
        return index

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
    ll.append(7)
    print(ll)
    print(len(ll))
    print(ll.find(2))
