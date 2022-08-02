# Ashmin Jayson 14 S4 DS
# ExperimentNo : 4 Program to print the surface area and volume of a cylinder
# Date : 10/05/2022

def sa(r, h):
    return 2 * 3.14 * r * r + 2 * 3.14 * r * h

def v(r, h):
    return 3.14 * r * r * h


r = int(input("Enter the radius of the cylinder : "))
h = int(input("Enter the height of the cylinder ; "))

print("The total surface area of the cylinder is : ", sa(r, h))
print("The volume of the cylinder is : ", v(r, h))


#Output : 
Enter the radius of the cylinder : 4
Enter the height of the cylinder ; 12
The total surface area of the cylinder is :  401.92
The volume of the cylinder is :  602.88

