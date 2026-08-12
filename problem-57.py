def compare_string_lengths(str1: str, str2: str) -> str:
    if len(str1) > len(str2):
        result = (f'The first string is longer by {len(str1) - len(str2)} character(s).')
    elif len(str2) > len(str1):
        result = result = (f'The second string is longer by {len(str2) - len(str1)} character(s).')
    else:
        result = "Two str is equal"
    return result

print(compare_string_lengths("apple", "banana"))