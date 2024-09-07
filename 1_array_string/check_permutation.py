# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# Solution 1: Sort the strings and compare them
# Time complexity: O(nlogn)
def check_permutation(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

# Solution 2: Using a hash map to store the characters of the strings
# Time complexity: O(n)
def check_permutation_2(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    seen = dict()
    for char in str1:
        if seen.get(char):
            seen[char] += 1
        else:
            seen[char] = 1
    for char in str2:
        if seen.get(char):
            seen[char] -= 1
        else:
            return False
    return all(value == 0 for value in seen.values())