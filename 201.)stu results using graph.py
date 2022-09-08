import pandas as pd
import matplotlib.pyplot as plt
data = {"Names" : ["ABC","XYZ","PQR","LMN"],
                   "English" : [89,90,93,78],
                   "Computer S." : [67,78,88,80],
                   "Maths" : [90,67,88,92]}
df = pd.DataFrame(data)
print(df)
df.plot(kind = 'bar')
plt.show()
