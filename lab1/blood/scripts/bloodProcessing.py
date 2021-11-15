import matplotlib.pyplot as plt
import numpy as np

## CALIBRATION

data40mm = np.loadtxt("blood/data/40 mmHg.txt", dtype= int)
data120mm = np.loadtxt("blood/data/120 mmHg.txt", dtype= int)
data160mm = np.loadtxt("blood/data/160 mmHg.txt", dtype= int)
data180mm = np.loadtxt("blood/data/180 mmHg.txt", dtype= int)

dataarr = [40, 120, 160, 180]

mean40 = np.mean(data40mm)
mean120 = np.mean(data120mm)
mean160 = np.mean(data160mm)
mean180 = np.mean(data180mm)

meanarr = np.array([mean40, mean120, mean160, mean180])
plf = np.polyfit(dataarr, meanarr, 1)
yfit = np.polyval(plf, dataarr)

y0 = np.polyval(plf, 0)
k = (np.polyval(plf, 160) - np.polyval(plf, 40))/(160 - 40)
leg = str(" N = {:.3f}P + {:.3f}".format(k, y0))

fig1, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(dataarr, yfit,  label = leg, lw = 2, c = 'red')
plt.ylabel("ADC counts")
plt.xlabel("Pressure, mmHg")
plt.title("Calibration graph N(P)", fontsize = 20)
ax.set_xlim(dataarr[0] - 5, dataarr[3] + 10)
ax.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig1.savefig("pressure-calibration.png")

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

figp3.savefig("rest-pulse.png") 
