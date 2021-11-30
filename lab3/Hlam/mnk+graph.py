import matplotlib.pyplot as plt
import numpy

a = numpy.loadtxt('C:\\Users\\Askar\\PycharmProjects\\pythonProject\\i.txt', dtype=float)
b = numpy.loadtxt('C:\\Users\\Askar\\PycharmProjects\\pythonProject\\r.txt', dtype=float)

x = 0
y = 0
xy = 0
x2 = 0

for i in range (len(a)):
    x += a[i]
    y += b[i]
    xy += a[i] * b[i]
    x2 += a[i] ** 2
n = len(a)
k = (n * xy - x * y) / (n * x2 - x ** 2)
d = (y - k * x) / n

a1 = 0
a2 = max(a)
b1 = k * a1 + d
b2 = k * a2 + d

print(k, d, sep='\n')

ax = plt.subplot()
ax.plot((a1, a2), (b1, b2))


plt.grid(True)
plt.title("")
plt.xlabel("")
plt.ylabel("")
plt.xlim(0, max(a) * 1.1)
plt.ylim(0, max(b) * 1.1)
plt.scatter(a, b)
plt.savefig('C:\\Users\\Askar\\PycharmProjects\\pythonProject\\graph.png')
plt.show()
