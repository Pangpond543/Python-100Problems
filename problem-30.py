def calculate_set_differences(set1: set, set2: set) -> tuple[set, set]:
    result = set1 - set2    #เอาของใน set1 แล้วตัดตัวที่มีอยู่ใน set2 ออก
    result2 = set2 - set1   #เอาด้านขวาลบด้านซ้ายเอา แล้วเอาค่าด้านซ้าย
    return (result, result2)

print(calculate_set_differences({'a', 'b', 'c'}, {'b', 'c', 'd'}))

#----------------------------------
def calculate_set_differences_2(set1: set, set2: set) -> tuple[set, set]:
    result = set()
    result2 = set()
    for s1 in set1:
        if not s1 in set2:  # ถ้าไม่ได้อยู่
            result.add(s1)
    for s2 in set2:
        if not s2 in set1:
            result2.add(s2)
    return (result,result2)

print(calculate_set_differences_2({'a', 'b', 'c'}, {'b', 'c', 'd'}))
