#Creating a menu for selecting options on a contact management system.

def add_contact():
	'''
	The add_contact enables user to insert record of contact of that individual's first name, phone numbers, and email address.

	'''
	contact = [] # An emptied list that will hold a dictionary of contact information.
	fname = input('Enter the contact\'s first name: ')
	phone = input("Enter the phone number without parenthesis and no dash: ")
	email = input("Enter the email address: ")
	contact_catalog = {"Name": fname,"Phone_Number": phone,"Email":email}
	contact=contact.append(contact_catalog)
	return contact

	#Tests if context matches with conditions:
	if fname.isalpha()==True:
		'''Name must be in alphabet'''
		pass
	else:
		print("Name isn't in alphabet.")

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

	if ("@" and ".com" in email) == True:
		'''Email must contains @ symbol and .com from contacts'''
		pass
	else:
		print("Invalid email was entered.")

	print(add_contact(contact))

def view_contact():
	'''
	The view_contact enables user to look at contact's name list only.
	'''
	pass

def search_contact():
	'''
	The search_contact enables user to look at that individual's contact information once search is successful.
	'''
	pass

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
	""")
	option = input("Enter a number corresponding with the task or cancel program with \"q\": ")
	#User will have to select a number to call a function inorder for a task to begin or close loop. An error handling was added on the else.
	if  option == "1":
		(add_contact())
	elif option == "2":
		(view_contact())
	elif option == "3":
		(search_contact())
	elif option == "q":
		print("Thank you for using Contact Management System. See you later.")
		on=False
	else:
		print("No valid option was entered.")
