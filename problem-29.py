def set_operations(set1: set, set2: set) -> tuple[set, set]:
    union = set1.union(set2)
    intersec = set1.intersection(set2)
    return (union, intersec)

print(set_operations({'a', 'e', 'i', 'o', 'u'}, {'h', 'e', 'l', 'l', 'o'}))

#-------------------------------------
def set_operations_2(set1: set, set2: set) -> tuple[set, set]:
    union = set()
    intersec = set()
    for s in set1:
        for s2 in set2: 
            union.add(s)    
            union.add(s2)   # เอามายำรวมกัน เพราะยังไง set ก็ไม่เพิ่มตัวที่ซํ้าเข้าไปเพิ่ม
        if s in set2:
            intersec.add(s)
    return (union, intersec)

print(set_operations_2({'a', 'e', 'i', 'o', 'u'}, {'h', 'e', 'l', 'l', 'o'}))
        