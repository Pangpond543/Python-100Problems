def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    rates = {
            "USD": 1,
            "EUR": 0.85,
            "GBP": 0.75,
            "JPY": 110,
            "THB": 32.0
        }
    
    USD_ = (amount / rates.get(from_currency))  # แปลงเป็นค่าเงิน USD ก่อน โดยการหารด้วยเรทค่าเงินแรก
    return round(USD_ * rates.get(to_currency), 2)  # แล้วก็แปลงค่าเงินจาก USD เป็นค่าเงินปลายทางที่จะเปลื่ยน โดยการคูณเรทเหมือนข้อ 55

print(convert_currency(100.0,  "USD", "EUR"))