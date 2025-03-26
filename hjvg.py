def is_leap_year(year):
    # A year is a leap year if it is divisible by 4
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def days_in_year(year):
    # A year has 366 days if it's a leap year, else it has 365 days
    if is_leap_year(year):
        return 366
    return 365


def days_since_birthday(birthday):
    # Splitting the birthday into day, month, and year
    day, month, year = map(int, birthday.split("-"))

    # Get the current year
    current_year = 2025  # The current year is 2025

    # Starting by calculating the total days from the full years between birth and current year
    total_days = 0
    for year in range(year + 1, current_year):  # We start at year + 1 and end at current_year - 1
        total_days += days_in_year(year)

    return total_days


# Example of my birthday:
birthday = "26-07-2005"
result = days_since_birthday(birthday)
print(result)  # It will print the number of days passed, excluding the birth year and the current year, which is 6940
