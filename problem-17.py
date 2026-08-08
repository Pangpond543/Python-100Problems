def is_word_in_list(word_list: list[str], search_term: str) -> bool:
    return search_term in word_list

print(is_word_in_list(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew","kiwi", "lemon"], "cherry"))



def is_word_in_list_2(word_list: list[str], search_term: str) -> bool:
    for s in word_list:
        if search_term == s:
            return True
    return False

print(is_word_in_list_2(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew","kiwi", "lemon"], "cherry"))