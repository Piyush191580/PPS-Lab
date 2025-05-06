'''Write a program to count the number of vowels using sets in a given string.



Input Format:

The program should prompt the user to enter the string.


Output Format:

The program should print the count of vowels present in the string.

Sample Test Cases
Test case 1
Hello World	
3⏎	
Test case 2
Rhythm	
0⏎	
Test case 3
CodeTantra	
4⏎	


'''


def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
	for char in str:
	    if char in vowel:
	        count += 1
	print(count)
str = input()
vowel_count(str)
