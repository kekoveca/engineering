import matplotlib.pyplot as plt
import numpy as np

d20mm = np.loadtxt("Hlam/20mm.txt", dtype= int, skiprows=4)
d40mm = np.loadtxt("Hlam/40mm.txt", dtype= int, skiprows=4)
d60mm = np.loadtxt("Hlam/60mm.txt", dtype= int, skiprows=4)
d80mm = np.loadtxt("Hlam/80mm.txt", dtype= int, skiprows=4)
d100mm = np.loadtxt("Hlam/101mm.txt", dtype= int, skiprows=4)

data = [20, 40, 60, 80, 101]

md2 = np.mean(d20mm)
md4 = np.mean(d40mm)
md6 = np.mean(d60mm)
md8 = np.mean(d80mm)
md10 = np.mean(d100mm)

meanarr = np.array([md2, md4, md6, md8, md10])
plf = np.polyfit(data, meanarr, 4)
yfit = np.polyval(plf, data)

leg = str(" N = {:.3f}p^4 + {:.3f}p^3 - {:.3f}p^2 + {:.3f}p - {:.4f}".format(plf[4], plf[3], abs(plf[2]), plf[1], abs(plf[0])))

fig1, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(data, yfit, label = leg, lw = 2, c = 'orange')
ax.scatter(data, meanarr)
#plt.ylabel("ADC counts")
#plt.xlabel("Pressure, mmHg")
#plt.title("Calibration graph N(P)", fontsize = 20)
ax.set_ylim(1000, 2100)
ax.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig1.savefig("1.png")


wave = np.loadtxt("Hlam/sliv40mm.txt", dtype= int, skiprows=4)
dataw = np.linspace(0, 30, len(wave))

plf = np.polyfit(dataw, wave, 2)
yfit = np.polyval(plf, dataw)

fig2, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(dataw, wave, lw = 2, c = 'orange')
#plt.ylabel("ADC counts")
#plt.xlabel("Pressure, mmHg")
#plt.title("Calibration graph N(P)", fontsize = 20)
ax.set_xlim(0, 7*max(dataw)/15)
#ax.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig2.savefig("40mm.png")


wave = np.loadtxt("Hlam/sliv80mm.txt", dtype= int, skiprows=4)
dataw = np.linspace(0, 30, len(wave))

plf = np.polyfit(dataw, wave, 2)
yfit = np.polyval(plf, dataw)

fig3, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(dataw, wave, lw = 2, c = 'orange')
#plt.ylabel("ADC counts")
#plt.xlabel("Pressure, mmHg")
#plt.title("Calibration graph N(P)", fontsize = 20)
ax.set_xlim(0, 7*max(dataw)/15)
#ax.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig3.savefig("80mm.png")


wave = np.loadtxt("Hlam/sliv101mm.txt", dtype= int, skiprows=4)
dataw = np.linspace(0, 30, len(wave))

plf = np.polyfit(dataw, wave, 2)
yfit = np.polyval(plf, dataw)

fig4, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(dataw, wave, lw = 2, c = 'orange')
#plt.ylabel("ADC counts")
#plt.xlabel("Pressure, mmHg")
#plt.title("Calibration graph N(P)", fontsize = 20)
ax.set_xlim(0, 7*max(dataw)/15)
#ax.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig4.savefig("101mm.png")