# Ashmin Jayson 14 S4 DS
# ExperimentNo : 1 Program to find the largest of three numbers
# Date : 10/05/2022

print("Enter the three numbers : ")
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c: 
    print(a, "is the largest")
elif b >= c and b >= a : 
    print(b, "is the largest")
else:
    print(c, "is the largest")

#Output : 
# Enter the three numbers : 
# 4
# 3
# 5
# 5 is the largest
