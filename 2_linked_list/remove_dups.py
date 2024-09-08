# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from linked_list import LinkedList

# O(n) time complexity
# O(n) space complexity
def remove_dups(linked_list: LinkedList) -> LinkedList:
    if linked_list.head is None:
        return linked_list

    seen = dict()
    node = linked_list.head
    prev = None
    while node:
        is_duplicate = seen.get(node.data, False)
        if is_duplicate:
            prev.next = node.next
        else:
            seen[node.data] = True
            prev = node
        node = node.next

    return linked_list

# O(n^2) time complexity
# O(1) space complexity
def remove_dups_no_buffer(linked_list: LinkedList) -> LinkedList:
    if linked_list.head is None:
        return linked_list

    current = linked_list.head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return linked_list
