def month_to_season(month_num):
    if not (1 <= month_num <= 12):
        print("Неверный номер месяца.")
        return "Не определено"
    if 1 <= month_num <= 2 or month_num == 12:
        return "Зима"
    if 3 <= month_num <= 5:
        return "Весна"
    if 6 <= month_num <= 8:
        return "Лето"
    if 9 <= month_num <= 11:
        return "Осень"


month = int(input("Введите номер месяца: "))
result = month_to_season(month)

print(result)
