# Ashmin Jayson 14 S4 DS
# ExperimentNo : 11 Program to read numbers from a file and print the prime numbers
# Date : 24/05/2022

f = open("numbers.txt", "r")

lines = f.readlines()
print("The prime numbers are : ")

for l in lines :
    a = map(int,l.split(" "))
    for c in a :
        if c == 2 or c == 1 :
            print(c)
        else : 
            i = 2
            flag = 1
            for i in range(2, c):
                if c % i == 0 : 
                    flag = 0
                    break

            if flag == 1:
                print(c)

f.close()       

# Output : 
# The prime numbers are : 
# 431
# 1
# 2
# 3
# 5


