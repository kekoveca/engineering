import matplotlib.pyplot as plt
import numpy as np

## CALIBRATION

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
ax.plot(data, yfit,  label = leg, lw = 2, c = 'red')
plt.ylabel("ADC counts")
plt.xlabel("Pressure, mmHg")
plt.title("Calibration graph N(P)", fontsize = 20)
ax.set_ylim(2000, 3000)
ax.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig1.savefig("1.png")

'''
## FITNESS 

dataRawFitness = np.loadtxt("blood/data/fitness.txt", dtype= int)
dataFit = dataRawFitness/k - y0/k
time = np.linspace(0, 60, len(dataFit))
tstep = len(time)/60
leg1 = str("Pressure = {}/{}".format(147,97))

fig2, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(time, dataFit, lw = 1, c = 'brown', marker = 'o', markevery = [6*tstep, 41.7*tstep], label = leg1,
markersize = 15, markerfacecolor = 'red', markeredgecolor = 'red')
ax.legend()
plt.ylabel("Pressure, mmHg")
plt.xlabel("Time, seconds")
plt.title("Blood pressure after fitness", fontsize = 25)
ax.text(0.12, 0.75, 'Systole', fontsize = 20, transform=ax.transAxes)
ax.text(0.82, 0.2, 'Diastole', fontsize = 20, transform=ax.transAxes)
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()

fig2.savefig("fintess-pressure.png")

##FITNESS PULSE

pplf = np.polyfit(time, dataFit, 2)
pyfit = np.polyval(pplf, time)
deltadata1 = pyfit - dataFit
legp1 = str("The pulse is {:.0f} ".format(60*(16)/(28-18)))

figp2, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(time, deltadata1, lw = 0.5, c = 'orange', label = legp1)
ax.legend()
plt.ylabel("Changes of the blood pressure, mmHg")
plt.xlabel("Time, seconds")
plt.title("Pulse after fitness", fontsize = 25)
ax.set_xlim(17, 30)
ax.set_ylim(-3, 5)
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()

figp2.savefig("fitness-pulse.png") 

## CALM

dataRawCalm = np.loadtxt("blood/data/rest.txt", dtype= int)
dataCalm = dataRawCalm/k - y0/k
time = np.linspace(0, 60, len(dataCalm))
leg2 = str("Pressure = {}/{}".format(137,96))

fig3, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(time, dataCalm, lw = 1, c = 'brown', marker = 'o', markevery = [10.8*tstep, 37.5*tstep], label = leg2,
markersize = 15, markerfacecolor = 'red', markeredgecolor = 'red')
ax.legend()
plt.ylabel("Pressure, mmHg")
plt.xlabel("Time, seconds")
plt.title("Blood pressure before fitness", fontsize = 25)
ax.text(0.18, 0.68, 'Systole', fontsize = 20, transform=ax.transAxes)
ax.text(0.79, 0.14, 'Diastole', fontsize = 20, transform=ax.transAxes)
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()

fig3.savefig("rest-pressure.png")

##CALM PULSE

cplf = np.polyfit(time, dataCalm, 2)
cyfit = np.polyval(cplf, time)
deltadata2 = cyfit - dataCalm
legp2 = str("The pulse is {:.0f} ".format(60*(12)/(28-18)))

figp3, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(time, deltadata2, lw = 0.5, c = 'orange', label = legp2)
ax.legend()
plt.ylabel("Changes of the blood pressure, mmHg")
plt.xlabel("Time, seconds")
plt.title("Pulse before fitness", fontsize = 25)
ax.set_xlim(17, 30)
ax.set_ylim(-2, 1.5)
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()

figp3.savefig("rest-pulse.png") '''
