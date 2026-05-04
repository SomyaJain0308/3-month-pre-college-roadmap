"""
The Password Manager project is a program designed to help users organize and store their account names and 
passwords in a local text file.
Key features and functionality include:

* Storage: It saves account names alongside their corresponding passwords.
* Mode selection: The user can interact with the program to either view existing saved credentials or add new ones .
* Encryption: To avoid storing sensitive data in plain text, the project uses the Fernet module from the cryptography library to 
encrypt and decrypt the password.
* File Handling: It utilizes Python's file operations—specifically 'append' (a) mode for adding new entries and 'read' (r) mode 
for viewing them—ensuring data is persistent between program runs.
Important Note: As the creator mentions, this project is intended as a fun learning exercise and is not a secure way to store 
real-world sensitive passwords now tell me if i should do the project now or later?
"""
print("------------------------------------------------------------------------------------------------------------------")
while True:
    try:
        ask=input("Do you want to view the existing passwords or save a new one? ").strip().lower()
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    if ask=="save":
        break
    elif ask=="view":
        break
    else:
        print("Type 'Save' or 'View' Retard!")
        continue



if ask=="save":
    ask_username=input("Username: ").strip()
    ask_password=input("Password: ").strip()
    print("------------------------------------------------------------------------------------------------------------------")
    with open("passwords.txt", "a") as f:
        f.write("\n"+ "Username: " + ask_username + "\n" + "Password: " + ask_password + "\n" + "\n" + "-------------------------------" + "\n")
elif ask=="view":
    print("------------------------------------------------------------------------------------------------------------------")
    with open("passwords.txt", "r") as f:
        for line in f:
            print(line.strip())

