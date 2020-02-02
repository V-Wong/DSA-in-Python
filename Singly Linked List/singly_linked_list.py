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

        l.print_list()