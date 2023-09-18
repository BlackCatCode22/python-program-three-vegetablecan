'''
Written by Donald Cao
Date 09/12/2023
Python Program Three: List and Dictionary
CIT 95
'''
#Creating a menu for selecting options on a contact management system.

contact = [] # An emptied list that will hold a dictionary of contact information. It's global scope, thus it saves dictionary record for future use. If in local scope, no save would be possible.

def add_contact():
        '''
        The add_contact enables user to insert record of contact of that individual's first name, phone numbers, and email address. Considering to use for loop to enable contacts to be inserted into list. 
        Currently, if there's an input error like less than 10 digits phone numbers or a number inserted in the name's value, a dictionary save will be kept rather than canceled. Possible future approach will be to conditioned this within an if/else statement to determine if that dictionary gets saved to a list or not.

        '''
        name = input('Enter the contact\'s name: ')
        phone = input("Enter the 10 digits phone number without parenthesis and no dash: ")
        email = input("Enter the email address: ")
        contact_catalog = {"Name": name,"Phone_Number": phone,"Email":email}
        
        #Using the copy method enables dictionary to be added to list. By not having a variable assigned to this line, result will show rather than "None".
        contact.append(contact_catalog.copy())
        
        #Stores updated contact.
        return contact
        print("Saved contact.") 

        #Tests if context matches with conditions:
        if name.replace(" ","").strip().isalpha()==True:
                '''Name must be in alphabet and removes white spaces in between and around'''
                pass
        else:
                print("Name isn't alphabetical.")

        if phone.isdigit()==True:
                '''Phone numbers must contains numerical digits'''
                pass
        else:
                print("Phone number must contains numerical digits only.")

        if len(phone[:10])==len(phone)==10:
                '''Phone numbers must contains 10 digits'''
                pass
        else:
                print("Phone number must be 10 digit only.")

        if ("@" and (".com" or ".gov" or ".edu" or ".net") in email) == True:
                '''Email must contains @ symbol and .com from contacts'''
                pass
        else:
                print("Invalid email was entered.")

def view_contact():
        '''
        The view_contact enables user to look at contact's name list only. 
        Used for-loop to cancel list type and draw only dictionary. Then set the count of dictionary to draw count of indexes. This resulted in calling each dictionary with their respective index number and finally with specifying the key leads to drawing the Name from the contact. 
        If I had more time, I would add more feature to this, like numbering the contact names.
        '''
        for contacts_name in range(len(contact)):                
                print('Name:',contact[contacts_name]["Name"])

def search_contact():
        '''
        The search_contact enables user to look at that individual's contact information once search is successful.
        A prompt will pop up and asking user to enter contact's name. If name does not exist, the condition will be seen as False and loop back to request for another name. However, should a name matches to the value, it will print a record of that dictionary. 
        There are a few things I would improve on in this function:
                1. Program further to show a cleaner output than a dictionary should a name matches a record. An idea to make a nested for-loop with contact.items() would be needed and tested.
                2. After running a couple of tests, I had hit a trap and could not get out from: This program doesn't call dictionary away from list but instead call it individually. Thus, contact check does not give True Positive. It loops for a finite about depending on the list of contact and goes in order. If the user doesn't input the first contact name, then its immediately goes to False. Like if I had a contact name Tom and searched Tom who is not the first contact of the contact list. Despite being present on the list, my program will give a false-negative result. This section will need to be observed more. So for now, it can only check in order of names ridgidly.
        '''
        for i in range(len(contact)):
                name=input("Enter a name or \'q\' to return to main menu: ")
                if (name in contact[i].values()) == True:
                        print('\nContact Found!\nContact: ',contact[i])
                else:
                        print("\nNo Record Found.")

def print_contact():
        '''
        This function enables user to print a text file of a list of contact. Data type for this statement must be in string and can not be written from a dictionary type. 
        For future work, will try to explore method of cleaning this list of contacts. Issue found is that if going down the Main Menu's option list, will only print list of contacts that had been searched. Will look into this in the future.
        '''
        for i in range(len(contact)):
                with open("contact.txt", "w") as f:
                        f.write(str(contact[0:i]))
                        print("Text file of your contacts has been printed")

#Enable while loop to return back to menu page once an option's task has been completed.
on = True
while on:
        '''
        From having ON being True, a loop can be executed. Only when user enters 'q' will it become False and the program will close.
        '''
        print("""
Welcome to your Contact Management System. Below you have options you can select.\n
\t1. Add New Contact
\t2. View Contact List
\t3. Search for a Contact Information
\t4. Print Contact List (Please create a list first before choosing this option.)
        """)
        option = input("Enter a number corresponding with the task or cancel program with \"q\": ")
        #User will have to select a number to call a function inorder for a task to begin or close loop. An error handling was added on the else.
        if  option == "1":
                (add_contact())
        elif option == "2":
                (view_contact())
        elif option == "3":
                (search_contact())
        #File handling feature was added.
        elif option == "4":
                (print_contact())
        elif option == "q":
                print("\nThank you for using Contact Management System. See you later.")
                on=False
        else:
                print("\nNo valid option was entered.")
