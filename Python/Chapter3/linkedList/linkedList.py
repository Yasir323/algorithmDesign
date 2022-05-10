from typing import Any
from collections import namedtuple
import gc  # Garbage collection

# Node = namedtuple('Node', ['data', 'next'], defaults=[None])


class NodeElement:

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, value: Any = None) -> None:
        head = NodeElement(value)
        self._head = head
    
    def __str__(self) -> str:
        """Traverse Linked List and print the nodes. String Representation."""
        curr = self._head
        ls = []
        # Traverse if List is not empty
        while curr:
            value = curr.data
            pointer = hex(id(curr.next)) if curr.next else None
            Node = namedtuple('Node', ['value', 'next'])
            curr_node = Node(value, pointer)
            ls.append(curr_node)
            curr = curr.next
        return f"{ls}"

    def __repr__(self) -> str:
        """Traverse Linked List and print the nodes. Raw Representation."""
        curr = self._head
        ls = []
        while curr:
            value = curr.data
            pointer = hex(id(curr.next)) if curr.next else None
            Node = namedtuple('Node', ['value', 'next'])
            curr_node = Node(value, pointer)
            ls.append(curr_node)
            curr = curr.next
        return f"{ls}"
    
    def __len__(self) -> int:
        counter = 0
        curr = self._head
        while curr:
            counter += 1
            # if not curr.next:
            #     break
            curr = curr.next
        return counter

    def push(self, value: Any, index: int = None) -> None:
        new_node = NodeElement(value)
        # If list is empty, new node becomes the head
        if not self._head:
            self._head = new_node
            return

        if index == 0:  # Push Left
            # Set the next of the new node to head
            new_node.next = self._head
            # Make the new node, the head of the linked list
            self._head = new_node

        elif index == self.__len__() or index is None:  # Push Right
            # Traverse to the last element
            curr = self._head
            while curr.next:
                curr = curr.next
            # Set the next of the last node to new_node
            curr.next = new_node

        elif index > self.__len__() or index < 0:
            raise IndexError("List index out of range.")

        else:
            # Traverse to the left node of given index
            curr = self._head
            i = 0
            while i < index - 1:
                curr = curr.next
                i += 1
            # Copy the next of left node to next of new node
            new_node.next = curr.next
            # Set next of left node to new node
            curr.next = new_node

    def remove(self, index: int) -> None:
        if index > self.__len__() or index < 0:
            raise IndexError("List index out of range.")
        curr = self._head
        if index == 0:
            self._head = self._head.next
            gc.collect()
            return
        # Traverse to the left of given index
        i = 0
        while i < index - 1:
            curr = curr.next
            i += 1
        # Copy the next elements' next to left
        temp = curr.next.next
        # Set next element's next to None
        curr.next.next = None
        curr.next = temp
        # curr = None
        gc.collect()


if __name__ == '__main__':
    node1 = 1
    node2 = 2
    node3 = 3
    node4 = 5

    linked_list = LinkedList(node1)
    print(linked_list)
    print(len(linked_list))

    linked_list.push(node2)
    print(linked_list)
    print(len(linked_list))

    linked_list.push(node3)
    print(linked_list)
    print(len(linked_list))

    linked_list.push(node4, index=3)
    print(linked_list)
    print(len(linked_list))

    linked_list.push(node4, index=2)
    print(linked_list)
    print(len(linked_list))

    linked_list.push(node3, index=0)
    print(linked_list)
    print(len(linked_list))

    try:
        linked_list.push(node4, 8)
    except IndexError as e:
        print(f"{type(e).__name__}: {str(e)}")

    linked_list.remove(index=0)
    print(linked_list)
    print(len(linked_list))

    linked_list.remove(index=2)
    print(linked_list)
    print(len(linked_list))

    linked_list.remove(index=1)
    print(linked_list)
    print(len(linked_list))
