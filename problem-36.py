def print_diamond_pattern(n: int) -> None:
    for i in range(1, n // 2 + 1):
        stars = n // 2 - i + 1  # n//2 คือจำนวน * แต่ละข้าง แล้วเอา i มาลบเพื่อที่จะให้มันลดตามแถวอย่างละข้าง +1ชดเชย เพราะ i เริ่มที่ 1
        hyphens = (i-1) * 2
        
        for j in range(stars):
            print("*", end=" ")

        for j in range(hyphens):
            print("-", end=" ")

        for j in range(stars):
            print("*", end=" ")
            
        print()
            
    for i in range(n // 2 - 1, 0, -1):
        stars = n // 2 - i + 1
        hyphens = (i-1) * 2
        
        for j in range(stars):
            print("*", end=" ")

        for j in range(hyphens):
            print("-", end=" ")

        for j in range(stars):
            print("*", end=" ")
            
        print()

print_diamond_pattern(10)

#แถวที่  1   2   3   4   5
    # 10 → 8 → 6 → 4 → 2 จำนวน *
    #  0 → 2 → 4 → 6 → 8 จำนวน -