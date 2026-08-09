def calculate_statistics(t: tuple[int, ...]) -> tuple[tuple[int, ...], int, int, int, float]:
    squared = ()
    for i in t:
        squared = squared + (i ** 2,)
    max_value = max(squared)
    min_value = min(squared)
    total = sum(squared)
    average = total / len(squared) #เครื่องหมาย / คือการหารแบบ float อยู่แล้ว ถ้าใช้ // จะเป็นการหารแบบ int

    result = (squared, max_value, min_value, total, average)

    return result

print(calculate_statistics((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))