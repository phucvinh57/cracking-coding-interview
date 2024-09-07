# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# Approach 1: Using a hash map to store the characters of the string.
# Time complexity: O(n)
def is_unique(s: str) -> bool:
    seen = dict()
    for char in s:
        if seen.get(char):
            return False
        seen[char] = True
    return True

# Approach 2: Sorting the string and checking if there are any adjacent characters that are the same.
# Time complexity: O(nlogn)
def is_unique_2(s: str) -> bool:
    s = sorted(s)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

print(is_unique_2("helo")) # False