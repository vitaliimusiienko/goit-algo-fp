from linked_list import LinkedList

def reverse_linked_list(linked_list: LinkedList) -> None:
    prev = None
    current = linked_list.head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    linked_list.head = prev