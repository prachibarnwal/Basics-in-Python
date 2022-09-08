import matplotlib.pyplot as plt
age = [14,15,14,16,17,18,15,19,17,16,18,14,15,14,13,17,18,19,17,15,13,14,14,16]
age.sort()
plt.hist(age,bins = 3, color = "ORANGE")
plt.show()
