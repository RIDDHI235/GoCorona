import time

class Reminder:

    def set_reminder(self):
        reminder = str(input("What shall i remind you about??"))
        set = float(input("Enter the time interval (in mins): "))
        set = set*60
        while (True):
            time.sleep(set)
            print(reminder)
            stop = int(input("Do you wish to stop the reminder?? \n 1: Yes \n 0: No \n"))
            if stop == 1:
                print("Thank you")
                break









reminder = Reminder()
reminder.set_reminder()

