# Reminder-Project-python
This program has a list of reminders of what the user should be doing throughout the evening, and it will show a notification on the user's desktop

All the reminders are stored in a list of dictionaries. These dictionaries include the time and message. This list is then run through a for loop that will check the current time to see if it corresponds to any of the times in the reminders' list, and if it finds a match, then it will show a notification and then break out of the loop. After a notification is activated then the program will puase for 60 seconds to avoid activating the same reminder multiple times. If while iterating through the foor loop, the current time does not correspond with any of the times in the reminders' list then the program will sleep for 10 seconds before continuing again. 

Libraries used in this program: datetime, time, plyer
