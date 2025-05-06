'''Write a program to calculate the area of a circle and print the result as shown in the displayed test cases.



Constraints:

Radius is in between the range 0.0 to 100.0 both are inclusive
Input is in the form of float.
Follow the given instructions and write the code in the space provided.



Note: Take the pi value as 3.14.


Sample Test Cases
Test case 1
Enter·the·radius·:·0	
Area·of·circle·=·0.000000⏎	
Test case 2
Enter·the·radius·:·-100	
Enter·a·positive·value·upto·100⏎'''

#Solution
radius = float(input("Enter the radius : "))

if radius < 0 or radius > 100:
    print("Enter a positive value upto 100")
else:
    pi = 3.14
    area = pi * radius * radius
    print(f"Area of circle = {area:.6f}")

