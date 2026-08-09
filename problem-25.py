def store_student_scores(student_data: list[tuple[str, str, float]]) -> dict[str, dict[str, float]]:
    dict = {}
    for id, name, score in student_data:   # unpack ออกมาเป็น id, name และ score จาก tuple ของ student_data
        dict[id] = {"name": name, "score": score }  # สร้าง dict ของ student_info ที่มี key เป็น "name" และ "score"
    return dict
    
print(store_student_scores([("123456", "Alice", 85.5), ("654321", "Bob", 92.0), ("112233", "Charlie", 78.0)]))