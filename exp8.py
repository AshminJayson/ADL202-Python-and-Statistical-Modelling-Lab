# Ashmin Jayson 14 S4 DS
# ExperimentNo : 9 Program to print even and odd tuple
# Date : 17/05/2022


a = tuple(map(int, input("Enter the tuple elements : ").split()))

print("Odd positions are : ", a[1::2])
print("Even positions are : ", a[::2])

# Output : 
# Enter the tuple elements : 1 2 3 4 5 6 
# Odd positions are : 
# [2, 4, 6]
# Even positions are : 
# [1, 3, 5]

