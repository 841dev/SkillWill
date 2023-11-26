import json
import uuid
import menu
import diarybook

class Authorization():
    def __init__(self):

        self.first_of_all = {
            "1": self.register,
            "2": self.login,
            "3": self.ext
        }

    def login(self):
        print("Please enter your Username and Passwod ")

        self.user_name = input(" Please enter user name:  ")

        self.access_granted = False

        with open('users.json', 'r') as file:
            data = json.load(file)
            x = 0
            for i in data["users"]:
                if self.user_name == data["users"][x].get("username"):
                    self.user_pass = input(" Please enter a password:  ")
                    if self.user_pass == data["users"][x].get("userpass"):
                        print("Welcome")
                        # print(f'Logged in user ID is: {data["users"][x].get("id")}')
                        self.access_granted = True
                        break
                    else:
                        print("The password is incorrect, please try again")

                else:
                    x = x + 1

        if self.access_granted:
            print("Access Granted")
            print(f'Logged in user ID is: {data["users"][x].get("id")}')
            exit()
        else:
            print(f"There is no such username ' {self.user_name} ' , please try again")
            self.login()

    def register(self):
        print("New User Registration")

        self.user_id = uuid.uuid4().hex
        self.user_name = input(" Please enter user name:  ")
        self.user_pass = input(" Please enter a password:  ")
        self.user_mail = input(" Please enter your mail:  ")

        new_user = {
            'id':self.user_id,
            'username':self.user_name.lower(),
            'userpass':self.user_pass,
            'mail':self.user_mail
        }
        with open('users.json', 'r') as file:
            data = json.load(file)
            x=0
            #print(len(data["users"][x].get("username")))
            for i in data["users"]:
                if self.user_name == data["users"][x].get("username"):
                    print("This user name is already in use, next time please chose different user name and try again.")
                    self.register()
                else:
                    x=x+1

        #print("there is no such a user in db")
        data["users"].append(new_user)
        with open('users.json', 'w') as file:
            json.dump(data, file, indent=4)
            print(f"The new user: {self.user_name} with mail: {self.user_mail} has been registered successfully")

        self.run_app()



    def display_menu(self):
        print("""
            Diary Autorization
            
            1. Register
            2. Login
            3. Exit
            
        """)

    def run_app(self):
        self.display_menu()
        choice = input("Enter an Option  ")
        action = self.first_of_all.get(choice)
        if action:
            action()
        else:
            print("{0} is not a valid choice".format(choice))

    def ext(self):
        exit()

if __name__ == "__main__":
    Authorization().run_app()