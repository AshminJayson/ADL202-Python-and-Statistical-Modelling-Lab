# Ashmin Jayson 14 S4 DS
# ExperimentNo : 3 Program to print the fibonacci series upto n
# Date : 10/05/2022

n = int(input())

if n == 0:
    print()
elif n == 1:
    print(0)
else : 
    a = 0
    b = 1
    print(a, b, end = " ")
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c, end = " ")
