# Alex Castro - acastro23@student.gsu.edu
# Start date: August 21, 2023
# Reminder project


import datetime as dt
import time
from plyer import notification

# My list of reminders(currently being updated with new taks)
reminders = [
    {'Time': (16,30), 'message': "You must Study for one hour, starting now!"},
    {'Time': (17,30), 'message': "Take a 30 minute break, you deserve it!"},
    {'Time': (18,00), 'message': "Time to study for another hour."},
    {'Time': (19,00), 'message': "Reminder to go eat dinner, can't study on an empty stomach!"},
    {'Time': (20,30), 'message': "Time to study for two hours, GO!"},
    {'Time': (22,30), 'message': "You studied enough for tonight, relax for a while"},
    {'Time': (23,30), 'message': "It's 11:30, time to turn everything off and head to sleep, Good Night!"}
]

def CheckTime(reminders):
    CurrentTime = dt.datetime.now()

    for i in reminders:
        if(CurrentTime.hour, CurrentTime.minute) == reminders['Time']:
            #playing a notification sound: "oh my god bruh, oh hell nah..."

            notification.notify(
                title = "Reminder",
                message = reminders['message'],
                timeout = 7
            )

            time.sleep(60)
            break           # I am putting a break here to avoid multiple notifications 

        time.sleep(10)


if __name__ == "__main__":
    while True:
        CheckTime(reminders)
