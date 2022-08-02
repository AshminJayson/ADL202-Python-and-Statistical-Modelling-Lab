#Ashmin Jayson S4 DS Roll No : 14
#Experiment No : 18 Calculation of mean, median and mode
#Date : 22/06/22


table = [["Alabama", 4779736, 5.7], ["Alaska", 710231, 5.6], ["Arizona", 6392017, 4.7], ["Arkansas", 2915918, 5.6], ["California", 37253956, 4.4], ["Colorado", 5029196, 2.8], ["Conneticut", 3574097, 2.4], ["Delaware", 897934, 5.8]]

print("Input Data")
print("{:<12}{:<14}{:<12}".format("State","Population","Murderrate(per 100000)"))
for i in range(8):
    print("{:<12}{:<14}{:<12}".format(table[i][0],table[i][1],table[i][2]))

mean = 0
median = 0
variance = 0

mtable = []
for i in range(8) : 
    x = table[i][1] / 100000
    mtable.append(x * table[i][2])
    mean = mean + mtable[i]

mean = mean / 8
mtable.sort()
median = (mtable[3] + mtable[4]) / 2

#variance evaluation
for i in range(8):
    x = (mean - mtable[i]) ** 2;
    variance = variance + x

variance = variance / 8


print("\nThe mean of the data is : ", round(mean,2))
print("The median of the data is : ", round(median, 2))
print("The variance of the data is : ", round(variance, 2))
