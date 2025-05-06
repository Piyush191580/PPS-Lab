'''Write a Python program to check if a given year is a leap year or not.



Sample Input and Output -1 :

Enter a year: 2020
2020 is a leap year
Sample Input and Output -2 :

Enter a year: 2006
2006 is not a leap year

Sample Test Cases
Test case 1
Enter·a·year:·1994	
1994·is·not·a·leap·year⏎	
Test case 2
Enter·a·year:·2024	
2024·is·a·leap·year'''

year = int(input("Enter a year: "))
if(year%4==0):
	print(f'{year} is a leap year')
else:
	print(f'{year} is not a leap year')
