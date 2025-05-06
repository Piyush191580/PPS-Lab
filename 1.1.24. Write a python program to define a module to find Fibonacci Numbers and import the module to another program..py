'''Write a python program to define a module to find Fibonacci Numbers and import the module to another program.



Aim:

To create a Python program that generates a Fibonacci sequence up to a given maximum value.


Algorithm:

Step 1: Import the fibonacci_module.

Step 2: Accept an integer input from the user as the maximum value (n).

Step 3: If n is greater than 0:

Generate the Fibonacci sequence up to n using the generate_fibonacci_sequence() function from the fibonacci_module.
Print the generated Fibonacci series.
Step 4: If n is not greater than 0, print "Please enter a positive integer".

Step 5: End the program.



Note: The fibonacci_module contains the generate_fibonacci_sequence() function to generate the Fibonacci sequence up to a specified maximum value.












Sample Test Cases
Test case 1
Enter·the·max·value:·10	
Fibonacci·series·upto·10·:⏎	
0·1·1·2·3·5·8·13·21·34·	
Test case 2
Enter·the·max·value:·-9	
Please·enter·a·positive·integer⏎'''











#fibonacci_program.py
import fibonacci_module

def main():
    try:
        n = int(input("Enter the max value: "))

        if n > 0:
            fibonacci_series = fibonacci_module.generate_fibonacci_sequence(n)
            print(f"Fibonacci series upto {n} :")
            print(*fibonacci_series,end=(" "))
        else:
            print("Please enter a positive integer")

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

# fibonacci_module.py

def generate_fibonacci_sequence(num_terms):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(num_terms):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

