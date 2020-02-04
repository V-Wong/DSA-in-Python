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

    def insert_after_node(self, key, val):
        if self.head:
            cur = self.head
            while cur and cur.val != key:
                cur = cur.next
            
            if cur:
                if not cur.next:
                    self.append(val)
                else:
                    new_node = Node(val)
                    new_node.next = cur.next
                    cur.next.prev = new_node
                    cur.next = new_node

    def insert_before_node(self, key, val):
        if self.head:
            cur = self.head
            while cur and cur.val != key:
                cur = cur.next
            
            if cur:
                if not cur.prev:
                    self.prepend(val)
                else:
                    new_node = Node(val)
                    new_node.next = cur
                    cur.prev.next = new_node
                    cur.prev = new_node

    def delete(self, key):
        cur = self.head
        while cur.val != key:
            cur = cur.next

        if cur:
            if not cur.next and not cur.prev:
                self.head = None
            elif not cur.prev:
                self.head = cur.next
                self.head.prev = None
            elif not cur.next:
                cur.prev.next = None
            else:
                prev_node, next_node = cur.prev, cur.next
                prev_node.next = next_node
                next_node.prev = prev_node

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
        l.insert_after_node(1, "after 1")
        l.insert_after_node(100, "end")
        l.insert_before_node(-100, "start")
        l.insert_before_node(1, "before 1")
        l.delete("start")
        l.delete(100)
        l.delete(-100)
        l.delete("end")
        l.print_list()

