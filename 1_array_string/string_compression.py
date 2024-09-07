# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def string_compression(s: str) -> str:
    compressed : list[[str, int]] = []
    current_char = s[0]
    current_count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            current_count += 1
        else:
            compressed.append([current_char, current_count])
            current_char = s[i]
            current_count = 1
        
    compressed.append([current_char, current_count])

    if len(compressed) * 2 >= len(s):
        return s
    
    return "".join([char + str(count) for char, count in compressed])

print(string_compression("aabcccccaaa")) # "a2b1c5a3"
print(string_compression("aabbcc")) # "aabbcc"