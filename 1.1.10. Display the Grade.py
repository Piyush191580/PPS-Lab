'''Write a Python program to calculate the average marks for 5 subjects. The program should prompt the user to input the marks for each subject. After receiving the input, it should compute the average marks and then determine the corresponding grade based on the following grading system:



A: 90 - 100
B: 80 - 89
C: 70 - 79
D: 60 - 69
F: Below 60


The program should display the average marks up to 2 decimal places and the assigned grade.


Sample Test Cases
Test case 1
subject·1:·67.8	
subject·2:·89.7	
subject·3:·90.5	
subject·4:·90.0	
subject·5:·98.0	
Average·Marks:·87.20⏎	
Grade:·B⏎	
Test case 2
subject·1:·89.50	
subject·2:·91.50	
subject·3:·92.0	
subject·4:·97.45	
subject·5:·89.7	
Average·Marks:·92.03⏎	
Grade:·A⏎'''


sub1 = float(input("subject 1: "))
sub2 = float(input("subject 2: "))
sub3 = float(input("subject 3: "))
sub4 = float(input("subject 4: "))
sub5 = float(input("subject 5: "))
average = (sub1+sub2+sub3+sub4+sub5)/5
print(f"Average Marks: {average:.2f}")
if(average>=90):
	print("Grade: A")
elif(average>=80 and average<=89):
	print("Grade: B")
elif(average>=70 and average<=79):
	print("Grade: C")
elif(average>=60 and average<=69):
	print("Grade: D")
else:
	print("Grade: F")
