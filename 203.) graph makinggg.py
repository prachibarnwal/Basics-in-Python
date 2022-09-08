import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)

y1 = [30,35,22,50,40]
y2 = [45,23,45,55,39]
plt.bar(x,y1,width = 0.45)
plt.bar(x + 0.45,y2,width = 0.45)
plt.show()
