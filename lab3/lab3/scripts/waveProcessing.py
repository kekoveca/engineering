import matplotlib.pyplot as plt
import numpy as np
import math

d20mm = np.loadtxt("20mm.txt", dtype= int, skiprows=4)
d40mm = np.loadtxt("40mm.txt", dtype= int, skiprows=4)
d60mm = np.loadtxt("60mm.txt", dtype= int, skiprows=4)
d80mm = np.loadtxt("80mm.txt", dtype= int, skiprows=4)

data = [20, 40, 60, 80]

md2 = np.mean(d20mm)
md4 = np.mean(d40mm)
md6 = np.mean(d60mm)
md8 = np.mean(d80mm)
adc = np.linspace(md2, md8, int(md8 - md2))
meanarr = np.array([md2, md4, md6, md8])
plf = np.polyfit(meanarr, data, 3)
yfit = np.polyval(plf, adc)


leg = str(" H = {:.8f}n^3 - {:.4f}n^2 + {:.3f}n - {:.3f}".format(plf[0], abs(plf[1]), plf[2], abs(plf[3])))
fig1, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(adc, yfit, label = leg, lw = 2, c = 'orange')
ax.scatter(meanarr, data)
plt.ylabel("Уровнь воды, мм", fontsize = 14)
plt.xlabel("Значения АЦП", fontsize = 14)
plt.title("График калибровки H(N)", fontsize = 20)
ax.legend(fontsize = 12)
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig1.savefig("1.png")


wave40 = np.loadtxt("sliv40mm.txt", dtype= int, skiprows=4)

t40 = np.linspace(0, 15, len(wave40))
sliv40 = np.polyval(plf, wave40)

tt40_1 = np.array([])
i = 0
while t40[i] <= 2:
    tt40_1 = np.append(tt40_1, t40[i])
    i += 1
wave40line = np.array([])
for i in range(len(tt40_1)):
    wave40line = np.append(wave40line, sliv40[i])
plf40line = np.polyfit(tt40_1, wave40line, 1)
sliv40line = np.polyval(plf40line, t40)

tt40_2 = np.array([])
i = 0
while t40[i] < 2.5:
    i+=1
j = i
while t40[i] <= 4:
    tt40_2 = np.append(tt40_2, t40[i])
    i += 1
wave40line_1 = np.array([])
for i in range(j, j + len(tt40_2)):
    wave40line_1 = np.append(wave40line_1, sliv40[i])
plf40line_1 = np.polyfit(tt40_2, wave40line_1, 1)
sliv40line_1 = np.polyval(plf40line_1, t40)

t_drop40 = (plf40line_1[1] - plf40line[1])/(plf40line[0] - plf40line_1[0])
v40 = 1.5 / t_drop40
leg1 = str(" V = {:.2f} [м/с]".format(v40))
fig2, ax = plt.subplots(figsize = (16, 10), dpi = 400)
#ax.scatter(t_drop40, plf40line[0]*t_drop40 + plf40line[1], zorder = 4)
ax.plot(t40, sliv40, lw = 2, c = 'orange')
ax.plot(t40, sliv40line, lw = 1, c = 'red', linestyle = '--')
ax.plot(t40, sliv40line_1, lw = 1, c = 'purple', linestyle = '--')
plt.axvline(x = t_drop40, ymin = 0, ymax=40, color= 'blue', linestyle = '--')
plt.ylabel("Уровень воды, мм", fontsize = 14)
plt.xlabel("Время, с", fontsize = 14)
plt.title("H(t)", fontsize = 20)
ax.set_xlim(0, 4)
ax.set_ylim(0, 40)
ax.text(3, 36, leg1,bbox = {'boxstyle':'round'} ,fontsize = 16)
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig2.savefig("40mm.png")



wave80 = np.loadtxt("sliv80mm.txt", dtype= int, skiprows=4)

t80 = np.linspace(0, 15, len(wave80))

sliv80 = np.polyval(plf, wave80)

tt80_1 = np.array([])
i = 0
while t80[i] <= 1.4:
    tt80_1 = np.append(tt80_1, t80[i])
    i += 1
wave80line_1 = np.array([])
for i in range(len(tt80_1)):
    wave80line_1 = np.append(wave80line_1, sliv80[i])
plf80line_1 = np.polyfit(tt80_1, wave80line_1, 1)
sliv80line_1 = np.polyval(plf80line_1, t80)

tt80_2 = np.array([])
i = 0
while t80[i] < 1.5:
    i+=1
