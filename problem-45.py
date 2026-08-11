def calculate_annual_return(initial_investment: float, final_investment: float, years: int) -> float:
    return round(100 * ((final_investment / initial_investment) ** (1 / years) - 1), 2)

print(calculate_annual_return(1000, 1500, 5))