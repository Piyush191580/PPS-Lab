'''Write a Python program that prompts the user to input a date (year, month, and day) and checks if it is a valid date. If the entered date is valid, the program should increment the date by one day and display the incremented date. The program should take into account leap years when determining the number of days in February.


Sample Test Cases
Test case 1
year:·2024	
month:·12	
day:·7	
valid⏎	
incremented·date:·2024-12-08⏎	
Test case 2
year:·2023	
month:·13	
day:·30	
invalid⏎	
Test case 3
year:·2021	
month:·2	
day:·29	
invalid⏎'''

from datetime import date, timedelta
def is_valid_date(year,month,day):
	try:
		valid_date=date(year,month,day)
		return True
	except ValueError:
		return False
def increment_date(year,month,day):
	given_date = date(year,month,day)
	next_day=given_date+timedelta(days=1)
	return next_day
try:
	year=int(input("year: "))
	month=int(input("month: "))
	day=int(input("day: "))

	if is_valid_date(year,month,day):
		print("valid")
		next_date=increment_date(year,month,day)
		print(f"incremented date: {next_date}")
	else:
		print("invalid")

except ValueError:
	print("Invalid input!Please enter valid integers for year,month,and day.")
