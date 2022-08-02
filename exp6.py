# Ashmin Jayson 14 S4 DS
# ExperimentNo : 7 Program to remove all occurances of a number from a list
# Date : 17/05/2022


a = list(map(int, input("Enter the list elements : ").split()))

for i in a : 
    count = 0
    for k in a :
        if k == i :
            count = count + 1
    for j in range(1, count):
        a.remove(i)

print("The modified list is : ", end = " ")
print(a)

Output : 
Enter the list elements : 4 3 2 1 1 2 2 3 4 5 
The modified list is :  [1, 2, 3, 4, 5]
