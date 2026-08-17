def student_summary(students):
    result = {}
    
    for s, v in students:
        if s in result:
            value = result[s]
            result[s] = (v + value) / 2
        else:
            result[s] = v
            
    return result
    
#-----------------------------------------------------

def student_summary_2(students):
    all_sccore = {}
    
    for s, v in students:
        if s not in all_sccore:
            all_sccore[s] = []
        all_sccore[s].append(v)
    
    result = {}
    for s, v in all_sccore.items():
        result[s] = sum(v) / len(v)

    return result

students = [
    ("Alice", 80),
    ("Bob", 65),
    ("Alice", 90),
    ("Bob", 75),
    ("John", 50)
]


print(student_summary(students))
print(student_summary_2(students))