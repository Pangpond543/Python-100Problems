def find_dupicate_chars_count(s: str) -> dict:
    result = {}
    dupicate = {}
    for ch in s:
        #print(ch)
        if ch.islower():    #เช็กว่าตัวเล็กมั้ย
            if ch in result:    #เช็กว่าเจอตัวซํ้ามั้ย
                result[ch] += 1
            else:
                result[ch] = 1
            
    for key, value in result.items():   #ลูปหาตัวที่ซํ้า ไม่เอาตัวที่ไม่ซํ้า เช่น 'e': 1
        if value > 1:
            dupicate[key] = value
    #print(result)
    return dupicate
        
print(find_dupicate_chars_count("Hello Hi Pond!"))



def find_pair_with_product(nums: list, target: int) -> list:
    number = []
    for num1 in range(len(nums)):
        for num2 in range(num1, len(nums)):
            if nums[num1] * nums[num2] == target:
                number.append([nums[num1], nums[num2]])
                
    return number

#print(find_pair_with_product([-1,-2, 2], 4))