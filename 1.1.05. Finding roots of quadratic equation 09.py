'''Write a Python program to find the roots of a quadratic equation by taking the coefficients from the user.



Note: Refer to the displayed test cases for input and output format.


Sample Test Cases
Test case 1
a:·3	
b:·33	
c:·0	
The·roots·are:·0.00·and·-11.00⏎	
Test case 2
a:·3	
b:·0	
c:·1	
The·roots·are:·-0.00+0.58j·and·-0.00-0.58j⏎	
Test case 3
a:·1	
b:·2	
c:·1	
The·root·is:·-1.00⏎'''

import cmath
a= float(input("a: "))
b= float(input("b: "))
c= float(input("c: "))
discriminant=b**2-4*a*c
if discriminant >0:
	root1=(-b+cmath.sqrt(discriminant))/(2*a)
	root2=(-b-cmath.sqrt(discriminant))/(2*a)
	print(f"The roots are: {root1.real:.2f} and {root2.real:.2f}")
elif discriminant == 0:
	root=-b/(2*a)
	print(f"The root is: {root:.2f}")
else:
	root1=(-b+cmath.sqrt(discriminant))/(2*a)
	root2=(-b-cmath.sqrt(discriminant))/(2*a)
	real_part1=f"{root1.real:.2f}"
	imag_part1=f"{root1.imag:.2f}"
	real_part2=f"{root2.real:.2f}"
	imag_part2=f"{root2.imag:.2f}"

	if float(real_part1)==0.0:
		real_part1="-0.00"

	print(f"The roots are: {real_part1}+{imag_part1}j and {real_part2}{imag_part2}j")
