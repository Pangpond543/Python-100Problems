def calculate_median(provinces: dict[str, int]) -> list[tuple[str, int]]:
    sort = sorted(provinces.values())
    
    if len(sort) % 2 == 1:
        median = sort[len(sort) // 2]
    elif len(sort) % 2 == 0:
        median = (sort[(len(sort) // 2) - 1] + sort[(len(sort) // 2)]) / 2
        
    result = []
        
    for p, n in provinces.items():
        if n == median :
            result.append((p, int(n)))
            
    return result
    
print(calculate_median({'Thailand':76, 'Laos':17, 'Vietnam':58, 'Japan':47, 'China':23}))