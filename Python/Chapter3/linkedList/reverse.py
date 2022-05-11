"""
Intersection of 2 Sorted Linked Lists.
"""

class Node:

    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:

    def __init__(self, data):
        self.__head = Node(data)
        self.__count = 1

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value
    
    def __len__(self):
        return self.count

    def __repr__(self):
        ls = []
        curr = self.head
        while curr:
            ls.append(curr.value)
            curr = curr.next
        return str(ls)

    def append(self, data):
        """Insert element at the end of the Linked List -> O(n)"""
        # If list is empty? Node becomes the head
        if not self.head:
            self.head = Node(data)
        else:
            # Traverse to the end O(n)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
        # Increase the length
        self.count = self.count + 1

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next    
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev


if __name__ == '__main__':
    ll = LinkedList(2)
    ll.append(4)
    ll.append(7)
    ll.append(56)
    print(f"Original Linked List: {ll}")
    print(f"Length of the Linked List: {len(ll)}")
    ll.reverse()
    print(f"Reversed Linked List: {ll}")
    print(f"Length of the Linked List: {len(ll)}")
