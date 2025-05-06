'''Write a python program to print factorial of given number.



Note: If user enters a negative number as input prompt the message "Enter a positive number"


Sample Test Cases
Test case 1
Enter·a·number·:·5	
Factorial·of·given·number·is·:·120⏎	
Test case 2
Enter·a·number·:·-20	
Enter·a·positive·number⏎'''


def factorial(n):
	if n == 0:
		return 1
	else:
		fact =1
		for i in range (1,n+1):
			fact *=i
		return fact

num = int (input("Enter a number : "))
if num < 0:
	print("Enter a positive number")
else:
	fact = factorial(num)
	print(f"Factorial of given number is : {fact}")
