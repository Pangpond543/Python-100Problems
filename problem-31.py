def highest_sales_country(sales: dict[str, int]) -> tuple[str, int]:
    high_country = ""
    high_sales = 0
    
    for c, s in sales.items():
        if s > high_sales:
            high_sales = s
            high_country = c
            
    return (high_country, high_sales)

print(highest_sales_country({
"Thailand": 1500,
 "Laos": 1200,
 "Vietnam": 1800,
 "Japan": 1700,
 "China": 2000
}))

#------------------------------------------------------------------
def highest_sales_country_2(sales: dict[str, int]) -> tuple[str, int]:
    return max(sales.items, key=lambda item: item[1])   #lamda คือการสร้างฟังก์ชั่นสั้นๆ คล้ายกับ def - [1]การเอาตัวที่2มาวัด maximum

print(highest_sales_country({
"Thailand": 1500,
 "Laos": 1200,
 "Vietnam": 1800,
 "Japan": 1700,
 "China": 2000
}))

#------------------------------------------------------------
def highest_sales_country_3(sales: dict[str, int]) -> tuple[str, int]:
    highest = None

    for item in sales.items():
        #print(item)    #เช็กว่า .items ส่งมาแบบไหน
        if highest is None or item[1] > highest[1]: #เช็กว่า ค่าที่2ของitem มากกว่า ค่าที่เคยได้ตั้งไว้รึป่าว
            highest = item

    return highest

print(highest_sales_country_3({
"Thailand": 1500,
 "Laos": 1200,
 "Vietnam": 1800,
 "Japan": 1700,
 "China": 2000
}))

