def print_number_pattern(rows: int) -> None:
    for row in range(1, rows + 1):
        deshes = rows - row
        
        for d in range(deshes):
            print("-", end="")
        
        for i in range(row, 0, -1):
            print(i, end="")
        print()
            
print_number_pattern(5)