import pandas as pd
import matplotlib.pyplot as plt
names = ["Apoorva","Prachi","Jiya","Gayatri","Tanisha","Vaibhavi","Manasvi"]
attendance = [94,50,75,80,10,98,60]
plt.xlabel("Names")
plt.ylabel("Attendance (in %)")
plt.title("Students's Attendance Chart")
plt.ylim((0,150))
plt.yticks((10,20,30,40,50,60,70,80,90,100,110,120,130,140,150))
plt.bar(names,attendance, color = ['yellow','pink','gray','orange','cyan','#99ff99','green'])
plt.show()
