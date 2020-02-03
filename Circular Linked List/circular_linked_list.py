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

    def delete(self, val):
        if self.head:
            if self.head.val == val:
                if self.head.next == self.head:
                    self.head = None
                else:
                    new_head = self.head.next
                    cur = self.head.next
                    while cur.next != self.head:
                        cur = cur.next
                    cur.next = new_head
                    self.head = new_head
            else:
                prev = None
                cur = self.head
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.val == val:
                        prev.next = cur.next

    def delete_node(self, node):
        if self.head:
            if self.head == node:
                if self.head.next == self.head:
                    self.head = None
                else:
                    new_head = self.head.next
                    cur = self.head.next
                    while cur.next != self.head:
                        cur = cur.next
                    cur.next = new_head
                    self.head = new_head
            else:
                prev = None
                cur = self.head
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur == node:
                        prev.next = cur.next

    def split_list(self):
        length = len(self)

        if length == 0 or length == 1:
            return CircularLinkedList()

        midpoint = length // 2

        prev = None
        cur = self.head
        for _ in range(midpoint):
            prev = cur
            cur = cur.next

        prev.next = self.head

        new_list = CircularLinkedList()
        while cur and cur != self.head:
            new_list.append(cur.val)
            cur = cur.next

        return new_list

    def __len__(self):
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next
            if cur == self.head:
                break

        return length

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
        l.delete(1)
        l.print_list()

    print("\nTest split list:")
    l = CircularLinkedList()
    l.list_from_array([1])
    right_half = l.split_list()
    l.print_list()
    right_half.print_list()