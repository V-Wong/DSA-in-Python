from circular_linked_list import Node
from circular_linked_list import CircularLinkedList


def is_circular_linked_list(l):
    cur = l

    while cur and cur.next != l:
        cur = cur.next

    if cur:
        return True
    else:
        return False


if __name__ == "__main__":
    linear_list = Node(0)
    cur = linear_list
    for num in [1, 2, 3, 4, 5]:
        cur.next = Node(num)
        cur = cur.next

    circular_list = CircularLinkedList()
    circular_list.list_from_array([1, 2, 3, 4, 5])

    print(is_circular_linked_list(linear_list))
    print(is_circular_linked_list(circular_list.head))