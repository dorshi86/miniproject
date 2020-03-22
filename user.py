import csv
import hashlib
import os.path

class User:
    def __init__(self, user_firstname, user_lastname, user_email, user_gender, user_id, user_pass):
        self.__user_firstname = user_firstname
        self.__user_lastname = user_lastname
        self.__user_email = user_email
        self.__user_gender = user_gender
        self.__user_id = user_id
        self.__user_pass = user_pass

    def create_user(self):
        if self.check_if_user_exists(self.__user_id):
            return 'User Exists'
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

    def check_if_user_exists(self, user):
        if os.path.isfile('user.csv'):  # Check if the file exists
            with open('user.csv', newline='') as file:
                usersdict = csv.DictReader(file)
                for row in usersdict:
                    return user in row['Username']
        else:
           pass

    def login(self):
        pass

    def validate_user(self, user, password):
        if os.path.isfile('user.csv'):  # Check if the file exists
            with open('user.csv', newline='') as file:
                usersdict = csv.DictReader(file)
                for row in usersdict:
                    if user in row['Username']:
                        password = hashlib.sha256(password.encode()).hexdigest()
                        return password in row['Password']
                    else:
                        return 'User not found'
        else:
           pass

    def validate_email(self):
        pass

Dor=User('Dor','Shiloni','dorshi@gmail.com','Male','dorshi','2840')
Dor.create_user()
#User.check_if_user_exists(1,'dorshsi')
print(User.validate_user(1,'dorfshi','2840'))