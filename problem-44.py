def calculate_investment_growth(principal: float, annual_rate: float, years: int) -> list[float]:
    annual = []
    for y in range(1, years + 1):
        annual.append(round(principal * (1 + annual_rate / 100) ** y, 2))
    return annual

print(calculate_investment_growth(1000, 5, 5))
        