import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data.txt", dtype= int)
plt.plot(data)
plt.savefig("early.png")
plt.show()