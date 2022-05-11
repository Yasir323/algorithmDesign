"""
Intersection of 2 Sorted Linked Lists.
"""

class Node:

    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:

    def __init__(self, data):
        self._head = Node(data)
        self._count = 1

    @property
    def head(self):
        return self._head

    def __len__(self):
        return self._count

    def __repr__(self):
        ls = []
        curr = self._head
        while curr:
            ls.append(curr.value)
            curr = curr.next
        return str(ls)

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


def intersection(a: LinkedList, b: LinkedList):
    result = []
    curr_a = a.head
    curr_b = b.head
    while curr_a is not None and curr_b is not None:
        if curr_a.value == curr_b.value:
            result.append(curr_a.value)
            curr_a = curr_a.next
            curr_b = curr_b.next
        elif curr_a.value > curr_b.value:
            curr_b = curr_b.next
        elif curr_a.value < curr_b.value:
            curr_a = curr_a.next
    return result

if __name__ == '__main__':
    ll1 = LinkedList(2)
    ll1.append(4)
    ll1.append(7)
    ll1.append(56)
    print(f"First Linked List: {ll1}")
    print(f"Length of first Linked List: {len(ll1)}")
    ll2 = LinkedList(2)
    ll2.append(4)
    ll2.append(5)
    ll2.append(7)
    ll2.append(70)
    print(f"Second Linked List: {ll2}")
    print(f"Length of second Linked List: {len(ll2)}")
    print(f"Intersection of the two Linked Lists: {intersection(ll1, ll2)}")
