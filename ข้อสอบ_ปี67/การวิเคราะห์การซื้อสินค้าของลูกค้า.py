def analyze_purchases(purchases: list) -> dict:
    cust = {}                   #{'cust1': {'electronics': {'labtop': 2, 'mouse': 1}}, 'cust2': {'groceries': {'apple': 2, 'banana': 1}}, 'cust3': {'groceries': {'banana': 1, 'apple': 1}, 'electronics': {'camera': 1}}}
    product = {}                #{'electronics': {'labtop': 2, 'mouse': 1, 'camera': 1}, 'groceries': {'apple': 3, 'banana': 2}}
    result = {}
    
    for cut, cat, pro in purchases:
        if cut not in cust:
            cust[cut] = {}
        if cat not in cust[cut]:
            cust[cut][cat] = {}
        if pro in cust[cut][cat]:
            cust[cut][cat][pro] += 1
        else:
            cust[cut][cat][pro] = 1
        
        if cat not in product:
            product[cat] = {}
        if pro in product[cat]:
            product[cat][pro] += 1
        else:
            product[cat][pro] = 1
            
    for cut, cat_dict in cust.items():
        for cat, pro_dict in cat_dict.items():
            result[cat]
            for pro, value in pro_dict.items():
                if value >= 2:
                    total =
                
        
            
    
    return product
        
purchases = [
    ("cust1", "electronics", "labtop"),
    ("cust2", "groceries", "apple"),
    ("cust1", "electronics", "labtop"),
    ("cust1", "electronics", "mouse"),
    ("cust2", "groceries", "apple"),
    ("cust2", "groceries", "banana"),
    ("cust3", "groceries", "banana"),
    ("cust3", "groceries", "apple"),
    ("cust3", "electronics", "camera")
]

print(analyze_purchases(purchases))