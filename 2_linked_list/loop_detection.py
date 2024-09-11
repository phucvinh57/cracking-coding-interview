# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.

from linked_list import LinkedList, Node

def loop_direction(linked_list: LinkedList) -> Node | None:
    hash: dict[Node, bool] = dict()
    current = linked_list.head
    while current:
        if hash.get(current):
            return current
        
        hash[current] = True
        current = current.next

node = Node(4)
linked_list = LinkedList([1, 2, 3])
linked_list.append_node(node)
linked_list.append(5)
linked_list.append(6)
# linked_list.append_node(node)

print(loop_direction(linked_list)) 
