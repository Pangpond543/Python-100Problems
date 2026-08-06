def character_frequency(*args: str):
    pass

A = "Hello World! pond"

print(A.split())

#print(list(A)) แยกทีละตัวอักษร
#print(A.split()) แยกทีละคำ
#print(A.lower())
#print(A.upper())
#print(A.replace("Hello", "Hi")) แทนที่คำ
print("".join(list(A))) #join รวม str ใน list