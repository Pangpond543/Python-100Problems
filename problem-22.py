def create_dictionary(list1: list[int], list2: list[str]) -> dict[int, str]:
    dict = {}
    for i in range(len(list1)):
        dict[list1[i]] = list2[i]
    return dict

print(create_dictionary([1, 2, 3, 4], ["blue", "green", "pink", "yellow"]))

#--------------------------------------------------------------

def create_dictionary_2(list1: list[int], list2: list[str]) -> dict[int, str]:
    dict = {}
    for i, j in zip(list1, list2): # zip() จะเอา list1 กับ list2 มาจับคู่กันเป็น tuple แล้วเอาไป unpack เป็น i กับ j
        dict[i] = j
    return dict

print(create_dictionary_2([1, 2, 3, 4], ["blue", "green", "pink", "yellow"]))

#--------------------------------------------------------------

def create_dictionary_3(list1: list[int], list2: list[str]) -> dict[int, str]:
    dict = {}
    for i in range(len(list1)):
        dict.update({list1[i]: list2[i]}) # update() จะเอา dict ใหม่ที่เราสร้างขึ้นมาใส่เข้าไปใน dict เดิม
    return dict

print(create_dictionary_3([1, 2, 3, 4], ["blue", "green", "pink", "yellow"]))

#--------------------------------------------------------------

def create_dictionary_4(list1: list[int], list2: list[str]) -> dict[int, str]:
    return dict(zip(list1, list2))  # zip() จะเอา list1 กับ list2 มาจับคู่กันเป็น tuple แล้วเอาไปสร้าง dict โดยใช้ dict() สร้าง dict จาก tuple ของ key-value pairs

print(create_dictionary_4([1, 2, 3, 4], ["blue", "green", "pink", "yellow"]))
