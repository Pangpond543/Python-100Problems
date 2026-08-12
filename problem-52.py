def group_by_unit_digit(numbers: list[int]) -> list[list[int]]:
    result = [[],[],[],[],[],[],[],[],[],[]]
    for num in numbers:
        result[num % 10].append(num)    # mod 10 แล้วจะได้หลักหน่วยมา
        
    return (result)

print(group_by_unit_digit([21, 34, 51, 23, 37, 44, 60, 11, 91, 99]))        
