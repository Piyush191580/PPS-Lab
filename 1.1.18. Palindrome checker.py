'''Write a Python program to find whether a given string is a palindrome or not.



Note: A palindrome is a string that reads the same backwards as forward.

For example, "racecar" is a palindrome because it reads the same in both directions, while "hello" is not.



Input Format:

The input should be a string.


Output Format:

If the given string is a palindrome, print "palindrome".
Otherwise, print "not a palindrome".

Sample Test Cases
Test case 1
mam	
palindrome⏎	
Test case 2
sir	
not·a·palindrome'''



def is_palindrome(text):
  processed_text = ''.join(filter(str.isalnum, text)).lower()
  return processed_text == processed_text[::-1]

input_string = input()
if is_palindrome(input_string):
  print("palindrome")
else:
  print("not a palindrome")
