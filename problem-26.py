def search_countries_by_letter(country_data: dict[str, str], letter: str) -> list[str]:
    result = []
    for country in country_data.values():
        if country.lower().startswith(letter.lower()): # ปรับเป็น lower เพื่อให้ไม่สนใจตัวพิมพ์ใหญ่/เล็ก และใช้ startswith ว่า True หรือ False
            result.append(country)
    return result
        
print(search_countries_by_letter({"+1": "United States", "+44": "United Kingdom", "+91": "India", "+81": "Japan", "+49": "Germany", "+86": "China"}, "u"))

#--------------------------------

def search_countries_by_letter_2(country_data: dict[str, str], letter: str) -> list[str]:
    result = []
    for country in country_data.values():
        if letter.lower() in country.lower():
            result.append(country)
    return result

print(search_countries_by_letter_2({"+1": "United States", "+44": "United Kingdom", "+91": "India", "+81": "Japan", "+49": "Germany", "+86": "China"}, "u"))