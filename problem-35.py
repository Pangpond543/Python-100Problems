def print_diamond_pattern(n: int) -> None:
    for row in range(n + 1):
        print("*" * row)
    for row in range(n - 1, 0, -1):
        print("*" * row)
        
print_diamond_pattern(3)

#-----------------------------
def print_diamond_pattern_2(n: int) -> None:
    # เพิ่ม
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()

    # ลด
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end="")
        print()
        
print_diamond_pattern_2(6)