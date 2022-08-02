# Ashmin Jayson 14 S4 DS
# ExperimentNo : 8 Program to add two matrices
# Date : 17/05/2022

print("Enter no of rows and columns of matrix 1 : ")
r1 = int(input())
c1 = int(input())

a = []
b = []
print("Enter the elements of matrix 1 : ")
for i in range(r1) : 
    temp = []
    for j in range(c1):
        temp.append(int(input()))
    a.append(temp)

print("Enter no of rows and columns of matrix 2 : ")
r2 = int(input())
c2 = int(input())

print("Enter the elements of matrix 2 : ")

for i in range(r2): 
    temp = []
    for j in range(c2):
        temp.append(int(input()))
    b.append(temp)

c = []
if r1 == r2 and c1 == c2 : 
    for i in range(r1):
        temp = []
        for j in range(c1):
            x = a[i][j] + b[i][j]
            temp.append(x)
        c.append(temp)
        
    print("The sum matrix is : ")
    for i in c : 
    	print(i)
else:
    print("The matrices are incompatible")
    
    
Output : 
Enter no of rows and columns of matrix 1 : 
2
2
Enter the elements of matrix 1 : 
1
2
3
4
Enter no of rows and columns of matrix 2 : 
2
2
Enter the elements of matrix 2 : 
4
3
2
1
The sum matrix is : 
[5, 5]
[5, 5]
