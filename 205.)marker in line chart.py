import pandas as pd
import matplotlib.pyplot as plt
names = ["Apoorva","Prachi","Jiya","Gayatri","Tanisha","Vaibhavi","Manasvi"]
attendance = [94,50,75,80,30,98,60]
marks = [96,93,94,89,95,96,87]
xyz = [19,28,50,69,40,32,89]
plt.xlabel("Names-->")
plt.ylabel("Records (in %) -->")
plt.title("Students's Attendance Chart")
plt.ylim((0,100))
plt.yticks((10,20,30,40,50,60,70,80,90,100))
plt.plot(names,attendance, color = '#99ff99', linestyle=(0, (3, 1, 1, 1, 1, 1)), marker = "s",
         markersize=15, markerfacecolor='green')
plt.plot(names,marks, color = 'cyan', linestyle='dashdot', marker = "p",
         markersize=20, markerfacecolor='blue')
plt.plot(names,xyz, color = 'red', linestyle='dashed', marker='o',
         markerfacecolor='pink', markersize=17)
plt.legend(["class attandance","marks ","library attendance"], loc = 'lower center')

plt.show()
