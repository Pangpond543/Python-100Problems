def check_prime(n: int):
    num = []
    for i in range(1, n + 1):
        if n % i == 0:
            num.append(i)
    if len(num) == 2:
        return "is prime"
    else:
        return "is not prime"

print(check_prime(51))