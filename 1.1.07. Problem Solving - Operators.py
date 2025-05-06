'''Write a program to read temperature in Celsius and print the temperature in fahrenheit.



Input Format:

The user is prompted to enter a temperature (float) in Celsius.


Output Format:

The program outputs the equivalent temperature in Fahrenheit.


Hint: The formula for conversion is F = 1.8 * Temperature_in_Celsius + 32.0.


Sample Test Cases
Test case 1
celsius:·23.30	
fahrenheit:·73.94⏎	
Test case 2
celsius:·45.3	
fahrenheit:·113.53999999999999⏎'''

celsius= float(input("celsius: "))
fah = 1.8*celsius+32.0
print(f"fahrenheit: {fah}")
