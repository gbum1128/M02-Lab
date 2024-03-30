# Gabriel Bumgardner
# Ivytech Sign UP
# This program asks the for the user's first and last name and then asks for their 
# GPA and decides wether they made it to IvyTech or not

Welcome_Message = "Welcome to Ivytech's Qaulification Program"

Goodbye_Message = "Thank you for using our Qaulification Program"

while True:
    print(Welcome_Message)
    
    last_name = input("Please enter your last name (Type ZZZ to quit): ")
    
    if last_name == 'ZZZ':
        break

    first_name = input("Please enter your first name: ")

    gpa = float(input("Enter your current GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made it on the list.")
    else:
        if gpa >= 3.25:
            print(f"{first_name} {last_name} has made honor roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the list nor the honor roll.")


    print(Goodbye_Message)