import matplotlib.pyplot as plt
import pandas as pd
names = ["Rahul", "Rohit", "Hardik", "Virat", "Surya"]
score1 = [20,10,38,57,39]
score2 = [45,12,56,40,69]
plt.title("Cricket Score Sheet")
plt.xlabel("names")
plt.ylabel("scores")
dt = {"Names" : names, "Score 1" : score1, "Score 2 " : score2}
df = pd.DataFrame(dt)
df.plot()
plt.show()


