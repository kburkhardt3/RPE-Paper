#!/usr/bin/python
import csv
import matplotlib.pyplot as plt
import pylab
import numpy as np

# Turn interactive plotting off
plt.ioff()

LogTprep = []
Infidelity = []
ErrNeg = []
ErrPos = []

Data_Tprep = [400, 447, 501, 562, 631, 708, 794, 891, 1000] # ns
Data_Tprep_label = []
Data_REPreps = [8, 16, 32, 64, 128]
TimeMatrix = np.array([[0.025, 0.050, 0.025, 0.075, 0.175, 0.275, 0.325, 0.625, 0.675],
                       [0.100, 0.200, 0.275, 0.300, 0.300, 0.475, 0.725, 0.850, 0.925],
                       [0.200, 0.300, 0.525, 0.575, 0.675, 0.825, 1.000, 1.000, 1.000],
                       [0.275, 0.400, 0.675, 0.825, 0.900, 1.000, 1.000, 1.000, 1.000],
                       [0.275, 0.475, 0.800, 0.900, 1.000, 1.000, 1.000, 1.000, 1.000]])

with open('time_calibration.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    n = 0
    for row in csv_reader:
        if n == 0:
            n += 1
        else:
            LogTprep.append(float(row[1]))
            Infidelity.append(float(row[6]))
            ErrNeg.append(float(row[7]))
            ErrPos.append(float(row[8]))
            n += 1

Tprep = np.power(10,np.asarray(LogTprep))

### Calibration Plot #############################################

plot_min = 0.1 # cropping parameters
plot_max = 3

fig = plt.figure(1)
ax = fig.add_subplot(111)
plt.title('SPAM Error as a Function of Qubit Preparation Time')
ax.set_xlabel(r'Qubit Preparation Time ($\mu$s)')
ax.set_ylabel('SPAM Error')
ax.axvline(min(Data_Tprep)/1000, color='k', linestyle='--')
ax.axvline(max(Data_Tprep)/1000, color='k', linestyle='--')
ax.axhline(1/np.sqrt(8), color='r', linestyle='-')
ax.semilogx(Tprep, Infidelity, color="b")
ax.annotate(r'1/$\sqrt{8}$', (2*plot_min, 1/np.sqrt(8)), xytext=(0.15,0.15),
            arrowprops=(dict(facecolor='k', shrink=0.05)))
pylab.xlim([plot_min, plot_max])
plt.savefig('time_calib.jpg')
plt.close(fig)

### Data Matrix #################################################

Data_Tprep_label = [str(i)+' ns' for i in Data_Tprep]

fig, ax = plt.subplots()
im = ax.matshow(TimeMatrix, cmap='GnBu') # imshow for smoothing

ax.set_xticks(np.arange(len(Data_Tprep)))
ax.set_yticks(np.arange(len(Data_REPreps)))
ax.set_xticklabels(Data_Tprep_label)
ax.set_yticklabels(Data_REPreps)

ax.xaxis.set_ticks_position('bottom')
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
         
for i in range(len(Data_REPreps)):
    for j in range(len(Data_Tprep)):
        text = ax.text(j, i, TimeMatrix[i, j],
                       ha="center", va="center", color="k")

ax.set_title("RPE Success as a Function of Qubit Preparation Time")
plt.savefig('time_data.jpg')
plt.close(fig)

# plt.show()