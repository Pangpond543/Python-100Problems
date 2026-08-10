def print_rectangle_pattern(rows: int, columns: int) -> None:
    for row in range(rows):
        print() # โดยปกติ print จะมี end="\n" บอกให้ขึ้นบรรทัดใหม่อยู่แล้ว
        for column in range(columns):
            print("*", end=" ") # เราเปลื่ยน end เป็น " "
            
print_rectangle_pattern(5, 5)