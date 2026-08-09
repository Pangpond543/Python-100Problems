def check_membership(s: set, value: str) -> bool:
    return value in s

print(check_membership({1, 2, 3, 'a', 'e', 'i', 'o', 'u', "red", "green", "blue"}, 2))