# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.
# Hints: #7, #30, #71, #95, #109

from linked_list import LinkedList, Node


def sum_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    current1 = l1.head
    current2 = l2.head
    cary = 0
    result = LinkedList()

    while current1 or current2:
        if current1:
            cary += current1.data
            current1 = current1.next
        if current2:
            cary += current2.data
            current2 = current2.next
        result.append(cary % 10)
        cary = cary // 10

    if cary:
        result.append(cary)
    return result


l1 = LinkedList([7, 1, 6])
l2 = LinkedList([5, 9, 2])
print(sum_lists(l1, l2))

l1 = LinkedList([6, 1, 7])
l2 = LinkedList([2, 9, 5])
print(sum_lists(l1, l2))

l1 = LinkedList([6, 1, 7])
l2 = LinkedList([2, 9, 5, 1])
print(sum_lists(l1, l2))
