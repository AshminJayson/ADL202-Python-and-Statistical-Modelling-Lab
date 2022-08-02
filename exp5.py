# Ashmin Jayson 14 S4 DS
# ExperimentNo : 6 Program to check for the validity of an email address
# Date : 10/05/2022
import re

regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'

s = input("Enter the email id : ")

if(re.fullmatch(regex, s)):
    print("The email address is valid")
else:
    print("The email address is invalid")
    
    
#Output : 
# Enter the email id : ash@gmail.com
# The email address is valid

