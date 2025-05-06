'''Write a Python program to print the following pattern.

Sample Input and Output:
Enter a number : 6
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

Sample Test Cases
Test case 1
Enter·a·number·:·5	
*·*·*·*·*·⏎	
*·*·*·*·⏎	
*·*·*·⏎	
*·*·⏎	
*·⏎	
Test case 2
Enter·a·number·:·6	
*·*·*·*·*·*·⏎	
*·*·*·*·*·⏎	
*·*·*·*·⏎	
*·*·*·⏎	
*·*·⏎	
*·⏎	
Test case 3
Enter·a·number·:·3	
*·*·*·⏎	
*·*·⏎	
*·⏎'''


n = int(input("Enter a number : "))

for i in range(n, 0, -1):
    print("* " * i)

