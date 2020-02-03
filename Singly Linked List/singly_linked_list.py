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

    def iterative_reverse(self):
        prev = None
        cur = self.head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        self.head = prev

    def recursive_reverse(self):
        def _reverse(cur, prev):
            if not cur:
                return prev
            else:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

                return _reverse(cur, prev)

        self.head = _reverse(self.head, None)

    def merge_sorted(self, list2):
        if not self.head:
            return list2
        elif not list2:
            return self.head

        p, q = self.head, list2.head
        
        if p.val < q.val:
            new_head = p
            p = p.next
        else:
            new_head = q
            q = q.next

        cur = new_head
        while p and q:
            if p.val <= q.val:
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next
            cur = cur.next
        if not p:
            cur.next = q
        if not q:
            cur.next = p

        return new_head

    def delete_duplicates(self):
        seen = set()

        prev = None
        cur = self.head

        while cur:
            if cur.val in seen:
                prev.next = cur.next
            else:
                seen.add(cur.val)
                prev = cur
            cur = prev.next

    def rotate_right(self, k):
        if not self.head:
            return None
        
        k %= self.length(self.head)

        p, q = self.head, self.head
        
        for _ in range(k):
            q = q.next
            
        while q.next:
            p = p.next
            q = q.next
            
        q.next = self.head
        new_head = p.next
        p.next = None
            
        self.head = new_head

    def nth_last(self, n):
        p, q = self.head, self.head

        for _ in range(n - 1):
            q = q.next
            if not q:
                return None

        while p and q.next:
            p = p.next
            q = q.next

        return p.val

    def count_occurences(self, val):
        def _count(cur, val):
            if not cur:
                return 0
            elif cur.val == val:
                return 1 + _count(cur.next, val)
            else:
                return _count(cur.next, val)

        return _count(self.head, val)

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
        l.recursive_reverse()
        l.print_list()
        print(f"2nd last: {l.nth_last(2)}")
        print(f"Length: {l.length()}")

    print("\nTest sorted merge:")
    
    l0 = LinkedList()
    l1 = LinkedList()
    for num in [1, 2, 3, 4, 5]:
        l0.append(num)
    for num in [2, 4, 5, 6, 10]:
        l1.append(num)

    new_list = LinkedList()
    new_list.head = l0.merge_sorted(l1)
    new_list.print_list()

    print("\nTest delete duplicates:")
    l = LinkedList()
    for num in [1, 1, 1, 2, 3, 3, 4, 3, 3, 3, 5, 6, 3, 3]:
        l.append(num)
    l.delete_duplicates()
    l.print_list()

    print("\nTest count occurences:")
    l = LinkedList()
    for num in [1, 1, 1, 2, 3, 3, 4, 3, 3, 3, 5, 6, 3, 3]:
        l.append(num)
    l.print_list()
    print(f"{l.count_occurences(1)} occurences of 1")

    print("\nTest rotate right:")
    l = LinkedList()
    for num in [1, 1, 1, 2, 3, 3, 4, 3, 3, 3, 5, 6, 3, 3]:
        l.append(num)
    l.print_list()
    print("Rotate 2: ")
    l.rotate_right(2)
    l.print_list()
    print("Rotate 10: ")
    l.rotate_right(10)
    l.print_list()