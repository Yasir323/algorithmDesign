class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def merge_sort(self, h):
        if h is None or h.next is None:
            return h

        # Get the mmiddle
        mid = self.get_middle(h)
        next_to_mid = mid.next

        # Set the next to mid to None
        mid.next = None

        # Sort the left side
        left_sorted = self.merge_sort(h)

        # Sort te right side
        right_sorted = self.merge_sort(next_to_mid)

        # Merge
        sorted_list = self.merge(left_sorted, right_sorted)
        return sorted_list

    def get_middle(self, h):
        if not h:
            return h
        slow = h
        fast = h

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        result = None

        # Base cases
        if not left:
            return right
        if not right:
            return left

        # Pick either left or right and recur...
        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result


def print_list(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end = " ")
        curr_node = curr_node.next
    print(' ')


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(15)
    ll.append(10)
    ll.append(5)
    ll.append(20)
    ll.append(3)
    ll.append(2)

    print("Unsorted List:")
    print_list(ll.head)
    # Merge Sort
    ll.head = ll.merge_sort(ll.head)
    print("Sorted List:")
    print_list(ll.head)
