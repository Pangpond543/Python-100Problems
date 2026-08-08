def str_int_float():
    name = str(input("ชื่อ: "))
    age = int(input("อายุ: "))
    weight = float(input("นํ้าหนัก: "))
    height = float(input("ส่วนสูง: "))

    print(f'Name: {name} \nAge: {age} \nWeight: {weight} \nHight: {height}')
#str_int_float()

#----------------------------------------------------------------------------------

def function_2():
    score = []
    pas = []
    for i in range(1, 6):
        score.append(int(input(f'Enter score{i}: ')))
    len_ = len(score)
    hig_scr = max(score)
    low_scr = min(score)
    average = sum(score) / len_
    sorted_ = sorted(score)
    for i in score:
        if i >= 50:
            pas.append(True)
        else:
            pas.append(False)
    all_pas = all(pas)
    fail = any(pas)
    print(f'---------------------------------- \nNumber of students: {len_} \nHighest score: {hig_scr} \nLowest score: {low_scr} \nAverage score: {average} \nSorted scores: {sorted_} \nPassed all: {all_pas} \nHas failed: {fail}')
function_2()
        