#Ashmin Jayson S4 DS Roll No : 14
#Experiment 15 : Program to plot bar graph of continental area
#Date : 07/06/22

import matplotlib.pyplot as plt

areas = {"Africa" : 11.7, "Asia" : 10.4, "Europe" : 1.9, "North America" : 9.4, "Oceania" : 3.3, "South America" : 6.9, "Soviet Union" : 7.9}

plt.title("Continent area bar graph")
cont = list(areas.keys())
val = list(areas.values())
for i in range(0, 7):
    plt.text(i, val[i], val[i])

plt.bar(areas.keys(), areas.values())
plt.xlabel("Continents")
plt.ylabel("Area(In million sq kms)")
plt.show()
