'''Implement a Python program using a class named Complex to perform operations on complex numbers. The class has the following methods:



initComplex(): A method that takes user input for the real and imaginary parts to initialize a complex number.
display(): A method that displays the complex number in the form "a + bi".
sum(): A method that computes the sum of two complex numbers and stores the result in the current instance.


The program creates three instances of the Complex class, initializes two complex numbers, displays them, computes their sum, and displays the result.


Sample Test Cases
Test case 1
complex·number·1⏎	
Real·Part:·3	
Imaginary·Part:·4	
3+4i⏎	
complex·number·2⏎	
Real·Part:·-9	
Imaginary·Part:·5	
-9+5i⏎	
Sum:·-6+9i⏎	
Test case 2
complex·number·1⏎	
Real·Part:·-5	
Imaginary·Part:·0	
-5+0i⏎	
complex·number·2⏎	
Real·Part:·-8	
Imaginary·Part:·0	
-8+0i⏎	
Sum:·-13+0i⏎'''



class Complex ():
	def __init__(self):
		self.real=0
		self.imaginary=0

	def initComplex(self):
		self.real=int(input("Real Part: "))
		self.imaginary=int(input("Imaginary Part: "))

	def display(self):
		if self.imaginary>=0:
			print(f"{self.real}+{self.imaginary}i")
		else:
			print(f"{self.real}{self.imaginary}i")

	def sum(self,c1,c2):
		self.real = c1.real+c2.real
		self.imaginary = c1.imaginary+c2.imaginary

c1 = Complex()
c2 = Complex()
c3 = Complex()
print("complex number 1")
c1.initComplex()
c1.display()
print("complex number 2")
c2.initComplex()
c2.display()
print("Sum:",end=" ")
c3.sum(c1,c2)
c3.display()
