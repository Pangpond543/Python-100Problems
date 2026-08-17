def count_words(words):
    dict = {}
    
    for w in words:
        if w in dict:
            dict[w] += 1
        else:
            dict[w] = 1
            
    return dict    
    
print(count_words(["apple", "banana", "apple", "orange", "banana", "apple"]))