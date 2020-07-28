class Body_Temperature:

    def input_temperature(self):
        temp = float(input("Enter your body temperature in *F:"))
        print(temp, "*F")

        if (temp < 99.5):
            print("You are safe.")
        elif (99.5 <= temp <= 100.5):
            print("Take care!")
        else:
            print("You are at risk!")


class Check:

    def choose_your_symptoms(self):
        print("Choose your symptoms!")
        print("1: Cough \n 2: Fever \n 3: Tiredness \n 4: Difficulty in Breathing ")

        c = int(input("Do you have cough? \n 1: Yes \n 0: No \n"))
        f = int(input("Do you have fever? \n 1: Yes \n 0: No \n"))
        t = int(input("Do you feel tired? \n 1: Yes \n 0: No \n"))
        b = int(input("Do you have difficulty in breathing? \n 1: Yes \n 0: No \n"))

        if (c == 1 and f == 1 and t == 1 and b == 1):
            print("Please check yourself!")
        elif (c == 0 and f == 0 and t == 0 and b == 0):
            print("You are immortal!")
        elif ((c == 0 and f == 1 and t == 1 and b == 1) or (c == 1 and f == 0 and t == 1 and b == 1) or (c == 1 and f == 1 and t == 1 and b == 0) or (c == 1 and f == 1 and t == 0 and b == 1)):
            print("Please take care of your health!")
        elif ((c == 0 and f == 0 and t == 1 and b == 1) or (c == 0 and f == 1 and t == 0 and b == 1) or (c == 0 and f == 1 and t == 1 and b == 0) or (c == 1 and f == 0 and t == 0 and b == 1) or (c == 1 and f == 0 and t == 1 and b == 0) or (c == 1 and f == 1 and t == 0 and b == 0)):
             print("Unsure symptoms!")
        elif ((c == 0 and f == 0 and t == 0 and b == 1) or (c == 0 and f == 0 and t == 1 and b == 0) or (c == 0 and f == 1 and t == 0 and b == 0) or (c == 1 and f == 0 and t == 0 and b == 0)):
             print("You are safe!")
        else:
            print("Sorry invalid input!")


body = Body_Temperature()
body.input_temperature()
check = Check()
check.choose_your_symptoms()
