import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("~/engineering/lab1/fitness.txt", dtype= int, skiprows= 10)
print(data)

plt.ylim(-2,2)
##plt.show()