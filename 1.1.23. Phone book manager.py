'''1.1.23. Phone book manager
09:36










Sample Test Cases
Test case 1
1.·Add·Contact⏎	
2.·Remove·Contact⏎	
3.·Display⏎	
4.·Quit⏎	
Enter·choice·(1-4):·3	
{}⏎	
1.·Add·Contact⏎	
2.·Remove·Contact⏎	
3.·Display⏎	
4.·Quit⏎	
Enter·choice·(1-4):·1	
Name:·Aman	
Phone·number:·8900004500	
1.·Add·Contact⏎	
2.·Remove·Contact⏎	
3.·Display⏎	
4.·Quit⏎	
Enter·choice·(1-4):·1	
Name:·Arjun	
Phone·number:·966969669	
1.·Add·Contact⏎	
2.·Remove·Contact⏎	
3.·Display⏎	
4.·Quit⏎	
Enter·choice·(1-4):·3	
{'Aman':·'8900004500',·'Arjun':·'966969669'}⏎	
1.·Add·Contact⏎	
2.·Remove·Contact⏎	
3.·Display⏎	
4.·Quit⏎	
Enter·choice·(1-4):·2	
Name:·Aanya	
Not·found⏎	
1.·Add·Contact⏎	
2.·Remove·Contact⏎	
3.·Display⏎	
4.·Quit⏎	
Enter·choice·(1-4):·2	
Name:·Arjun	
1.·Add·Contact⏎	
2.·Remove·Contact⏎	
3.·Display⏎	
4.·Quit⏎	
Enter·choice·(1-4):·3	
{'Aman':·'8900004500'}⏎	
1.·Add·Contact⏎	
2.·Remove·Contact⏎	
3.·Display⏎	
4.·Quit⏎	
Enter·choice·(1-4):·7	
Invalid⏎	
1.·Add·Contact⏎	
2.·Remove·Contact⏎	
3.·Display⏎	
4.·Quit⏎	
Enter·choice·(1-4):·4'''



'''while True:
	print("1. Add Contact")
	print("2. Remove Contact")
	print("3. Display")
	print("4. Quit")
'''
phonebook = {}

while True:
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Display")
    print("4. Quit")

    choice = int(input("Enter choice (1-4): "))

    if choice == 1:
        name = input("Name: ")
        phone_number = input("Phone number: ")
        phonebook[name] = phone_number
        
    elif choice == 2:
        name = input("Name: ")
        if name in phonebook:
            del phonebook[name]
            #(f"Contact '{name}' removed.")
        else:
            print("Not found")
            
    elif choice == 3:
        print(phonebook)
        
    elif choice == 4:
        break
        
    else:
        print("Invalid")
