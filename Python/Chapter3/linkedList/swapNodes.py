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

    def find_previous(self, target):
        curr = self._head
        while curr.next:
            if curr.next.value == target:
                break
            curr = curr.next
        return curr

    def swap_nodes(self, a, b):
        prev_a = self.find_previous(a)
        prev_b = self.find_previous(b)
        curr_a = prev_a.next
        curr_b = prev_b.next
        
        # temp = prev_a.next
        prev_a.next = curr_b
        prev_b.next = curr_a

        temp = curr_a.next
        curr_a.next = curr_b.next
        curr_b.next = temp

    def __repr__(self):
        ls = []
        curr = self._head
        while curr:
            ls.append(curr.value)
            curr = curr.next
        return str(ls)


if __name__ == '__main__':
    ll = LinkedList(1)
    ll.append(2)
    ll.append(9)
    ll.append(7)
    ll.append(4)
    print(ll)
    print(len(ll))
    print(ll.swap_nodes(2, 7))
    print(ll)
