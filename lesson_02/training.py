# 1) Работа со списками
employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]

sec = employee_list[1]
sec_end = employee_list[-2]

print(sec + ", " + sec_end)


# 2) Деление на три
def dev_by_three(x):
    if x % 3 == 0:
        return "Да"
    else:
        return "Нет"


num = int(input("Введите число: "))
result = dev_by_three(num)


print(f"Делится ли на три число {num}? - {result}")


# 3) Округление
from math import ceil


def min_boxes(item):
    return ceil(item / 5)


items = int(input("Введите количество предметов: "))
print(f"Для количества предметов -8 {items}, нужно коробок - {min_boxes(items)}")


# 4) Два делителя
def check_divisibility(n):
    for i in range(1, n + 1):
        if i % 2 == 0 and i % 4 != 0:
            print(f"{i} Делится на 2, но не на 4")
        elif i % 2 == 0 and i % 4 == 0:
            print(f"{i} Делится и на 2, и на 4")
        else:
            print(i)


number = int(input("Введите число: "))
check_divisibility(number)


# 5) Квартал
def quarter_of_year(x):
    if 1 <= x <= 3:
        return "1-й квартал"
    if 4 <= x <= 6:
        return "2-й квартал"
    if 7 <= x <= 9:
        return "3-й квартал"
    if 10 <= x <= 12:
        return "4-й квартал"
    return "Это не номер месяца"


num_month = int(input("Введите номер месяца: "))
print(f"Месяц {num_month} - {quarter_of_year(num_month)}")


# 6) Фильтрация списка
lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

# for i in lst:
#     if i > 15 and i % 3 == 0:
#         print(i)

result = [i for i in lst if i > 15 and i % 3 == 0]  # Генератор списков
print(result)


# 7) Range
list_range = list(range(25, 4, -5))

print(list_range)


# 8) Поменять значения местами
var_1 = 50
var_2 = 5

x = var_1
y = var_2

var_1 = y
var_2 = x

print(f"var_1 = {var_1} \nvar_2 = {var_2}")

print()

# использование множественного присваивания
# Python сначала полностью вычисляет правую часть (создает кортеж),
# и только потом начинает присваивать значения в левую.
# Поэтому старое значение var_1 не затирается до того, как оно попадет в var_2
var_1 = 50
var_2 = 5

var_1, var_2 = var_2, var_1

print(f"var_1 = {var_1} \nvar_2 = {var_2}")
