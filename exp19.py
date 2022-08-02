#Ashmin Jayson S4 DS Roll No : 14
#Experiment No : 22 Checking independance using chi-square value
#Date : 29/06/2022

t = [[60, 54, 46, 41, 201],[40, 44, 53, 57, 194], [100, 98, 99, 98, 395]]

print("{:^8}{:^12}{:^12}{:^12}{:^12}{:^12}".format("", "HighSchool", "Bachelors", "Masters", "Phd", "Total"))
for i in range(3):
    if i == 0:
        print("{:^8}{:^12}{:^12}{:^12}{:^12}{:^12}".format("Female",t[i][0], t[i][1], t[i][2], t[i][3], t[i][4]))
    elif i == 1:
    	print("{:^8}{:^12}{:^12}{:^12}{:^12}{:^12}".format("Male",t[i][0], t[i][1], t[i][2], t[i][3], t[i][4]))
    else:
    	print("{:^8}{:^12}{:^12}{:^12}{:^12}{:^12}".format("",t[i][0], t[i][1], t[i][2], t[i][3], t[i][4]))
    	
calcchi = 0
tablechi = 7.815

for i in range(2):
	for j in range(4):
		ob = t[i][j]
		exp = (t[i][4] * t[2][j]) / t[2][4]
		t[i][j] = round(exp, 2)
		val = (((ob - exp) ** 2)) / exp
		calcchi = calcchi + val
		
print("\nExpected values : ")
print("{:^8}{:^12}{:^12}{:^12}{:^12}".format("", "HighSchool", "Bachelors", "Masters", "Phd"))
for i in range(2):
    if i == 0:
        print("{:^8}{:^12}{:^12}{:^12}{:^12}".format("Female",t[i][0], t[i][1], t[i][2], t[i][3]))
    elif i == 1:          
    	print("{:^8}{:^12}{:^12}{:^12}{:^12}".format("Male",t[i][0], t[i][1], t[i][2], t[i][3]))



print("\n\nThe calculated value of chi-square is : ", round(calcchi,3))
print("The table value of chi-square is : ", tablechi)

if tablechi < calcchi:
	print("Therefore relationship is dependent")
else:
	print("Therefore relationship is independent")
	
	

