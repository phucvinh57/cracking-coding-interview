# String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").

def is_substring(s1: str, s2: str) -> bool:
    return s2 in s1

def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return is_substring(s1 + s1, s2)