def find_non_multiples(start: int, end: int) -> list:
    result = []
    for i in range(start,end+1):
        if i % 3 != 0 and i % 4 != 0 and i % 5 != 0:
            result.append(i)
    return result

print(find_non_multiples(10, 25))
