import matplotlib.pyplot as plt
import numpy as np

d20mm = np.loadtxt("wave-starter-kit/data example/20 mm.txt", dtype= int, skiprows=4)
d40mm = np.loadtxt("wave-starter-kit/data example/40 mm.txt", dtype= int, skiprows=4)
d60mm = np.loadtxt("wave-starter-kit/data example/60 mm.txt", dtype= int, skiprows=4)
d80mm = np.loadtxt("wave-starter-kit/data example/80 mm.txt", dtype= int, skiprows=4)
d100mm = np.loadtxt("wave-starter-kit/data example/100 mm.txt", dtype= int, skiprows=4)
d120mm = np.loadtxt("wave-starter-kit/data example/120 mm.txt", dtype= int, skiprows=4)

data = [20, 40, 60, 80, 100, 120]

md2 = np.mean(d20mm)
md4 = np.mean(d40mm)
md6 = np.mean(d60mm)
md8 = np.mean(d80mm)
md10 = np.mean(d100mm)
md12 = np.mean(d120mm)

meanarr = np.array([md2, md4, md6, md8, md10, md12])
plf = np.polyfit(data, meanarr, 4)
yfit = np.polyval(plf, data)

leg = str(" N = {:.3f}P + {:.3f}".format(plf[1], plf[0]))

fig1, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(data, yfit,  label = leg, lw = 2, c = 'orange')
ax.scatter(data, meanarr)
#plt.ylabel("ADC counts")
#plt.xlabel("Pressure, mmHg")
#plt.title("Calibration graph N(P)", fontsize = 20)
ax.set_ylim(2000, 3000)
#ax.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig1.savefig("1.png")

wave = np.loadtxt("wave-starter-kit/data example/wave.txt", dtype= int, skiprows=4)
dataw = np.linspace(0, 30, len(wave))

plf1 = np.polyfit(dataw, wave, 2)
yfit1 = np.polyval(plf1, dataw)

fig2, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(dataw, wave,lw = 2, c = 'orange')
#plt.ylabel("ADC counts")
#plt.xlabel("Pressure, mmHg")
#plt.title("Calibration graph N(P)", fontsize = 20)
ax.set_xlim(0, 1.5*dataw)
#ax.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig2.savefig("2.png")