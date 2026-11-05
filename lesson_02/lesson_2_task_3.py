from math import ceil


def square(side):
    round_up = ceil(side)
    return round_up * round_up


calc_area = float(input("Введите длину стороны квадрата: "))
result = square(calc_area)

print(f"Площадь квадрата = {result}.")
