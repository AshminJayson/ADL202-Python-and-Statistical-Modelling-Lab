#Ashmin Jayson S4 DS Roll No : 14
#Experiment No : 23 T test for checking NULL hypothesis
#Date : 6/7/22

smean, ssd, size, pmean, sig = 22, 3, 16, 20, 0.05
z = ((size**0.5)*(smean-pmean))/ssd
t = 1.753

print("The table value of t is :", t, " and the calculated value of z is : ", round(z,3));
if z > t:
    print("Null hypothesis is rejected as Z is in the rejection region, therefore the new model has a higher mileage")
else:
    print("Null hypothesis is not rejected")
    
#Output
#The table value of t is : 1.753  and the calculated value of z is :  2.667
#Null hypothesis is rejected as Z is in the rejection region, therefore the new model has a higher mileage

