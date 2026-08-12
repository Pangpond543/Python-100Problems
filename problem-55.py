def convert_thb_to_currency(amount: float, to_currency: str) -> float:
    rates = {
        "USD": 0.030,
        "EUR": 0.027,
        "GBP": 0.024,
        "JPY": 3.4,
        "AUD": 0.045
    }
    return round((amount * rates.get(to_currency)), 1)

print(convert_thb_to_currency(1000.0, "JPY"))