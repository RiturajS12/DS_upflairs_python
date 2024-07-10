import json
import os

DATA_FILE = 'chat_data.json'
USERS_FILE = 'users_data.json'

def load_data(filename):
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        return []
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def register_user():
    users = load_data(USERS_FILE)
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in users:
        if user['username'] == username:
            print("Username already exists.")
            return None
    user = {"username": username, "pass": password}
    users.append(user)
    save_data(users, USERS_FILE)
    return username

def login_user():
    users = load_data(USERS_FILE)
    uname = input("Please enter your username: ")
    passwd = input("Please enter your password: ")
    for user in users:
        if user['username'] == uname and user['pass'] == passwd:
            print(f"Hey {user['username']}, you are now logged in.")
            return user['username']
    print("Invalid username or password.")
    return None

def send_message(sender, recipient, message):
    messages = load_data(DATA_FILE)
    messages.append({"sender": sender, "recipient": recipient, "message": message})
    save_data(messages, DATA_FILE)
    print("Message sent!")

def view_chat_history(username):
    messages = load_data(DATA_FILE)
    for msg in messages:
        if msg["recipient"] == username or msg["sender"] == username:
            print(f'{msg["sender"]} to {msg["recipient"]}: {msg["message"]}')
       

def main():
    print("Welcome to the Simple CLI Chat Application")

    choice = input("Do you want to (1) Register or (2) Login? ")
    username = None

    if choice == '1':
        username = register_user()
        if username is None:
            return
    elif choice == '2':
        username = login_user()
        if username is None:
            return
    else:
        print("Invalid choice.")
        return

    while True:
        print("\nOptions:\n1. Send Message\n2. View Chat History\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            recipient = input("Enter recipient's username: ")
            message = input("Enter your message: ")
            send_message(username, recipient, message)
        elif choice == '2':
            view_chat_history(username)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
