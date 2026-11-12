def is_year_leap(year):
    if year % 4 == 0:
        return True
    return False


check_year = int(input("Введите год: "))
result = is_year_leap(check_year)

print(f"год {check_year}: {result}")
