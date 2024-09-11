# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter­
# secting node. Note that the intersection is defined based on reference, not value.That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

from linked_list import LinkedList, Node

def intersection(l1: LinkedList, l2: LinkedList) -> bool:
    c1 = l1.head
    c2 = l2.head

    len1 = 0
    len2 = 0

    while c1:
        len1 += 1
        c1 = c1.next
    while c2:
        len2 += 1
        c2 = c2.next
    
    c1 = l1.head
    c2 = l2.head

    if len1 > len2:
        for _ in range(len1 - len2):
            c1 = c1.next
    else:
        for _ in range(len2 - len1):
            c2 = c2.next
    
    while c1 and c2:
        if c1 == c2:
            return True
        c1 = c1.next
        c2 = c2.next
    return False
    