
def is_leap(year): 
    """Determine if a year is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False
        else:
            return True 
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


def month_name(month):
    """Convert numeric month value to word"""
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] 
    return month_name[month -1]
    
#inputs from user
year = int(input("Enter a year: "))
month = int(input("Enter a numeric month: "))
days = days_in_month(year, month)
month_word = month_name(month)
print(f"There are {days} days in the month of {month_word} in the year {year}.")












