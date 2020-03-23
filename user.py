import csv
import hashlib
import os.path

# This class handles all relevant actions for the User
class User:
    # Defining a user
    def __init__(self, user_firstname, user_lastname, user_email, user_gender, user_id, user_pass):
        self.__user_firstname = user_firstname
        self.__user_lastname = user_lastname
        self.__user_email = user_email
        self.__user_gender = user_gender
        self.__user_id = user_id
        self.__user_pass = user_pass

    # Creating a user
    def create_user(self):
        if self.check_if_user_exists(self.__user_id):
            return 'User Exists' # User is being informed if user already exists
        else:
            hashedpass = hashlib.sha256(self.__user_pass.encode()).hexdigest() #Encrypt pass
            if os.path.isfile('user.csv'): # Check if the file exists, if yes it will append, otherwise create a new one
                with open('user.csv', 'a', newline='') as file:
                    userscsv = csv.writer(file)
                    userscsv.writerow([self.__user_firstname, self.__user_lastname, self.__user_email, self.__user_gender, self.__user_id, hashedpass])
            else: # Otherwise it will create a new file with CSV headers
                with open('user.csv', 'w', newline='') as file:
                    userscsv = csv.writer(file)
                    userscsv.writerow(["First_Name", "Last_Name", "Email", "Gender", "Username", "Password"])
                    userscsv.writerow([self.__user_firstname, self.__user_lastname, self.__user_email, self.__user_gender, self.__user_id, hashedpass])
            return f'Welcome {self.__user_firstname}' # If this is a valid registration we welcome the user

    # Checks if a user exists (used by create_user)
    def check_if_user_exists(self, user):
        if os.path.isfile('user.csv'):  # We start by checking the user.csv exists
            with open('user.csv', newline='') as file:
                usersdict = csv.DictReader(file)
                for row in usersdict:
                    return user in row['Username']
        else:
           pass

    # User Login
    def validate_user(self):
        if os.path.isfile('user.csv'): # We start by checking the user.csv exists
            with open('user.csv', newline='') as file:
                usersdict = csv.DictReader(file)
                for row in usersdict:
                    if self.__user_id in row['Username']:
                        password = hashlib.sha256(self.__user_pass.encode()).hexdigest()
                        if password in row['Password']:
                            return f'Welcome {self.__user_id}'
                        else:
                            return f'Password is incorrect'
                    else:
                        return 'User not found'
        else:
           return 'User database is missing, cannot process login.'