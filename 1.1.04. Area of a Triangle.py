'''Write a Python program to print the area of a triangle.



Sample Input & Output:

Base: 10

Height: 15

Area: 75



Note: Round off the result to two decimal places


Sample Test Cases
Test case 1
Base:·10	
Height:·15	
Area:·75.00⏎	
Test case 2
Base:·30.5	
Height:·19.95	
Area:·304.24⏎'''


Base = float(input("Base: "))
Height =float(input("Height: "))

area = 0.5*Base*Height

print(f"Area: {area:.2f}")
