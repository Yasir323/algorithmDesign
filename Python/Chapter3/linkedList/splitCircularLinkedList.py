class Node:

    def __init__(self, data):
        self.value = data
        self.next = None


class CircularLinkedList:

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
            if curr.next:
                while curr.next != self._head:
                    curr = curr.next
            curr.next = Node(data)
            curr.next.next = self._head
        # Increase the length
        self._count += 1

    def __repr__(self):
        ls = [self._head.value]
        curr = self._head.next
        while curr != self._head:
            ls.append(curr.value)
            curr = curr.next
        return str(ls)

    def split_list(self, head1, head2):
        if self._head is None:
            return
        slow_ptr = self._head
        fast_ptr = self._head
        while fast_ptr.next != self._head and fast_ptr.next.next != self._head:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        if fast_ptr.next.next == self._head:
            fast_ptr = fast_ptr.next

        head1._head = self.head

        if self._head.next != self._head:
            head2._head = slow_ptr.next

        fast_ptr.next = slow_ptr.next
        slow_ptr.next = self.head


if __name__ == '__main__':
    ll = CircularLinkedList(2)
    ll.append(4)
    ll.append(56)
    print(ll)
    print(len(ll))
