from circular_linked_list import CircularLinkedList


def josephus_permutation(n):
    l = CircularLinkedList()

    for i in range(1, n + 1):
        l.append(i)

    cur = l.head
    while cur.next != cur:
        l.delete_node(cur.next)
        cur = cur.next
    
    return cur.val


if __name__ == "__main__":
    print(josephus_permutation(17))