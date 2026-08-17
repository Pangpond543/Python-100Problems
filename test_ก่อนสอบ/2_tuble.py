#หาค่าสูงสุด/ต่ำสุด
def analyze_numbers(numbers):
    result = ()
    count = 0
    max_int = max(numbers)
    
    for i in numbers:
        if i == max_int:
            count += 1
            
    result += (min(numbers), max_int, count)
    
    return result
    
print(analyze_numbers((12, 5, 20, 8, 20, 3)))