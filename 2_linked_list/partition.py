# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from linked_list import LinkedList, Node


def partition(linked_list: LinkedList, p: int) -> Node:
    left = LinkedList()
    right = LinkedList()

    current = linked_list.head
    while current:
        if current.val < p:
            left.push(current.val)
        else:
            right.push(current.val)
        current = current.next
    
    if left.tail:
        left.tail.next = right.head
    return left.head if left.head else right.head

print(
    partition(LinkedList([3, 5, 8, 6, 10, 2, 1]), 5)
)  # 3 -> 2 -> 1 -> 5 -> 8 -> 6 -> 10
