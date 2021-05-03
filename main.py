import uuid
import re
import os
import pprint
from send_mail import recognition

BASE_DATABASE = os.path.abspath(__file__)
FILE_DATABASE = os.path.dirname(BASE_DATABASE)
ABS_DATABAE = os.path.join(FILE_DATABASE, "database.txt")
with open(ABS_DATABAE, "r") as k:
    Database = k.read()
    Database = eval(Database)


# # print(type(Database))
# # pprint.pprint(Database)


class Register:
    def __init__(self):
        self.username = input("Enter your Username : ")
        self.email = input("Enter your Gmail address : ")
        self.password = input("Enter your password : ")

    def check_username(self):
        for user in Database:
            if Database[user]["username"] == self.username:
                return False
        return True

    def valid_email(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, self.email):
            return True
        else:
            return False

    def check_email(self):
        for user in Database:
            if Database[user]["email"] == self.email:
                return False
        return True


def SignOrLog():
    user = Register()
    if user.check_username() and user.check_email() and user.valid_email():
        data = createUser(username=user.username,
                          email=user.email, password=user.password)
        data.add_to_database()
        print("SuccessFull Sign up let's Check your email 🥳")
    elif not user.check_username() and user.check_email() and user.valid_email():
        print("Unfortunately This Username use before 😔😔😔 !!! ")
        print("Let's Try again 😄😄😄 ")
        SignOrLog()
    elif user.valid_email() and user.check_username() and not user.check_email():
        print("Wonderfull This Email SIGN UP before ☠️ ")
        doit = input("Do You Want To Login Y/N : ")
        if doit == "Y":
            login = loginUser(user.email)
            login.Login()
        else:
            print("Good Bye freinds 😭")
    elif user.check_username() and user.check_email() and not user.valid_email():
        print("Email Was INVALID 🍉  ")
        SignOrLog()
    elif not user.check_username() and not user.check_email() and user.valid_email():
        print("Wonderfull This Email and Username SIGN UP before ☠️ ")
        doit = input("Do You Want To Login Y/N : ")
        if doit == "Y":
            login = loginUser(user.email)
            login.Login()
        else:
            print("Good Bye freinds 😭")


class createUser:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def add_to_database(self):
        dict = {}
        dict['username'] = self.username
        dict['email'] = self.email
        dict['password'] = self.password
        Database[uuid.uuid1().hex] = dict
        with open(ABS_DATABAE, "w") as k:
            finally_database = str(Database)
            k.write(finally_database)
        recognition(self.username, self.email, turn="SIGN UP")
        # print(x)


class loginUser:
    def __init__(self, email):
        self.username = input("Enter Your Username ☠️  :")
        self.password = input("Enter Your Username ☠️  :")
        self.email = email

        for user in Database:
            if Database[user]["email"] == email:
                self.user = user

    def Login(self):
        if self.username == Database[self.user]["username"] and self.password == Database[self.user]["password"]:
            print("You Are Login")
            recognition(self.username, self.email, turn="LOG IN")
        else:
            print("Username and Password was Wrong 😟 ")


SignOrLog()

# pprint.pprint(Database)


# for user in Database:
#     print(Database[user]["email"])
