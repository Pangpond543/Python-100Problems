def store_student_info(student_data: list[tuple[str, str]]) -> dict[str, str]:
    dict = {}
    for id, name in student_data:   # unpack ออกมาเป็น id กับ name จาก tuple ของ student_data
        dict[id] = name
    return dict

print(store_student_info([("123456", "Alice"), ("654321", "Bob"), ("112233", "Charlie")]))