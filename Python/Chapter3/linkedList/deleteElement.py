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

    def delete_node(self, data):
        curr = self._head
        # If head is to be removed
        if curr.value == data:
            self._head = curr.next
            self._count -= 1
            return 0
        # Traverse to the previous node
        while curr.next:
            if curr.next.value == data:
                break
            curr = curr.next
        target_node = curr.next 
        if not target_node:
            return 0
        curr.next = target_node.next
        target_node = None
        self._count -= 1
        return 1

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
    ll.delete_node(89)
    print(ll)
    print(len(ll))
