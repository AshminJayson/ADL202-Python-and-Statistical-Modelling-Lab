# Ashmin Jayson 14 S4 DS
# ExperimentNo : 5 Program to replace a word by another in a sentence
# Date : 10/05/2022

sltr = input("Enter the string : ")
rep = input("Enter the string to be replaced : ")
swap = input("Enter the replacement : ")


while sltr.find(rep) != - 1: 
    index = sltr.find(rep)
    sltr = sltr[:index] + swap + sltr[index + len(rep):]
print("The new string is : ", sltr)

#Output: 
# Enter the string : hello there
# Enter the string to be replaced : hello
# Enter the replacement : hey
# The new string is :  hey there

