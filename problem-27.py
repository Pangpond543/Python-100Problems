def build_set() -> set[int]:
    int_set = set()
    while not len(int_set) == 5:    #วนลูปจนกว่าจะได้จำนวนเต็ม 5 
        num = int(input("User enters: "))
        if num in int_set: 
            while num in int_set:   # วนลูปจนกว่าจะได้ตัวเลขที่ไม่ซ้ำกัน
                num = int(input("Please enter a different number: "))
            int_set.add(num)
        else:
            int_set.add(num)
    return int_set

print(build_set())
 
 #----------------------------------------------------------------
 
def build_set_2() -> set[int]:
    int_set = set()

    while len(int_set) < 5:
        num = int(input("Enter number: "))

        while num in int_set:
            num = int(input("Please enter a different number: "))

        int_set.add(num)

    return int_set

print(build_set_2())