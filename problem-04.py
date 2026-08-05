def calculate_sum_and_average() -> None:
    num = []
    for i in range(5):
        number = float(input("Please enter your number: "))
        num.append(number)

    numbers = sum(num)
    average = numbers / len(num)

    print(f'sum: {numbers}')
    print(f'average: {average}')

print(calculate_sum_and_average())