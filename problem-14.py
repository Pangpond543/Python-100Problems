def collect_unique_words(s: list):
    return sorted(list(set(s))) #sorted เรียงคำ

print(collect_unique_words(["apple", "banana", "apple", "cherry", "date", "banana", "elderberry"]))
