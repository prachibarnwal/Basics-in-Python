import matplotlib.pyplot as plt
import pandas as pd
names = ["Rahul", "Rohit", "Hardik", "Virat", "Surya"]
score1 = [20,10,38,57,39]
score2 = [45,12,56,40,69]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','yellow']
plt.title("Cricket Score Sheet")

plt.pie(score1, labels = names, colors = colors)
plt.show()


