from linked_list import LinkedList, Node


def kth_to_last(linked_list: LinkedList, k: int) -> Node:
    if k < 0:
        return None
    slow = fast = linked_list.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    
    if fast is None:
        return None

    while fast.next:
        slow = slow.next
        fast = fast.next
    return slow


linked_list = LinkedList([1, 2, 3, 4, 5])

print(kth_to_last(linked_list, 2))  # 3
print(kth_to_last(linked_list, 4))  # 5
