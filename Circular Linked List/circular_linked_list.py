class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            self.head.next = self.head
        else:
            new_node = Node(val)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node

        self.head = new_node

    def print_list(self):
        traversal = []
        cur = self.head

        while cur:
            traversal.append(cur.val)
            cur = cur.next

            if cur == self.head:
                break

        print(traversal)

    def list_from_array(self, array):
        for val in array:
            self.append(val)


if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [1, 2, 3]
    ]

    for test_case in test_cases:
        l = CircularLinkedList()
        l.list_from_array(test_case)
        l.prepend(-100)
        l.append(100)
        l.print_list()