j = i
while t80[i] <= 3:
    tt80_2 = np.append(tt80_2, t80[i])
    i += 1
wave80line_2 = np.array([])
for i in range(j, j + len(tt80_2)):
    wave80line_2 = np.append(wave80line_2, sliv80[i])
plf80line_2 = np.polyfit(tt80_2, wave80line_2, 1)
sliv80line_2 = np.polyval(plf80line_2, t80)

t_drop80 = (plf80line_2[1] - plf80line_1[1])/(plf80line_1[0] - plf80line_2[0])
v80 = 1.5 / t_drop80
leg2 = str(" V = {:.2f} [м/с]".format(v80))

fig2, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(t80, sliv80, lw = 2, c = 'orange')
ax.plot(t80, sliv80line_1, lw = 1, c = 'red', linestyle = '--')
ax.plot(t80, sliv80line_2, lw = 1, c = 'purple', linestyle = '--')
plt.axvline(x = t_drop80, ymin = 0, ymax=80, color= 'blue', linestyle = '--')
plt.ylabel("Уровень воды, мм", fontsize = 14)
plt.xlabel("Время, с", fontsize = 14)
plt.title("H(t)", fontsize = 20)
ax.set_xlim(0, 3)
ax.set_ylim(0, 80)
ax.text(2.5, 70, leg2,bbox = {'boxstyle':'round'} ,fontsize = 20)
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig2.savefig("80mm.png")

wave101 = np.loadtxt("sliv101mm.txt", dtype= int, skiprows=4)

t101 = np.linspace(0, 15, len(wave101))

sliv101 = np.polyval(plf, wave101)

tt101_1 = np.array([])
i = 0
while t101[i] <= 1:
    tt101_1 = np.append(tt101_1, t101[i])
    i += 1
wave101line_1 = np.array([])
for i in range(len(tt101_1)):
    wave101line_1 = np.append(wave101line_1, sliv101[i])
plf101line_1 = np.polyfit(tt101_1, wave101line_1, 1)
sliv101line_1 = np.polyval(plf101line_1, t101)

tt101_2 = np.array([])
i = 0
while t101[i] < 1.2:
    i+=1
j = i
while t101[i] <= 3:
    tt101_2 = np.append(tt101_2, t101[i])
    i += 1
wave101line_2 = np.array([])
for i in range(j, j + len(tt101_2)):
    wave101line_2 = np.append(wave101line_2, sliv101[i])
plf101line_2 = np.polyfit(tt101_2, wave101line_2, 1)
sliv101line_2 = np.polyval(plf101line_2, t101)

t_drop101 = (plf101line_2[1] - plf101line_1[1])/(plf101line_1[0] - plf101line_2[0])
v101 = 1.5 / t_drop101
leg3 = str(" V = {:.2f} [м/с]".format(v101))

fig2, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(t101, sliv101, lw = 2, c = 'orange')
ax.plot(t101, sliv101line_1, lw = 1, c = 'red', linestyle = '--')
ax.plot(t101, sliv101line_2, lw = 1, c = 'purple', linestyle = '--')
plt.axvline(x = t_drop101, ymin = 0, ymax=100, color= 'blue', linestyle = '--')
plt.ylabel("Уровень воды, мм", fontsize = 14)
plt.xlabel("Время, с", fontsize = 14)
plt.title("H(t)", fontsize = 20)
ax.set_xlim(0, 3)
ax.set_ylim(0, 100)
ax.text(2.5, 85, leg3,bbox = {'boxstyle':'round'} ,fontsize = 20)
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig2.savefig("101mm.png")

log = [math.log(v40), math.log(v80), math.log(v101)]
h = [0.5*math.log(9.8*0.04), 0.5*math.log(9.8*0.08), 0.5*math.log(9.8*0.101)]

fig3, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(h, log, lw = 2, c = 'orange')
ax.scatter(h, log)
#ax.plot(t101, sliv101line_1, lw = 1, c = 'red', linestyle = '--')
#ax.plot(t101, sliv101line_2, lw = 1, c = 'purple', linestyle = '--')
#plt.axvline(x = t_drop101, ymin = 0, ymax=100, color= 'blue', linestyle = '--')
plt.ylabel("Log(v)", fontsize = 14)
plt.xlabel("0.5*Log(gh)", fontsize = 14)
plt.title("log", fontsize = 20)
#ax.set_xlim(0, 3)
#ax.set_ylim(0, 100)
#ax.text(2.5, 85, leg3,bbox = {'boxstyle':'round'} ,fontsize = 20)
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig3.savefig("log.png")