def calculate_coins(amount: int) -> tuple[int, int, int, int]:
    total = amount
    coin = [0, 0, 0, 0]
    
    while total != 0:
        if 10 <= total:
            total -= 10
            coin[0] += 1
        elif 5 <= total:
            total -= 5
            coin[1] += 1
        elif 2 <= total:
            total -= 2
            coin[2] += 1
        elif 1 <= total:
            total -= 1
            coin[3] += 1
    return tuple(coin)

print(calculate_coins(28))