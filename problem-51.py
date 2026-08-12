def separate_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    even_num = []
    odd_num = []
    for num in numbers:
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)
            
    return (even_num, odd_num)

print(separate_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        