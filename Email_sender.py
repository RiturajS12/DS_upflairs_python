class Email:
    def __init__(self):
        self.users = {"admin@gmail.com": "12345", "Rituraj@gmail.com": "kyundu17"}
        self.mails = {"Rituraj@gmail.com": ["""Subject: regarding Cats\n\nMessage: Cats are cute!!!So please don't u dare to hurt them they are just the creature of god itself. Cats are goddddddddd!!!Cats are enchanting creatures, embodying a perfect blend of elegance and playfulness; their gentle purrs are like a symphony of comfort, and their curious eyes reflect a universe of wonder and affection. They transform ordinary moments into magical memories with their graceful antics and affectionate nudges, reminding us that the purest love often comes wrapped in soft fur and delicate whiskers.!!\n\nFrom: admin@gmail.com\n"""]}

    def login(self, username):
        while True:
            print("1 for composing mail, 2 for checking mail, 3 for logging out")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.compose_mail(username)
            elif choice == '2':
                self.check_mail(username)
            elif choice == '3':
                print("You have logged out.")
                break
            else:
                print("Invalid choice. Please try again.")

    def compose_mail(self, username):
        print("                             ")
        print(f"            From: {username}")
        print("                             ")
        rec_email = input("Enter receiver's email address: ")
        print("                             ")
        print(f"            From: {username}")
        print(f"            To: {rec_email}")
        print("                             ")
        sub = input("Enter subject: ")
        print("                             ")
        print(f"            From: {username}")
        print(f"            To: {rec_email}")
        print(f"            Subject: {sub}")
        print("                             ")
        msg = input("Enter message: ")
        full_msg = f"Subject: {sub}\nMessage: {msg}\nFrom: {username}"
        print("                             ")
        print(f"            From: {username}")
        print(f"            To: {rec_email}")
        print(f"            Subject: {sub}")
        print(f"            Message: {msg}")
        print("                             ")

        if rec_email in self.mails:
            self.mails[rec_email].append(full_msg)
        else:
            self.mails[rec_email] = [full_msg]

        print("Mail sent!")

    def check_mail(self, username):
        if username in self.mails:
            print(f"                    Mails for {username}:")
            for msg in self.mails[username]:
                print(msg)
        else:
            print("No mails found.")

    def main(self):
        while True:
            print("----Enter---- 1 for login, 2 for signup and 3 for exit:")
            option = input()

            if option == '1':
                username = input("Enter Username: ")
                password = input("Enter Password: ")

                if username in self.users and self.users[username] == password:
                    print("Login Successful")
                    self.login(username)
                else:
                    print("Username or password is incorrect")
            elif option == '2':
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                if username in self.users:
                    print("Username already exists")
                else:
                    self.users[username] = password
                    print("Signup Successful")
                    self.login(username)
            elif option == '3':
                print("Thank you for using our service")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    obj = Email()
    obj.main()
