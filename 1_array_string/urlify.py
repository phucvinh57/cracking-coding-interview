# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters,and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

def urlify(s: str) -> str:
    # HACK: return s.replace(" ", "%20")
    num_spaces = 0
    for char in s:
        if char == " ":
            num_spaces += 1

    new_length = len(s) + num_spaces * 2
    new_s = [""] * new_length
    index = 0
    for i in range(0, len(s)):
        if s[i] == " ":
            new_s[index] = "%"
            new_s[index + 1] = "2"
            new_s[index + 2] = "0"
            index += 3
        else:
            new_s[index] = s[i]
            index += 1
    return "".join(new_s)

print(urlify("Mr John Smith ")) # "Mr%20John%20Smith"
