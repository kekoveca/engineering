import matplotlib.pyplot as plt
import numpy as np

#PRESSURE CALIBRATION
pressure0 = np.loadtxt("500 point 0pa.txt", dtype=float)
pressure = np.loadtxt("500 point 33.3pa.txt", dtype=float)

p0 = np.mean(pressure0)

p = np.mean(pressure)

pressure_polyfit = np.polyfit([p0, p], [0, 33.3], 1)
pressure_polyval = np.polyval(pressure_polyfit, [p0, p])
pressure_y0 = np.polyval(pressure_polyfit, 0)
pressure_k = 33.3 / (p - p0)

leg = str((" P = {:.3f}N - {:.3f}".format(pressure_k, abs(pressure_y0))))

#PRESSURE CALIBRATION GRAPH
fig1, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot([p0, p], pressure_polyval, label = leg, lw = 2, c = 'red')
ax.set_xlim(p0, p)
ax.set_ylim(min(pressure_polyval), max(pressure_polyval))
ax.set_xlabel("Отсчёты АЦП")
ax.set_ylabel("Давление, Па")
ax.set_title("График калибровки P(N)", fontsize = 20)
ax.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig1.savefig("graph.png")


#DISTANCE CALIBRATION (roflanFace)

k2 = 50 / 900
dist0 = -450
dist = 450


leg2 = str(("S (мм) = {:.3f}N".format(50/900)))

fig2, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot([dist0, dist], [k2 * dist0, k2 * dist], label = leg2, lw = 2, c = 'red')
ax.set_xlim(dist0, dist)
ax.set_xlabel("Расстояние в шагах JetMover")
ax.set_ylabel("Координата, мм")
ax.set_title("График калибровки S(N)", fontsize = 20)
fig2.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig2.savefig("graph2.png")



#Pressure into velocity

adc0mm = np.loadtxt("100 points 0mm.txt", dtype=int)
adc10mm = np.loadtxt("100 points 10mm.txt", dtype=int)
adc20mm = np.loadtxt("100points 20mm.txt", dtype=int)
adc30mm = np.loadtxt("100points 30mm.txt", dtype=int)
adc40mm = np.loadtxt("100points 40mm.txt", dtype=int)
adc50mm = np.loadtxt("100points 50mm.txt", dtype=int)
adc60mm = np.loadtxt("100points 60mm.txt", dtype=int)
adc70mm = np.loadtxt("100points 70mm.txt", dtype=int)

#some calculations

pres_0 = np.polyval(pressure_polyfit, adc0mm)
pres_1 = np.polyval(pressure_polyfit, adc10mm)
pres_2 = np.polyval(pressure_polyfit, adc20mm)
pres_3 = np.polyval(pressure_polyfit, adc30mm)
pres_4 = np.polyval(pressure_polyfit, adc40mm)
pres_5 = np.polyval(pressure_polyfit, adc50mm)
pres_6 = np.polyval(pressure_polyfit, adc60mm)
pres_7 = np.polyval(pressure_polyfit, adc70mm)

for i in range (len(pres_0)):
    if pres_0[i] < 0:
        pres_0[i] = 0
    if pres_1[i] < 0:
        pres_1[i] = 0
    if pres_2[i] < 0:
        pres_2[i] = 0
    if pres_3[i] < 0:
        pres_3[i] = 0
    if pres_4[i] < 0:
        pres_4[i] = 0
    if pres_5[i] < 0:
        pres_5[i] = 0
    if pres_6[i] < 0:
        pres_6[i] = 0
    if pres_7[i] < 0:
        pres_7[i] = 0

steps = []
for i in range (-50, 51):
    steps.append(i)
steps = np.array(steps)

#подсчёт скоростей

vel_0 = ((2 * pres_0) / 1.2754) ** 0.5
vel_1 = ((2 * pres_1) / 1.2754) ** 0.5
vel_2 = ((2 * pres_2) / 1.2754) ** 0.5
vel_3 = ((2 * pres_3) / 1.2754) ** 0.5
vel_4 = ((2 * pres_4) / 1.2754) ** 0.5
vel_5 = ((2 * pres_5) / 1.2754) ** 0.5
vel_6 = ((2 * pres_6) / 1.2754) ** 0.5
vel_7 = ((2 * pres_7) / 1.2754) ** 0.5

#подсчёт расхода

