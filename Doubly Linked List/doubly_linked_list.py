class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node = Node(val)
            new_node.prev = cur
            cur.next = new_node

    def prepend(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            new_node = Node(val)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        traversal = []

        cur = self.head
        while cur:
            traversal.append(cur.val)
            cur = cur.next

        print(traversal)

    def list_from_array(self, array):
        for num in array:
            self.append(num)


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5, 6],
        [1],
        []
    ]

    for test_case in test_cases:
        l = DoublyLinkedList()
        l.list_from_array(test_case)
        l.prepend(-100)
        l.append(100)
        l.print_list()

