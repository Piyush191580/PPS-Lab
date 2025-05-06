'''Write a Python program that prints prime numbers less than n which represents the upper limit.


Sample Test Cases
Test case 1
Enter·upper·limit:·20	
2⏎	
3⏎	
5⏎	
7⏎	
11⏎	
13⏎	
17⏎	
19⏎	
Test case 2
Enter·upper·limit:·36	
2⏎	
3⏎	
5⏎	
7⏎	
11⏎	
13⏎	
17⏎	
19⏎	
23⏎	
29⏎	
31⏎	
'''

n = int(input("Enter upper limit: "))
for num in range(1, n + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
