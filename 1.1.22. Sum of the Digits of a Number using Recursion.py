'''Take an integer n from the user. Your task is to Write a program to find out the sum of the digits of the given number using the process of recursion. Print the result as shown in the Test cases. 

The program defines the Sumof() function.
In the main program it takes the input n and sends it to the Sumof() function.
The Sumof() function contains base and recursive criterion.


Constraints:

1 <= integer <= 106



Sample Test Case:

4532 ----> Input integer

14 ----> Sum of the digits of the given number (4+5+3+2 = 14)


Sample Test Cases
Test case 1
4532	
14⏎	
Test case 2
109	
10⏎	
Test case 3
56	
11⏎'''



'''
Complete the given function using recursive approach,
and also write the driver code test the functionality,
and pass all the visible and hidden test cases.

'''
def Sumof(n):
	if n == 0:
		return 0
	else:
		return (n%10)+Sumof(n//10)

		
n = int(input())
print(Sumof(n))

# take user input and add the function call

