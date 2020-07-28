import pyrebase

config = {
    "apiKey": "AIzaSyDc_2yi1RMCG7xllIcGzlasfQuQa7m3vzk",
    "authDomain": "gocorona-324e4.firebaseapp.com",
    "databaseURL": "https://gocorona-324e4.firebaseio.com",
    "projectId": "gocorona-324e4",
    "storageBucket": "gocorona-324e4.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


class Authentication:

    @staticmethod
    def create_user(email, password):
        auth.create_user_with_email_and_password(email, password)
        print("Congraulations , successfully registered!")

    @staticmethod
    def signin_process(email, password):
        auth.sign_in_with_email_and_password(email, password)
        print("Congraulations , successfully logged in!")

    @staticmethod
    def check_for_password_length(password):
        if len(password) >= 8:
            return True

        else:
            print("Weak password!")
            return False

