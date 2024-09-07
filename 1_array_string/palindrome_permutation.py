# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input:Tact Coa
# Output:True (permutations: "taco cat", "atco eta", etc.)

def palindrome_permutation(s: str) -> bool:
    # Remove spaces
    s = s.replace(" ", "")
    seen = dict()
    for char in s:
        if seen.get(char):
            seen[char] += 1
        else:
            seen[char] = 1
    odd_count = 0
    for value in seen.values():
        if value % 2 == 0:
            continue
        odd_count += 1
        if odd_count > 1:
            return False
    return True