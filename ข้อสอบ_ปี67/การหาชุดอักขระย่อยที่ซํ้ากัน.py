def find_repeated_substrings(s: str) -> list :
    dict = {}
    
    for st in range(len(s)):
        for se in range(st + 2, len(s) + 1):
            # print(s[st:se])
            ss = s[st:se]
            if ss in dict:
                dict[ss] += 1
            else:
                dict[ss] = 1
                
    result = []
                
    for a, b in dict.items():
        if b >= 2:
            result.append(a)
                
    return result
    
print(find_repeated_substrings("banana"))
print(find_repeated_substrings("abcabcabc"))

#----------------------------------------------------

def find_repeated_substrings_2(s: str) -> list :
    list_ = []
    
    for st in range(len(s)):
        for se in range(st + 2, len(s) + 1):
            list_.append(s[st:se])
    
    result = []     # ['an', 'ana', 'na', 'an', 'ana', 'na']
    
    for st in  list_:
        count = 0
        for se in list_:
            if st == se:
                count += 1
        if count >= 2:
            result.append(st)
                
            
    return list(set(result))    #เพื่อให้ set รวมค่าให้มันเหลือค่าเดียว

print(find_repeated_substrings_2("banana"))
print(find_repeated_substrings_2("abcabcabc"))