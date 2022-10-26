# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtWidgets import (QMainWindow, QFileDialog, QMessageBox)
from MainWindow_UI import Ui_MainWindow
from pymsfilereader import MSFileReader
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import csv
import statistics


flex = True  # True for flex and False for RT
profile = True # True for profile and False for Centroid
rawFile = None

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.openFileButton.clicked.connect(self.openFile_clicked)
        self.ui.analysisButton.clicked.connect(self.analysis_clicked)
        self.ui.arrivingPlotButton.clicked.connect(self.arrivingPlot_clicked)
        self.ui.loadInterestedMassButton.clicked.connect(self.loadInterestedMass_clicked)
        self.ui.saveInterestedMassButton.clicked.connect(self.saveInterestedMass_clicked)

    def saveInterestedMass_clicked(self):
        file = QFileDialog.getSaveFileName(self,
            "Save interested mass list file", "", "Text Files (*.txt)")
        fileName = file[0]
        print(fileName)
        if fileName:
            with open(fileName, "w") as f:
                f.write(self.ui.interestedMassTextEdit.toPlainText())

    def loadInterestedMass_clicked(self):
        file = QFileDialog.getOpenFileName(self,
            "Open interested mass list file", "", "Text Files (*.txt)")
        fileName = file[0]
        print(fileName)
        if not fileName:
            print("cancelled")
        else:
            with open(fileName, "r") as f:
                self.ui.interestedMassTextEdit.setPlainText(f.read())

    def openFile_clicked(self):
        file = QFileDialog.getOpenFileName(self,
            "Open Thermo file", "", "RAW Files (*.raw)")
        fileName = file[0]
        print(fileName)
        if not fileName:
            print("cancelled")
        else:
            global rawFile
            rawFile = MSFileReader(fileName)
            self.ui.fileNameLabel.setText(os.path.basename(fileName))

    def analysis_clicked(self):
        if not rawFile:
            QMessageBox.warning(self, "Warning", "No raw file loaded!")
        else:
            self.ui.listWidget.clear()
            numSpectra = rawFile.GetNumSpectra()
            self.ui.totalMassScanNumberLabel.setText("Total mass scans: %i" %(numSpectra))
            firstValidMassScan = 1
            massTimeGap = 1000
            lastMassTime = 0
            massPerIms = 0
            massInCurrentIms = 0
            massPerImsDict = {}
            for ns in range(1, numSpectra + 1):
                thisMassTime = rawFile.RTFromScanNum(ns) * 60 * 1000
                self.ui.listWidget.addItem("%i: %f ms"%(ns, thisMassTime))
                if ns == firstValidMassScan:
                    lastMassTime = thisMassTime
                    massInCurrentIms = massInCurrentIms + 1
                    continue
                else:
                    if thisMassTime - lastMassTime > 2.5 * massTimeGap:
                        massPerIms = massInCurrentIms
                        massInCurrentIms = 1
                        lastMassTime = thisMassTime
                        firstValidMassScan = ns
                        if massPerIms in massPerImsDict:
                            massPerImsDict[massPerIms] = massPerImsDict[massPerIms] + 1
                        else:
                            massPerImsDict[massPerIms] = 1
                    else:
                        massTimeGap = thisMassTime - lastMassTime
                        massInCurrentIms = massInCurrentIms + 1
                        lastMassTime = thisMassTime
            print(sorted(massPerImsDict.items(), key=lambda item: item[1]))
            massPerIms = sorted(massPerImsDict.items(), key=lambda item: item[1])[-1][0]
            self.ui.massPerImsEdit.setText(str(massPerIms))
            self.ui.totalImsEdit.setText(str(numSpectra // massPerIms))

    def arrivingPlot_clicked(self):

        print("plotting arriving time")
        if not self.ui.totalImsEdit.text() or not self.ui.massPerImsEdit.text():
            QMessageBox.warning(self, "Warning", "Analysis raw file before plotting")
            return

        if self.ui.customeRangeRadioButton.isChecked() and ( not self.ui.fromRangeLineEdit.text() or not self.ui.toRangeLineEdit.text()):
            QMessageBox.warning(self, "Warning", "Custome ranage is not available")
            return

        imsScanNum = int(self.ui.totalImsEdit.text())
        msNumInIms = int(self.ui.massPerImsEdit.text())
        #massScanRange = (100, 1100) if flex else (600, 1600)

        peaksInterestedPlainText = self.ui.interestedMassTextEdit.toPlainText()
        peaksInterested = [float(line.strip()) for line in peaksInterestedPlainText.split()]

        if not peaksInterested:
            QMessageBox.warning(self, "Warning", "No mass list available!")
            return

        if not self.ui.mzPlotRangeLineEdit.text():
            QMessageBox.warning(self, "Warning", "No mz plot range available!")
            return
        mzPlotRange = int(self.ui.mzPlotRangeLineEdit.text().strip())

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
                if self.ui.customeRangeRadioButton.isChecked():
                    if not (scanStart >= int(self.ui.fromRangeLineEdit.text().strip()) and scanStart <= int(self.ui.toRangeLineEdit.text().strip()) - msNumInIms):
                        continue
                csvTitle.append("X-%i"%imsScan)
                csvTitle.append("Y-%i"%imsScan)
                legends.append(imsScan)
                x = []
                y = []
                xpeak = 0
                ypeak = 0
                for sn in range((imsScan - 1) * msNumInIms + 1, imsScan * msNumInIms):
                    x.append(rawFile.RTFromScanNum(sn) * 60 * 1000 - rawFile.RTFromScanNum((imsScan - 1) * msNumInIms + 1) * 60 * 1000)
                    masslist = rawFile.GetMassListFromScanNum(sn) if profile else rawFile.GetMassListFromScanNum(sn,"",0,0,0,True)
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
                plt.axis([max_arriving_time - mzPlotRange, max_arriving_time + mzPlotRange, 0, 1.2])

                if(self.ui.smoothRadioButton.isChecked()):
                    X_Y_Spline = make_interp_spline(x, y)
                    X_ = np.linspace(x[0], x[-1], 500)
                    Y_ = X_Y_Spline(X_)

                    max_arriving_intensity_Y = max(Y_)
                    Y_ = [YY / max_arriving_intensity_Y for YY in Y_] # normalization

                    plt.plot(X_, Y_)
                else:
                    plt.plot(x, y)


            csvData = np.array(curveData).transpose().tolist()
            with open('%s.csv'%target, 'w', newline='') as file:
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
            plt.text(max_arriving_time - mzPlotRange * 0.9, 1.1,r'$\mu=%.4f$'%(meanstatistics))
            plt.text(max_arriving_time - mzPlotRange * 0.9, 1.05,r'$RSD=%.4f$'%(rtdstatistics))
            plt.show()
