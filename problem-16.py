def insert_at_front(words: list[str]) -> list[str]:
    result = []
    for s in words:
        result.insert(0, s)
    return result
    
print(insert_at_front(["apple", "banana", "cherr"]))