def calculate_profit(sales: tuple[float, float, float, float, float], costs: tuple[float, float, float, float,float]) -> tuple[tuple[float, float, float, float, float], float]:
    profit = ()
    for s, c in zip(sales, costs):
        profit += (s - c,) # ห้ามลืมใส่ , ต่อท้ายทุกครั้ง เพื่อนให้เพิ่มเข้า tuple ได้ /ต้องทำให้มันเป็น tuple ที่มีสมาชิก 1 ตัว
    return (profit, sum(profit))

print(calculate_profit((10000.0, 15000.0, 20000.0, 25000.0, 30000.0),  (7000.0, 8000.0,9000.0, 11000.0, 12000.0)))