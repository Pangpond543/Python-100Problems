def reverse_string(s: str):
    str = list(s)
    str.reverse()
    return "".join(str)

print(reverse_string("Hello World! pond"))