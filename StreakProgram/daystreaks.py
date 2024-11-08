#-----------------------------
# Program: Day Streak Counter
# Author: Mandar Padole
# Version: 1.0
#-----------------------------

#----------Update Log---------
# 9/2/24: 
# Created file, documentaion, and update log.
# created program, variables, and other code.
#-----------------------------

# Modules
import datetime
import os


# Get the directory of the current script
scriptDir = os.path.dirname(os.path.abspath(__file__))


# File path to save/load the start date
filePath = os.path.join(scriptDir, "StreakStartDate.txt")


# Load startDate from the text file
def loadStartDate():
    if os.path.exists(filePath):
        with open(filePath, "r") as file:
            date_str = file.readline().strip()
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    else:
        return datetime.date.today()


# Save startDate to a file
def saveStartDate(start_date):
    with open(filePath, "w") as file:
        file.write(start_date.strftime("%Y-%m-%d"))


# Variables
#non-changable variables
dayOneStreak = 1
startDate = loadStartDate()

#current date
currDate = datetime.date.today()

#streak updater
streak = (currDate - startDate)
streak = streak.days
streak += dayOneStreak

#grammar control
daysOutput = ""
if streak != 1:
    daysOutput = "days"
else:
    daysOutput = "day"


# Clear Terminal
print("\033c")


# Program
running = 0
while running == 0:
  response = 0
  while response == 0:
    streakBreak = input("Has the streak been broken yet? (1 - Yes | 0 - No): ")
    if streakBreak == "0":
     print("\nGreat! The streak continues...")
     response = 1
    elif streakBreak == "1":
     print("\nStreak reseting... :/")
     print("Streak ended on day {}.\n".format(streak))

     startDate = currDate
     saveStartDate(startDate)
     streak = (currDate - startDate)
     streak = streak.days
     streak += dayOneStreak
     daysOutput = "day"

     response = 1
    else:
     print("Invalid input!")
  else:
     print("You have a current streak of", str(streak), "{}.\n\n".format(daysOutput))
     continueCode = input("Continue program? (1 - Yes | 0 - No) ")
     if continueCode == "0":
        print("Thanks for checking in on your streak!\n")
        running = 1
     elif continueCode == "1":
        print("Running it back...\n")
        response = 0
else:
   print("Program terminating...\n")