#Ashmin Jayson S4 DS Roll No : 14
#Experiment No : 16 Program to Create Student marklist and store it in a file, create bar graphs for marks and failed students
#Date : 15/06/22


import matplotlib.pyplot as plt

class student:
    def __init__(self, rno, name, marks, tm, per):
        self.rno = rno
        self.name = name
        self.marks = marks
        self.tm = tm
        self.per = per

    def __eq__(self, other):
        return self.per == other.per

    def __lt__(self, other):
        return self.per > other.per


failed = {"S1" : 0, "S2" : 0, "S3" : 0, "S4" : 0, "S5" : 0, "S6" : 0}
grades = { "90-100" : 0, "80-89" : 0, "70-79" : 0, "60-69" : 0, "50-59" : 0, "40-49" : 0, "<40" : 0}
f = open("marklist.txt", "w")
n = int(input("Enter the no of students : "))
rec = []
for i in range(n):
    rno = int(input("Enter the roll no of student : "))
    name = input("Enter the name of student : ")
    marks = list(map(int, input("Enter the marks of six subjects : ").split()))
    f.write("Roll No : " + str(rno) + " Name : " + name + " Marks : " + str(marks))
    tm = 0
    for i in range(6) :
        tm = tm + i
        if marks[i] > 90:
            grades["90-100"] = grades["90-100"] + 1
        elif marks[i] > 80:
            grades["80-89"] = grades["80-89"] + 1
        elif marks[i] > 70:
            grades["70-79"] = grades["70-79"] + 1
        elif marks[i] > 60:
            grades["60-69"] = grades["60-69"] + 1
        elif marks[i] > 50:
            grades["50-59"] = grades["50-59"] + 1
        elif marks[i] > 40:
            grades["40-49"] = grades["40-49"] + 1
        else:
            grades["<40"] = grades["<40"] + 1
            failed["S"+str(i+1)] = failed["S"+str(i+1)] + 1
    f.write(" Total : " + str(tm))
    f.write(" Percentage : " + str(tm/6))
    f.write("\n")
    rec.append(student(rno, name, marks, tm, tm/6))

rec.sort()

#Ranklist
print("\n\nRankList : ")

j = 1
print("Rank  Rno  Name       S1 S2 S3 S4 S5 S6  TotalMarks  Percentage")
for i in rec : 
    print('{:<6}'.format(str(j)) + '{:<5}'.format(str(i.rno)) + '{:<11}'.format(i.name), end = '')
    for k in i.marks:
        print('{:<3}'.format(k), end = '')
    print(" ", end = '')
    print('{:^12}'.format(str(i.tm)) + '{:.2%}'.format(i.tm/600));
    j = j + 1

print("\n\nFailed Students : ")
print("Rno  Name       S1 S2 S3 S4 S5 S6  TotalMarks  Percentage")
for i in rec : 
    if i.per < 40 : 
    	print('{:<5}'.format(str(i.rno)) + '{:<11}'.format(i.name), end = '')
    	for k in i.marks:
        	print('{:<3}'.format(k), end = '')
    	print(" ", end = '')
    	print('{:^12}'.format(str(i.tm)) + '{:.2%}'.format(i.tm/600));
        
#Count
print("\n\nCount of various categories : ")
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0

for i in rec : 
    if i.per > 90 :
        a = a + 1
    elif i.per > 80:
        b = b + 1
    elif i.per > 70:
        c = c + 1
    elif i.per > 60:
        d = d + 1
    elif i.per > 50:
        e = e + 1
    elif i.per > 40:
        f = f + 1
    else:
        g = g + 1

#Percentages
print("Percentage > 90 : " + str(a))
print("Percentage b/w 80 and 90 : " + str(b))
print("Percentage b/w 70 and 80 : " + str(c))
print("Percentage b/w 60 and 70 : " + str(d))
print("Percentage b/w 50 and 60 : " + str(e))
print("Percentage b/w 40 and 50 : " + str(f))
print("Percentage < 40 : "+ str(g))

#Bar Graphs
plt.bar(grades.keys(), grades.values())
plt.title("Marks/Numberofstudents Bar Graph")
plt.xlabel("Marks")
plt.ylabel("No of Students")
plt.show()
plt.bar(failed.keys(), failed.values())
plt.title("Failed Students per subject graph")
plt.xlabel("Subjects")
plt.ylabel("No of Students who failed")
plt.show()
