import sys
from PySide6 import QtWidgets

from MainWindow import Ui_MainWindow

from typing import Tuple, Any

import matplotlib.pyplot as plt
from pymsfilereader import MSFileReader
import statistics
import numpy as np
import csv


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
"""

flex = False  # True for flex and False for RT
profile = True # True for profile and False for Centroid

def getMass(peaklist, target, ignore:bool):
    if ignore:
        return 0

    if profile:
        length = len(peaklist[0])
        leftx = -1
        lefty = -1
        rightx = -1
        righty = -1
        for i in range(length):
            if float(peaklist[0][i]) == target:
                return peaklist[1][i]
            if float(peaklist[0][i]) < target:
                leftx = peaklist[0][i]
                lefty = peaklist[1][i]
            if float(peaklist[0][i]) > target:
                rightx = peaklist[0][i]
                righty = peaklist[1][i]
                if (lefty > 0) and (target - leftx < 1) and (rightx - target < 1):
                    #print(peaklist)
                    return righty - (righty - lefty) * (rightx - target) / (rightx - leftx)
                else:
                    return 0
    else:
        length = len(peaklist[0])
        for i in range(length):
            if abs(float(peaklist[0][i]) - target) < 0.5:
                return peaklist[1][i]

    return 0


rawfile = MSFileReader("rawfiles/flex.raw") if flex else MSFileReader("rawfiles/rt.raw")
numSpectra = rawfile.GetNumSpectra()
print("Total mass scans: ", rawfile.GetNumSpectra())
#for ns in range(1, 220):
#    print(ns, " start time: ", rawfile.RTFromScanNum(ns) * 60 * 1000)

peaksInterested = [322.0485,622.0305,922.0102,1122.0014,1221.9971] if flex else [422.7366,496.2865,586.79997,613.3166,801.4142]
massScanRange = (100, 1100) if flex else (600, 1600)
msNumInIms = 100
imsScanNum = int(numSpectra / msNumInIms)
print("Each IMS scan has %s mass scans"%(msNumInIms))
print("-------------------------------------")

for target in peaksInterested:
    arrvingTimes = []
    legends = []
    print("Arriving time of %s m/z"%(target))
    print("IMS\tMass\tarriving time\t\tintensity")
    plt.figure(figsize=(4, 6))
    max_arriving_time = 0
    csvTitle = []
    curveData = []
    for imsScan in range(1, imsScanNum):
        scanStart = (imsScan - 1) * msNumInIms + 1
        if not (scanStart >= massScanRange[0] and scanStart <= massScanRange[1] - msNumInIms):
            continue
        csvTitle.append("X-%i"%imsScan)
        csvTitle.append("Y-%i"%imsScan)
        legends.append(imsScan)
        x = []
        y = []
        xpeak = 0
        ypeak = 0
        for sn in range((imsScan - 1) * msNumInIms + 1, imsScan * msNumInIms):
            x.append(rawfile.RTFromScanNum(sn) * 60 * 1000 - rawfile.RTFromScanNum((imsScan - 1) * msNumInIms + 1) * 60 * 1000)
            masslist = rawfile.GetMassListFromScanNum(sn) if profile else rawfile.GetMassListFromScanNum(sn,"",0,0,0,True)
            y.append(getMass(masslist[0], target, False))
        plt.xlabel("Arriving time (ms)")
        plt.ylabel("Intensity")

        max_arriving_intensity = max(y)
        max_arriving_index = y.index(max_arriving_intensity)
        print(imsScan,"\t",max_arriving_index,"\t",x[max_arriving_index],"\t",max_arriving_intensity)
        max_arriving_time = x[max_arriving_index]
        arrvingTimes.append(max_arriving_time)

        curveData.append(x)
        curveData.append(y)

        y = [yy / max_arriving_intensity for yy in y] # normalization
        plt.axis([max_arriving_time - 200, max_arriving_time + 200, 0, 1.2])
        plt.plot(x, y)

    csvData = np.array(curveData).transpose().tolist()
    with open('curves/%s.csv'%target, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csvTitle)
        writer.writerows(csvData)

    meanstatistics = statistics.mean(arrvingTimes)
    stdstatistics = statistics.stdev(arrvingTimes)
    rtdstatistics = 100 * stdstatistics / meanstatistics
    print("Mean arriving time is %s ms"%(meanstatistics))
    print("Standard Deviation of arrving time is % s "%(stdstatistics))
    print("Relative Standard Deviation of arriving time is % s"%(rtdstatistics))
    plt.title("Arriving time" + " of " + str(target) + " m/z")
    print("-------------------------------------")
    plt.legend(legends, loc='upper right')
    plt.text(max_arriving_time - 180, 1.1,r'$\mu=%.4f$'%(meanstatistics))
    plt.text(max_arriving_time - 180, 1.05,r'$RSD=%.4f$'%(rtdstatistics))
    plt.show()
"""
