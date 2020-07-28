import auth

auth = auth.Authentication()

class Users:
    email = " "
    password = " "


    def user_choice(self):
        print(" Would you like to register or login? \n 1 : Register \n 2 :Login")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            self.user_input()
            self.check_password()
            self.register_user()

        elif choice == 2:
            self.user_input()
            self.check_password()
            self.login_user()

        else:
            print("Please select a valid input!")

    def user_input(self):
        print("Enter data!")
        self.email = input("Enter your email:")
        self.password = input("Enter your password:")

    def register_user(self):
         auth.create_user(self.email, self.password)

    def login_user(self):
        auth.signin_process(self.email, self.password)

    def check_password(self):
        auth.check_for_password_length(self.password)




user = Users()
user.user_choice()
