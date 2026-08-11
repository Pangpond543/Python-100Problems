def remove_word(sentence: str, word_to_remove: str) -> str:
    remove = sentence.replace(" " + word_to_remove, "") # จะมีปัญหาตรงที่ถ้าข้างหน้าไม่มี เว้นวรรค จะใช้ไม่ได้
    return remove
print(remove_word("Python is a popular programming language.", "popular"))

#----------------------------------------
def remove_word_2(sentence: str, word_to_remove: str) -> str:
    world = sentence.split()
    result = []
    for s in world:
        if word_to_remove != s:
            #print(s)
            result.append(s)
    return " ".join(result)
print(remove_word_2("Python is a popular programming language.", "popular"))

