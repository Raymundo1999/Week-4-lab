#Raymundo Sanchez
#CSS 225
#Oct 23,2020
#Lab

#This program takes the current time in hours between 0-23
#and the number of hours the user will wait.
#It will print what the time is in hours (between 0-23) after the user is done waiting
currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")


currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)
#The issue that this had was that it did not have a modulo that was required
#this helped it restart after the hour 24 and so it doesn't go past the hour 24.
finalTimeInt = (currentTimeInt + waitTimeInt) %24
print(finalTimeInt)
