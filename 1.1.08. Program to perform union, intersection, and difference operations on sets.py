'''Write a Python program to perform union, intersection and difference operations on Set A and Set B.



Input Format:

Set A: The first input prompts for a space-separated list of integers for Set A.
Set B: The second input prompts for a space-separated list of integers for Set B.


Output Format:

Union: The first line should display the union of both sets.
Intersection: The second line should display the intersection of both sets.
Difference: The third line should display the difference between Set A and Set B.


Note:

Please refer to the visible test cases for better understanding.

Sample Test Cases
Test case 1
Set·A:·0 2 4 6 8	
Set·B:·1 2 3 4 5	
Union:··{0,·1,·2,·3,·4,·5,·6,·8}⏎	
Intersection:··{2,·4}⏎	
Difference:··{0,·8,·6}⏎	
Test case 2
Set·A:·10 11 22 33 44 55	
Set·B:·15 16 17 18 19 14	
Union:··{33,·10,·11,·44,·14,·15,·16,·17,·18,·19,·22,·55}⏎	
Intersection:··set()⏎	
Difference:··{33,·10,·11,·44,·22,·55}⏎'''



a = list(map(int,input("Set A: ").split()))
A = set(a)
b = list(map(int,input("Set B: ").split()))
B = set(b)

# Write your code here to perform different operations
union_set = A | B  # Union
intersection_set = A & B  # Intersection
difference_set = A - B  # Difference (A - B)

# Displaying results
print(f"Union:  {union_set}")
print(f"Intersection:  {intersection_set}")
print(f"Difference:  {difference_set}")
