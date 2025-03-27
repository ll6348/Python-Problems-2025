def leap_year(year):
    '''
    This function takes the year as an argument.
    Checks it and returns if the year is a leap year or not.
    '''
    if year % 4 == 0 and year % 100 != 0:
        print(f"{year} is a leap year")
    elif year % 100 == 0 and year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year = int(input("Enter a year:"))
leap_year(year)
