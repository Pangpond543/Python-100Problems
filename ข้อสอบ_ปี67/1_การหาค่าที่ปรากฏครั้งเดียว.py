def find_single_occurrence_numbers(numbers: list) -> list :
    result = []
    for i in numbers:
        count = 0
        for check in numbers:
            if i == check:
                count += 1
        # print(count)
        if count == 1:
            result.append(i)
    return result
    
print(find_single_occurrence_numbers([4, 5, 6, 4, 7, 5, 8]))
print(find_single_occurrence_numbers([1, 2, 3, 4, 5, 6, 7]))
print(find_single_occurrence_numbers([1, 1, 1, 1, 1, 1,]))