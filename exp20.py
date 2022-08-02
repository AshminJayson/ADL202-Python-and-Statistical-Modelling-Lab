# Ashmin Jayson 14 S4 DS
# ExperimentNo : 21 Program to find the correlation coefficient of the given data
# Date : 29/06/2022

t = [["A", 17, 150, 0, 0, 0, 0, 0], ["B", 15, 154, 0, 0, 0, 0, 0], ["C", 19, 169, 0, 0, 0, 0, 0], ["D", 17, 172, 0, 0, 0, 0, 0], ["E", 21, 175, 0, 0, 0, 0, 0]]

handm = 0
heightm = 0

for i in range(5):
	handm = handm + t[i][1]
	heightm = heightm + t[i][2]
	
handm = handm / 5
heightm = heightm / 5
t1 = 0
t2 = 0
t3 = 0
print("{:<7}{:<7}{:<7}{:^7}{:^7}{:^7}{:^7}{:^7}".format("Person","Hand", "Height", "e", "f", "e * f", "e^2", "f^2"))
for i in range(5):
	t[i][3] = t[i][1] - handm
	t[i][4] = t[i][2] - heightm
	t[i][5] = t[i][3] * t[i][4]
	t[i][6] = t[i][3] ** 2
	t[i][7] = t[i][4] ** 2
	t1 = t1 + t[i][5]
	t2 = t2 + t[i][6]
	t3 = t3 + t[i][7]
	print("{:<7}{:<7}{:<7}{:<7.1f}{:<7.1f}{:<7.1f}{:<7.1f}{:<7.1f}".format(t[i][0],t[i][1],t[i][2],t[i][3],t[i][4], t[i][5], t[i][6], t[i][7]))
	
	
corr = t1 / ((t2 * t3) ** 0.5)
print("\nThe correlation coefficent is : ", round(corr,3))

#Output
# The correlation coefficient is : 0.721
	
