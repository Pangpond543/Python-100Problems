def count_word_occurrences(words: list[str]) -> dict[str, int]:
    count = {}
    for s in words:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    return count

print(count_word_occurrences(["apple", "banana", "apple", "orange", "banana", "apple"]))