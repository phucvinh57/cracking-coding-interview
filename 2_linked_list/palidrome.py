# Palindrome: Implement a function to check if a linked list is a palindrome
from linked_list import LinkedList

# Time complexity: O(n)
# Space complexity: O(n)
def is_palindrome(l: LinkedList) -> bool:
    arr = []
    current = l.head
    while current:
        arr.append(current.data)
        current = current.next
    
    return arr == arr[::-1]
