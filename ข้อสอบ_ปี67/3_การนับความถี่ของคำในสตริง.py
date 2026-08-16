def word_frequency(text: str) -> dict:
    list_s = text.lower().split()
    
    dict = {}
    for w in list_s:
        if w in dict:
            dict[w] += 1
        else:
            dict[w] = 1
                
    return dict
    
print(word_frequency("Hello world! Hello everyone"))
print(word_frequency("This is a test. This test is easy"))