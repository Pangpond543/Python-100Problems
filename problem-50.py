def find_words_of_length(words: list[str], length: int) -> list[str]:
    result = []
    for w in words:
        count = 0
        for c in w:
            count += 1
        if count == 5:
            result.append(w)
    return result

print(find_words_of_length(["apple", "banana", "cherry", "date", "fig", "grape"], 5))