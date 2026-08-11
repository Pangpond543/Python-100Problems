def calculate_discounted_prices(prices: list[float], discount_percentage: float) -> list[float]:
    result = []
    for p in prices:
        discount = round(p * (1 - discount_percentage / 100), 2) # round ปัดเศษทิ้ง ให้เหลือ 2 ตำแหน่ง
        result.append(discount)
        
    return result

print(calculate_discounted_prices([100.0, 250.0, 75.0], 20.0))