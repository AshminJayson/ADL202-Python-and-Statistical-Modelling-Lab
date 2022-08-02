# Ashmin Jayson 14 S4 DS
# ExperimentNo : 12 Program to count letters, words, lines and special characters in a file
# Date : 24/05/2022

import os

f = open('test.txt', 'r')
# print(os.listdir())
lines = f.readlines()



s, w, ul, ll, ss = 0, 0, 0, 0, 0


spclsym = ['\\','~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+',"|","{","}","[","]",";",":","'",'"',",","<",".",">","/","?"]

for line in lines : 
    s = s + 1
    
    for c in line : 
        if c.isupper() : 
            ul = ul + 1 
        if c.islower() :
            ll = ll + 1
        if c in spclsym :
            ss = ss + 1

    l = list(line.split(" "))
    # print(l)
    for i in l :
        if i != "":
            w = w + 1

f.close()

print("Number of words : ", w)
print("Number of lines : ", s)
print("Number of letters : ", ll + ul)
print("Number of lowercase letters : ", ll)
print("Number of uppercase letters : ", ul)
print("Number of special symbols : ", ss)


