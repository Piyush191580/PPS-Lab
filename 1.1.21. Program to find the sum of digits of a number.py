'''Write a program to print the sum of digits of a number.

For example: If the number is 1234, then the sum of digits, 1 + 2 + 3 + 4 = 10 should be printed.

Sample Input and Output:
num: 454545
sum: 27

Sample Test Cases
Test case 1
num:·101	
sum:·2⏎	
Test case 2
num:·454545	
sum:·27⏎	
Test case 3
num:·363	
sum:·12'''


num = int(input("num: "))

sum = 0

while num > 0:
    sum += num % 10
    num //= 10
print("sum:", sum)
