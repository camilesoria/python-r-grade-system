import sqlite3

# CONNECTING TO DATABASE
connection = sqlite3.connect('database.db')
cursor = connection.cursor() # Cursor transports data

# CREATING THE TABLE
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT  UNIQUE,
                    grade REAL
                 )
''')

connection.commit()

# IMPLEMENTING CRUD OPERATIONS

def create_user(name, email, grade):
    try:
        cursor.execute("INSERT INTO users(name, email, grade) VALUES (?,?,?)", (name, email, grade)) # Using '?' prevents SQL injection
        connection.commit()
        print(f"User {name} created successfully.")
        return True
    except Exception as e:
        print(f"Database Error: {e}")
        return False

def read_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("\n List of Users:")
    for user in users:
        print(f"ID: {user[0]} | Name: {user[1]} | Email: {user[2]} | Grade: {user[3]}")
    print("--------------------")
    if not users:
        print("No users found.")

def update_user(updateOption, name, email, grade, user_id):
   
    if updateOption == 1: # Updating Name
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
        print(f"User ID {user_id} update namely to {name} successfully.")
    
    elif updateOption == 2: # Updating Email
        cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, user_id))
        print(f"User ID {user_id} update email to {email} successfully.")

    elif updateOption == 3: # Updating Grade
        cursor.execute("UPDATE users SET grade = ? WHERE id = ?", (grade, user_id))
        print(f"User ID {user_id} update grade to {grade} successfully.")

    elif updateOption == 4: # Updating All
        cursor.execute("UPDATE users SET name = ?, email = ?, grade = ? WHERE id = ?", (name, email, grade, user_id))
        print(f"User ID {user_id} updated namely to {name }, email to {email}, and grade to {grade} successfully.")

    connection.commit()

def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    connection.commit()
    print(f"User ID {user_id} deleted successfully.")

# INPUT VALIDATION

def gradeValidation(): # Use grade validation to prevent errors and make sure grade is valid
    while True:
        try:
            grade = (float(input("Enter user grade: ")))
            if grade > 0 and grade < 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:  
            print("Invalid grade input. Please enter a valid value.")

def emailValidation(): # Used email validation to make sure email is valid and prevent input errors
    while True:
        d = 0
        a = 0
        email = input("Enter user email: ")
        if len(email) > 1: # Checking if email is not null
            for char in email:
                if char == '@':
                    a += 1
                elif char == '.':
                    d += 1 
            if a == 1 and d >= 1:
                return email
            else:
                print("Invalid email input. Please enter a valid email.")

def userIDValidation(): # Used user ID validation to make sure user ID is valid and prevent input errors
    while True:
        try:
            user_id = int(input("Enter user ID: "))
            return user_id
        except ValueError:
            print("Invalid ID input. Please enter a valid integer.")

# CONSOLE BASED INTERFACE

def print_menu():
    print("\nWelcome to the User Management System\n")
    print("Please choose the operation you want to perform:\n")
    print("1. Create User\n2. See all Users\n3. Update User\n4. Delete User\n5. Help\n6. Exit\n")

while True:
    print_menu()
    choice = input("Enter your choice (only numbers): ")

    while choice == '1': # Creating User
        name = input("User Name: ")
        email = emailValidation()
        grade = gradeValidation()
        create_user(name, email, grade)

        print("Do you want to create another user?")
        choice = input("Enter your choice (y/n): ")
        if choice.lower() == 'y':
            choice = '1'
        elif choice.lower() != 'y' and choice.lower() != 'n':
            print("Invalid input. Returning to main menu.")
        else: break

    if choice == '2': # Reading User
        read_users()

    while choice == '3': # Updating User
        user_id = userIDValidation()
        print("What do you want to update?")
        updateOption = int(input("Enter 1 for Name, 2 for Email, 3 for Grade, 4 for All: "))

        if updateOption not in [1, 2, 3, 4]:
            print("Invalid option selected. Returning to main menu.")
            break

        elif updateOption == 1: # Updating Name
            name = input("Enter new Name: ")
            update_user(updateOption, name, None, None, user_id)

        elif updateOption == 2: # Updating Email
            email = emailValidation()
            update_user(updateOption, None, email, None, user_id)

        elif updateOption == 3: # Updating Grade
            grade = gradeValidation()
            update_user(updateOption, None, None, grade, user_id)

        elif updateOption == 4: # Updating All
            name = input("Enter new Name: ")
            email = emailValidation()
            grade = gradeValidation()
            update_user(updateOption, name, email, grade, user_id)

        print("Do you want to update another user?")
        choice = input("Enter your choice (y/n): ")
        if choice.lower() == 'y':
            choice = '3'
        elif choice.lower() != 'y' and choice.lower() != 'n':
            print("Invalid input. Returning to main menu.")
        else: break

    while choice == '4':
        user_id = userIDValidation()
        delete_user(user_id)

        print("Do you want to delete another user?")
        choice = input("Enter your choice (y/n): ")
        if choice.lower() == 'y':
            choice = '4'
        elif choice.lower() != 'y' and choice.lower() != 'n':
            print("Invalid input. Returning to main menu.")
        else: break

    if choice == '5':
        print("Welcome to the Help Section!")
        print("In this program, you can manage users by selecting the desired operation from the menu.")
        print("1. Create User: Add a new user to the database by providing a name and email.")
        print("2. See all Users: Display a list of all users stored in the database.")
        print("3. Update User: Modify the details of an existing user by providing their ID, new name, and new email.")
        print("4. Delete User: Remove a user from the database by providing their ID.")
        print("5. Help: Display help section.")
        print("6. Exit: Exit the program and close the connection.")
        choice = input("Press Enter to return to the main menu. ")
        if choice == '':
            continue
    
    elif choice == '6':
        print("Thank you for using the User Management System. Goodbye!")
        connection.close()
        break