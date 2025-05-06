'''Write a Python program that takes a sentence as input, removes punctuations from the sentence, and displays the modified sentence.


Sample Test Cases
Test case 1
I love Coding!!	
I·love·Coding⏎	
Test case 2
I have 3 chocolates.	
I·have·3·chocolates⏎'''


sentence = input()

punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

clean = ""
for char in sentence:
    if char not in punctuations:
        clean += char

print(clean)

