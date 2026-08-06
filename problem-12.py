def replace_characters(s: str):
    str = s.lower().replace("a", "@").replace("l", "1").replace("o", "0")
    return str
print(replace_characters("HLlo World! pond"))