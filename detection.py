#!/usr/bin/python
import csv
import matplotlib.pyplot as plt
import pylab
import numpy as np

# Turn interactive plotting off
plt.ioff()

Counts = []
Pfail = []
NormHist = []

with open('detection.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    n = 0
    for row in csv_reader:
        if n == 0:
            n += 1
        else:
            Counts.append(float(row[0]))
            Pfail.append(float(row[1]))
            NormHist.append(float(row[2]))
            n += 1

### Fluorescence Histogram ####################################

plot_min = min(Counts)
plot_max = 35
thresh = 4

fig = plt.figure(1)
ax = fig.add_subplot(111)
plt.title('Normalized Flourescence Histogram')
ax.set_xlabel('PMT Counts')
ax.set_ylabel('Normalized Count Frequency')
ax.bar(Counts, NormHist, width=1)
ax.axvline(thresh, color='k', linestyle='--')
ax.annotate('Optimal Bright/Dark Threshold', (thresh, 60), xytext=(10, 80),
            arrowprops=(dict(facecolor='k', shrink=0.05)))
pylab.xlim([plot_min, plot_max])
pylab.ylim([0, max(NormHist)+1])
plt.savefig('detection_calib.jpg')
plt.close(fig)

### RPE Failure Data ###########################################

fig = plt.figure(2)
ax = fig.add_subplot(111)
plt.title('Probability of RPE Failure with Changing State Threshold')
ax.set_xlabel('Bright/Dark State Threshold')
ax.set_ylabel('Probability of RPE Failure')
ax.scatter(Counts, Pfail, color='b', linewidth=3)
pylab.xlim([plot_min, plot_max])
pylab.ylim([-1, max(Pfail)+1])
plt.savefig('detection_data.jpg')
plt.close(fig)

# plt.show()