class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            prev = self.head
            while prev.next:
                prev = prev.next

            prev.next = Node(val)

    def prepend(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

    def insert_after_node(self, prev_node, val):
        if not prev_node:
            return

        next_node = prev_node.next
        new_node = Node(val)
        new_node.next = next_node
        prev_node.next = new_node

    def delete_by_value(self, val):
        if not self.head:
            return None
        elif self.head.val == val:
            self.head = self.head.next
        else:
            prev = None
            cur = self.head
            while cur and cur.val != val:
                prev = cur
                cur = cur.next

            if cur:
                prev.next = cur.next

    def delete_by_position(self, pos):
        if self.head:
            if pos == 0:
                self.head = self.head.next
            else:
                prev = None
                cur = self.head
                for _ in range(pos):
                    prev = cur
                    cur = cur.next

                    if not cur:
                        break

                if cur:
                    prev.next = cur.next

    def length(self, node=-1):
        if node == -1:
            node = self.head

        if not node:
            return 0
        else:
            return 1 + self.length(node.next)

    def print_list(self):
        traversal = []

        cur = self.head
        while cur:
            traversal.append(cur.val)
            cur = cur.next

        print(traversal)

    
if __name__ == "__main__":
    test_cases = [
        [1, 2, 4, 5, 6, 7],
        [1, 3, 4, 1, 2, 1],
        [1],
        []
    ]

    for test_case in test_cases:
        l = LinkedList()
        for num in test_case:
            l.append(num)

        l.insert_after_node(l.head, "After head")
        l.prepend("first")
        l.delete_by_position(7)
        l.print_list()
        print(f"Length: {l.length()}")