firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
username = firstname + " " + lastname
email = firstname.lower() + "." + lastname.lower() + "@gmail.com"
print("Your full name is: " + username)
print("Your email is: " + email)