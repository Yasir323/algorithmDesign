class Node:

    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def print_list(self):
        curr = self.head
        data = []
        while curr:
            if curr:
                data.append(curr.value)
            curr = curr.next