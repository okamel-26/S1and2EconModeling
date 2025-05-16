def is_leap_year(year):
    """
    Determine whether a given year is a leap year.

    A year is a leap year if it is divisible by 4,
    except for years that are divisible by 100 unless they are also divisible by 400.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if it is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def days_in_year(year):
    """
    Return the number of days in a given year.

    Parameters:
        year (int): The year for which to return the number of days.

    Returns:
        int: 366 if the year is a leap year, 365 otherwise.
    """
    if is_leap_year(year):
        return 366
    return 365


def days_since_birthday(birthday):
    """
    Calculate the total number of days that have passed from the year after the given birthday
    up to (but not including) the current year.

    This function ignores partial years (the birth year and the current year are excluded).

    Parameters:
        birthday (str): The birth date in "DD-MM-YYYY" format.

    Returns:
        int: Total number of days passed between the years (excluding birth and current year).
    """
    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split("-"))

    # Define the current year
    current_year = 2025

    # Sum the total days in the full years between birth and current year
    total_days = 0
    for year in range(year + 1, current_year):
        total_days += days_in_year(year)

    return total_days


# Example usage
birthday = "26-07-2005"
result = days_since_birthday(birthday)
print(result)  # Should print 6940, days between 2006 and 2024
