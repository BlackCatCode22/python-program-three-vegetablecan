# Python Program 3 - List and Dictionary
## An Approach to Designing a Contact Management System
Written by Donald Cao
Date started on 09/12/2023

### Summary
Designing a Contact Management System by exploring the list and dictionary data structure as well as using flow control and loop control to create the program.

The Contact Management System opens a menu with four options:
1. Add Contact
2. View Contact
3. Search Contact
4. Print txt file of Contacts
5. Quit Program

Each of the option, except Quiting the program and the main menu, are written in function. The menu is written in a while loop. This loop uses the boolean result to continue or cancel the loop. 

In Option 1, Add Contact, user can input new contacts with test cases and error handling by using If/Else method and string methods. Had trouble with understanding with global and local scope when practicing an empty list called contact and trying to have a dictionary data to occupy it. Took a while from reading articles online as I have found that I was close to solving the problem. I didn't have to assign the values of the dictionary to a variable. Just return said contact.append(values). With that settled, its easier to save contacts as a dictionary into a list.

In Option 2, the View Contact gives a list of contact names. I thought it was going to be easy. I would set it to print(contact), but I wanted to see if I can clean it up and only show just the name without the details. The issue I found was the for loop did not give a full list immediately, but draw a name each loop it did until it runs out of name. This created problem for creating a table and indexing it if the list of name were to be larger than three. Eventhough these issues are cosmetic, visual cues to me are important.

In Option 3, the Search Contact is the most elusive among the program I tried to get correct. Basically, if the user input the name, full name with correct capitalization, it will pull a full contact detail about that individual. However that was not the case. I carried the for-loop procedure from Option 2 and it resulted in search following the order of the index. For exam, if John Smith was the first on the Contact List and the user were inputting that name, the program will return True and pull that contact detail. But if the user inputted other than John Smith and that input does exist somewhere else on that list, then the program will draw a false-negative. Besides that, will have to look into another approach in the near future. Also will include string method incase user decides to use lower case only or uppercase only.

In Option 4, the file handling does work. It uses a for statement to print a contact list into a txt file, but only after finishing Option 1 for a full list. Apparently, when testing the program by going down the option list, once option 3 was concluded and then tried to print my list, only a few names were saved. And those names was tested in the search contact in Orders. 

Overall, I did enjoy this project. It tested my understanding of global and local scope, functions, and data structures. I had to review a lot from string methods and while loops. Looking forward for another project.