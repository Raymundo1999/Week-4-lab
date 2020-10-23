#Raymundo Sanchez
#CSS 225
#Oct 23, 2020
#lab


#This program will take a password from the user and print an appropriate message
#The 'in' keyword checks to see if a value exists somewhere in the given string.

#I got rid of the "in" in the code since it was bringing up in issue
#the issue was that it would give you a response even when giving a wrong password.
greeting = input("Hello, possible pirate! What's the password?")
if greeting == ("Arrr!"):
	print("Go away, pirate.")
else:
        print("Greetings, hater of pirates!")
