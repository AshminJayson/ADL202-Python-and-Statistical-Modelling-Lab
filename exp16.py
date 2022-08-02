#Ashmin Jayson S4 DS Roll No : 14
#Experiment No : 19 Calculation of Standard Deviation and Coefficient of variation
#Date : 22/06/22


t = [[0, 10, 5], [10, 20, 10], [20, 30, 20], [30, 40, 40], [40, 50, 30], [50, 60, 20], [60, 70, 10], [70, 80, 5]]

print("Input Data")
print("Class    ",end = "  ")
for i in range(8):
    print(t[i][0], "-", t[i][1], end = " ")
print("")
print("Frequency  ", end = "  ")
for i in range(8):
    print(t[i][2], end = "      ")

mean = 0
fisum = 0
for i in range(8):
    x = (t[i][1] + t[i][0]) / 2
    mean = mean + (x * t[i][2])
    fisum = fisum + t[i][2]

mean = mean / fisum
variance = 0
for i in range(8):
    x = (t[i][1] + t[i][0])/2
    x = (x - mean) ** 2
    variance = variance + (x* t[i][2])

variance = variance / fisum
sd = variance ** 0.5
print("\n\nThe standard deviation of the data is : ", sd)
print("The Coeffiecient of Variation(CV) of the data is : ", sd/mean)



