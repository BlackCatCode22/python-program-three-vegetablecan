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
4. Quit Program

Each of the option, except Quiting the program, are written in function. The menu is written in a while loop. This loop uses the boolean result to continue or cancel the loop.

Test cases and error handling will be used in all three option. Will also have file input/output in option 3, Search Contact. Currently, have error handling in option 1 when recording contact names, phone numbers, and emails. 

### Concern/Issue
1. Figuring out how to append new record of dictionary into list and verifying if empty list should be diplaced outside of the function for add_contact or remain global?
2. Learning how to call list of dictionary from another function. An example is calling the list of record contact from Add_Contact to View_Contact.