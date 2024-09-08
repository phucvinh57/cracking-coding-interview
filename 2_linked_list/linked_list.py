class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, arr: list | None = None):
        self.head = None
        self.tail = None
        if arr:
            for data in arr:
                self.append(data)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    
    def __str__(self) -> str:
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return '->'.join(result)