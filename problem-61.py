def calculate_total_payment(num_bills: int, bills: list[float]) -> float:
    s = sum(bills)
    if s >= 10000:
        result = s * (1 - 20 / 100)
    elif s >= 5000:
        result = s * (1 - 10 / 100)
    elif s >= 1000:
        result = s * (1 - 5 / 100)
        
    return result

print(calculate_total_payment(3, [3000, 4000, 3500]))