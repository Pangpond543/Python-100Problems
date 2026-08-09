def calculate_median(lst: list[int]) -> float:
    sort = sorted(lst)
    n = len(sort)
    
    if n % 2 == 1:
        medain = sort[n // 2]
    elif n % 2 == 0:
        medain = (sort[(n // 2) - 1] + sort[(n // 2)]) / 2 
        
    #print(sort)
    return medain
    
print(calculate_median([8, 4, 7, 4, 6, 2, 10, 9, 3, 7, 1, 5]))
