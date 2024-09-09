# Deleting a Node from a Singly Linked List

from linked_list import Node

def remove_middle_node(node: Node) -> bool:
    if node is None or node.next is None:
        return False
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
    return True