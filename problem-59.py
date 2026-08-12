from datetime import date

def days_between_dates(date1: str, date2: str) -> int:
    y1, m1, d1 = map(int, date1.split("-"))
    y2, m2, d2 = map(int, date2.split("-"))
    
    d3 = date(y1, m1, d1)
    d4 = date(y2, m2, d2)
    
    result = d3 - d4
    
    return abs(result.days)
    
print(days_between_dates("2024-08-01", "2024-08-10"))