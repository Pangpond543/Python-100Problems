def process_scores(scores: list) -> list:
    result = []
    
    for i in scores:
        if i >= 50:
            result.append(i + 5)
        
    return sorted(result)
    
print(process_scores([75, 42, 90, 68, 55, 90, 30]))