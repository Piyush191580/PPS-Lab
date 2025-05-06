'''Write a Python program to find the largest of three numbers.



Note: Follow the input and output layout mentioned in the visible test cases.


Sample Test Cases
Test case 1
Enter·the·first·number:·5	
Enter·the·second·number:·12	
Enter·the·third·number:·8	
Largest·number:·12.0⏎	
Test case 2
Enter·the·first·number:·-3	
Enter·the·second·number:·-8	
Enter·the·third·number:·-1	
Largest·number:·-1.0⏎	
Test case 3
Enter·the·first·number:·6	
Enter·the·second·number:·6	
Enter·the·third·number:·6	
Largest·number:·6.0⏎'''



num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max(num1,num2,num3)
print(f"Largest number: {largest:.1f}")
