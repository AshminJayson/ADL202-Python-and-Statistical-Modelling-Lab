#Ashmin Jayson S4 DS Roll No : 14
#Experiment No : 14 Program to plot the graphs of various mathematical formula
#Date : 07/05/22

import matplotlib.pyplot as plt

def fact(x):
    if x == 0 or x == 1:
        return 1

    return x * fact(x - 1)

def sin(x):
    j = 1
    val = 0
    for i in range(1, 20):
        
        term = (x ** j) / fact(j)
        if i % 2 == 0:
            val = val - term
        else:
            val = val + term
        
        j = j + 2
    return val
    
    
    
print("MENU")
print("1.y = x")
print("2.y = x^2")
print("3,y = sin(x)")
print("4,y = 2^x")
print("5.y = x^0.5")
print("6.EXIT")


while 1:

    x = int(input("Enter the Option : "))
    xc = []
    floater = -10
    while floater < 10 :
        xc.append(floater)
        floater = floater + 0.1
        
    if x == 1:
        yc = [i for i in xc]
    elif x == 2:
        yc = [i * i for i in xc]
    elif x == 3:
        yc = [sin(i) for i in xc]
    elif x == 4:
        yc = [2**i for i in xc]
    elif x == 5:
        xc = range(0, 50)
        yc = [i**0.5 for i in xc]
    else:
        break
    plt.plot(xc, yc)
    plt.show()
