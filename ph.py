import re
regex = r'\b[1-9]{1}+[0-9]{10}\b'

n = input("Enter the phone number : ")


if(re.fullmatch(regex, n)):
    print("Invalid");
else:
    print("Invalid")
