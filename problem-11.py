def contains_vowel(s: str):
    str = list(s)
    for char in str:
        if char in "aeiouAEIOU":
            return True
        #print(char)
    return False

print(contains_vowel("Hello World!"))
print(contains_vowel("sdasd"))
print(contains_vowel("Hdgffdg"))
        