from doubly_linked_list import DoublyLinkedList


def pair_sum(target, numbers):
    l = DoublyLinkedList()
    l.list_from_array(numbers)

    solutions = []

    cur = l.head
    while cur:
        nxt = cur.next
        while nxt:
            if cur.val + nxt.val == target:
                solutions.append((cur.val, nxt.val))
            nxt = nxt.next
        cur = cur.next

    return solutions


if __name__ == "__main__":
    test_cases = {
        5: [1, 2, 3, 4, 5],
        3: [0, 3, 1, 2, 0],
        0: []
    }

    for target, numbers in test_cases.items():
        print(pair_sum(target, numbers))