q_0 = (2 * 3.14 * 1.2754 * 0.05 * 9 / 900) * (steps + 6) * vel_0
q_1 = (2 * 3.14 * 1.2754 * 0.05 * 9 / 900) * (steps + 6) * vel_1
q_2 = (2 * 3.14 * 1.2754 * 0.05 * 9 / 900) * (steps + 6) * vel_2
q_3 = (2 * 3.14 * 1.2754 * 0.05 * 9 / 900) * (steps + 6) * vel_3
q_4 = (2 * 3.14 * 1.2754 * 0.05 * 9/ 900) * (steps + 6) * vel_4
q_5 = (2 * 3.14 * 1.2754 * 0.05 * 9/ 900) * (steps + 6) * vel_5
q_6 = (2 * 3.14 * 1.2754 * 0.05 * 9/ 900) * (steps + 5) * vel_6
q_7 = (2 * 3.14 * 1.2754 * 0.05 * 9/ 900) * (steps + 4) * vel_7

q_0p = q_1p = q_2p = q_3p = q_4p = q_5p = q_6p = q_7p = 0
for i  in range (len(q_0)):
    q_0p += abs(q_0[i])
    q_1p += abs(q_1[i])
    q_2p += abs(q_2[i])
    q_3p += abs(q_3[i])
    q_4p += abs(q_4[i])
    q_5p += abs(q_5[i])
    q_6p += abs(q_6[i])
    q_7p += abs(q_7[i])
q_0p /= 2
q_1p /= 2
q_2p /= 2
q_3p /= 2
q_4p /= 2
q_5p /= 2
q_6p /= 2
q_7p /= 2
q = [q_0p, q_1p, q_2p, q_3p, q_4p, q_5p, q_6p, q_7p]

#velocity graph

lb0 = str(("Q(00мм) = {:.3f}[г/см]".format(q_0p)))
lb1 = str(("Q(10мм) = {:.3f}[г/см]".format(q_1p)))
lb2 = str(("Q(20мм) = {:.3f}[г/см]".format(q_2p)))
lb3 = str(("Q(30мм) = {:.3f}[г/см]".format(q_3p)))
lb4 = str(("Q(40мм) = {:.3f}[г/см]".format(q_4p)))
lb5 = str(("Q(50мм) = {:.3f}[г/см]".format(q_5p)))
lb6 = str(("Q(60мм) = {:.3f}[г/см]".format(q_6p)))
lb7 = str(("Q(70мм) = {:.3f}[г/см]".format(q_7p)))


fig3, ax = plt.subplots(figsize=(12, 7))
ax.plot(steps+6, vel_0, color = 'red',label = lb0, lw = 1, linestyle = '-')
ax.plot(steps+6, vel_1, color = 'green',label = lb1, lw = 1, linestyle = '-')
ax.plot(steps+6, vel_2, color = 'blue',label = lb2, lw = 1, linestyle = '-')
ax.plot(steps+6, vel_3, color = 'violet',label = lb3,lw = 1, linestyle = '-')
ax.plot(steps+6, vel_4, color = 'pink',label = lb4, lw = 1, linestyle = '-')
ax.plot(steps+6, vel_5, color = 'yellow',label = lb5, lw = 1, linestyle = '-')
ax.plot(steps+5, vel_6, color = 'orange',label = lb6, lw = 1, linestyle = '-')
ax.plot(steps+4, vel_7, color = 'black',label = lb7, lw = 1, linestyle = '-')
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.legend()
ax.set_ylabel("Скорость, м/с")
ax.set_xlabel("Координата на оси двигателя, мм")
ax.set_title("График скоростей")
plt.minorticks_on()
fig3.savefig("graph3.png")


s = [0, 10, 20, 30, 40, 50, 60, 70]
k8 = np.polyfit(s, q, 1)
b8 = np.polyval(k8, s)
lb8 = str(("Q = {:.3f}x + {:.3f}".format(k8[0], abs(k8[1]))))
fig4, ax = plt.subplots(figsize=(12, 7))
ax.plot(s, q, color = 'red', lw = 1, linestyle = '--')
ax.plot(s, b8, color = 'blue',label = lb8, lw = 1,  linestyle = '-')
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.legend()
ax.set_xlim(0, 75)
ax.set_ylabel("Расход струи, г/с")
ax.set_xlabel("Расстояние до сопла, мм")
ax.set_title("График зависимости расхода от расстояния до сопла")
plt.minorticks_on()
fig4.savefig("graph4.png")