def toggle_case(s: str) -> str:
    sss = ""
    for st in s:
        if st == st.upper():  # หรือใช้ st.isupper เป็น method ที่เช็กได้อยู่แล้ว
            sss += st.lower()
        elif st == st.lower():
            sss += st.upper()
        else:
            sss += st
    return sss
print(toggle_case("Hello World!"))