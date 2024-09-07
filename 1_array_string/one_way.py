# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

def replace_away(str1: str, str2: str) -> bool:
    found_difference = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found_difference:
                return False
            found_difference = True
    return True

def insert_away(str1: str, str2: str) -> bool:
    index1 = 0
    index2 = 0
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index1 += 1
        else:
            index1 += 1
            index2 += 1
    return True

def one_away(str1: str, str2: str) -> bool:
    diff_length = len(str1) - len(str2)
    if abs(diff_length) > 1:
        return False
    
    if diff_length == 0:
        return replace_away(str1, str2)
    elif diff_length == 1:
        return insert_away(str1, str2)
    else:
        return insert_away(str2, str1)

print(one_away("pale", "ple")) # True
print(one_away("pales", "pale")) # True
print(one_away("pale", "bale")) # True
print(one_away("pale", "bake")) # False