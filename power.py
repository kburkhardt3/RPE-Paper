#!/usr/bin/python
import csv
import matplotlib.pyplot as plt
import numpy as np

# Turn interactive plotting off
plt.ioff()

Power = []
Data = []
ErrNeg = []
ErrPos = []

with open('power_calibration.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    n = 0
    for row in csv_reader:
        if n == 0:
            n += 1
        else:
            Power.append(float(row[0]))
            Data.append(float(row[19]))
            ErrNeg.append(float(row[20]))
            ErrPos.append(float(row[21]))
            n += 1

### Power Calibration #############################################

fig = plt.figure(1)
ax = fig.add_subplot(111)
plt.title('Depolarizing Power Calibration')
ax.set_xlabel('369 nm AOM Drive Power (dB)')
ax.set_ylabel(r'Qubit Fidelity After 16 Repeated $\Pi$ Gates')
ax.plot(Power, Data)
plt.savefig('power_calib.jpg')
plt.close(fig)

# plt.show()