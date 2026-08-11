def calculate_jumps(d: int, s: int) -> int:
    count = (d + s - 1) // s    # d+s-1 เพราะว่า บวกตัวมันเองไป เพื่อที่จะให้มันเลยไปเลขต่อไป และ -1 เพื่อไม่ให้มันถึงเลขต่อไป เพื่อที่จะปัดเศษลงด้วย"//"  / ใน python ไม่มีการปัดเศษขึ้น เว้นแต่จะ import math
    return count

print(calculate_jumps(20, 7))