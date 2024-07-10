users = {"admin@gmail.com": "12345", "Rituraj@gmail.com": "kyundu17"}
mails = {"Rituraj@gmail.com": ['Subject: regarding Cats\nMessage: Cats are cute!!!\nFrom: admin@gmail.com']}

def login(username):
    while True:
        print("1 for composing mail, 2 for checking mail, 3 for logging out")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            compose_mail(username)
        elif choice == 2:
            check_mail(username)
        elif choice == 3:
            print("You have logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def compose_mail(username):
    print("                             ")
    print(f"            From: {username}")
    print("                             ")
    print("Enter receiver's email address:")
    rec_email = input()
    print("                             ")
    print(f"            From: {username}")
    print(f"            To: {rec_email}")
    print("                             ")
    print("Enter subject:")
    sub = input()
    print("                             ")
    print(f"            From: {username}")
    print(f"            To: {rec_email}")
    print(f"            Subject: {sub}")
    print("                             ")
    print("Enter message:")
    msg = input()
    full_msg = f"Subject: {sub}\nMessage: {msg}\nFrom: {username}"
    print("                             ")
    print(f"            From: {username}")
    print(f"            To: {rec_email}")
    print(f"            Subject: {sub}")
    print(f"            Message: {msg}")
    print("                             ")

    if rec_email in mails:
        mails[rec_email].append(full_msg)
    else:
        mails[rec_email] = [full_msg]

    print("Mail sent!")

def check_mail(username):
    if username in mails:
        print(f"                    Mails for {username}:")
        for msg in mails[username]:
            print(msg)
    else:
        print("No mails found.")

while True:
    print("----Enter---- 1 for login, 2 for signup and 3 for exit:")
    option = int(input())

    if(option == 1):
        print("Enter Username:")
        username = input()
        print("Enter Password:")
        password = input()

        if username in users and users[username] == password:
            print("Login Successful")
            login(username)
        else:
            print("Username or password is incorrect")
    elif(option == 2):
        print("Enter Username:")
        username = input()
        print("Enter Password:")
        password = input()
        if username in users and users[username]==password:
            print("Username already exists")
            login(username)
        else:
            users[username] = password
            print("Signup Successful")
            login(username)
    elif(option == 3):
        print("Thank you for using our service")
        break
    else:
        print("Invalid option. Please try again.")
