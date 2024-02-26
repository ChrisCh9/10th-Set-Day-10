#Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space). 

fname = input("Enter your first name: ")

fname_length = len(fname)

print("Your first name's length is: ",fname_length)

surname = input("Enter your surname: ")

surname_length = len(surname)

print("Your surname's length is: ",surname_length)

full_name = fname + " " + surname

print("Your full name is: ",full_name)

full_name_length = len(full_name)

print("Your full name's length is: ",full_name_length)