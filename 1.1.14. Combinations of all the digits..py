'''Write a Python program that prompts the user to input three digits (0-9) and checks if the entered digits are valid. If the digits are valid, the program generates all possible combinations of these three digits and prints them. Each combination is formed by arranging the digits in different orders. If the input is not valid (digits are not between 0 and 9), the program should display as "Invalid".


Sample Test Cases
Test case 1
digit1·(0-9):·1	
digit2·(0-9):·2	
digit3·(0-9):·3	
123⏎	
132⏎	
213⏎	
231⏎	
312⏎	
321⏎	
Test case 2
digit1·(0-9):·3	
digit2·(0-9):·2	
digit3·(0-9):·10	
Invalid⏎'''

d1 = int(input("digit1 (0-9): "))
d2 = int(input("digit2 (0-9): "))
d3 = int(input("digit3 (0-9): "))

if 0 <= d1 <= 9 and 0 <= d2 <= 9 and 0 <= d3 <= 9:
    digits = [d1, d2, d3]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and j != k and i != k:
                    print(digits[i], digits[j], digits[k], sep="")

else:
    print("Invalid")

