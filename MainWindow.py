# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget, QFileDialog, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMessageBox, QRadioButton)

from pymsfilereader import MSFileReader
import os
import matplotlib.pyplot as plt
import statistics
import numpy as np
import csv
from scipy.interpolate import make_interp_spline

flex = True  # True for flex and False for RT
profile = True # True for profile and False for Centroid
peaksInterested = []
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 663)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.openFileButton = QPushButton(self.centralwidget)
        self.openFileButton.setObjectName(u"openFileButton")
        self.openFileButton.setGeometry(QRect(10, 30, 80, 24))
        self.openFileButton.clicked.connect(MainWindow.openFile_clicked)

        self.fileNameLabel = QLabel(self.centralwidget)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(10, 70, 201, 31))
        self.analysisButton = QPushButton(self.centralwidget)
        self.analysisButton.setObjectName(u"analysisButton")
        self.analysisButton.setGeometry(QRect(130, 30, 80, 24))
        self.analysisButton.clicked.connect(MainWindow.analysis_clicked)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(230, 0, 321, 192))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(570, 90, 91, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(570, 50, 101, 21))

        self.totalImsEdit = QLineEdit(self.centralwidget)
        self.totalImsEdit.setObjectName(u"totalImsEdit")
        self.totalImsEdit.setGeometry(QRect(670, 90, 113, 24))
        self.massPerImsEdit = QLineEdit(self.centralwidget)
        self.massPerImsEdit.setObjectName(u"massPerImsEdit")
        self.massPerImsEdit.setGeometry(QRect(670, 50, 113, 24))
        self.totalMassScanNumberLabel = QLabel(self.centralwidget)
        self.totalMassScanNumberLabel.setObjectName(u"totalMassScanNumberLabel")
        self.totalMassScanNumberLabel.setGeometry(QRect(570, 15, 211, 21))
        self.arrivingPlotButton = QPushButton(self.centralwidget)
        self.arrivingPlotButton.setObjectName(u"arrivingPlotButton")
        self.arrivingPlotButton.setGeometry(QRect(410, 400, 80, 24))
        self.arrivingPlotButton.clicked.connect(MainWindow.arrivingPlot_clicked)

        self.linearRadioButton = QRadioButton(self.centralwidget)
        self.linearRadioButton.setObjectName(u"linearRadioButton")
        self.linearRadioButton.setGeometry(QRect(410, 310, 91, 22))
        self.linearRadioButton.setChecked(True)
        self.smoothRadioButton = QRadioButton(self.centralwidget)
        self.smoothRadioButton.setObjectName(u"smoothRadioButton")
        self.smoothRadioButton.setGeometry(QRect(530, 310, 91, 22))
        self.intertestedMasslistWidget = QListWidget(self.centralwidget)
        self.intertestedMasslistWidget.setObjectName(u"intertestedMasslistWidget")
        self.intertestedMasslistWidget.setGeometry(QRect(100, 310, 256, 192))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 360, 121, 16))
        self.startMassEdit = QLineEdit(self.centralwidget)
        self.startMassEdit.setObjectName(u"startMassEdit")
        self.startMassEdit.setGeometry(QRect(530, 357, 51, 24))
        self.loadInterestedMassButton = QPushButton(self.centralwidget)
        self.loadInterestedMassButton.setObjectName(u"loadInterestedMassButton")
        self.loadInterestedMassButton.setGeometry(QRect(100, 510, 80, 24))
        self.loadInterestedMassButton.clicked.connect(MainWindow.loadInterestedMass_clicked)

        self.saveInterestedMassButton = QPushButton(self.centralwidget)
        self.saveInterestedMassButton.setObjectName(u"saveInterestedMassButton")
        self.saveInterestedMassButton.setGeometry(QRect(275, 510, 80, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 876, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def loadInterestedMass_clicked(self):
        file = QFileDialog.getOpenFileName(self,
            "Open interested mass list file", "", "Text Files (*.txt)")
        fileName = file[0]
        print(fileName)
        if not fileName:
            print("cancelled")
        else:
            global peaksInterested
            peaksInterested.clear()
            with open(fileName) as f:
                peaksInterested = [float(line.strip()) for line in f]

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
            self.fileNameLabel.setText(os.path.basename(fileName))

    def analysis_clicked(self):
        if not rawFile:
            QMessageBox.warning(self, "Warning", "No raw file loaded!")
        else:
            self.listWidget.clear()
            numSpectra = rawFile.GetNumSpectra()
            self.totalMassScanNumberLabel.setText("Total mass scans: %i" %(numSpectra))
            firstValidMassScan = 1
            massTimeGap = 1000
            lastMassTime = 0
            massPerIms = 0
            massInCurrentIms = 0
            massPerImsDict = {}
            for ns in range(1, numSpectra + 1):
                thisMassTime = rawFile.RTFromScanNum(ns) * 60 * 1000
                self.listWidget.addItem("%i: %f ms"%(ns, thisMassTime))
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
            self.massPerImsEdit.setText(str(massPerIms))
            self.totalImsEdit.setText(str(numSpectra // massPerIms))

    def arrivingPlot_clicked(self):
        print("plotting arriving time")
        if not self.totalImsEdit.text() or not self.massPerImsEdit.text():
            QMessageBox.warning(self, "Warning", "Analysis raw file before plotting")
        imsScanNum = int(self.totalImsEdit.text())
        msNumInIms = int(self.massPerImsEdit.text())
        #peaksInterested = [322.0485,622.0305,922.0102,1122.0014,1221.9971] if flex else [422.7366,496.2865,586.79997,613.3166,801.4142]
        massScanRange = (100, 1100) if flex else (600, 1600)

        if not peaksInterested:
            QMessageBox.warning(self, "Warning", "No mass list available!")
        else:
            print(peaksInterested)

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
                plt.axis([max_arriving_time - 200, max_arriving_time + 200, 0, 1.2])

                if(self.smoothRadioButton.isChecked()):
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
            plt.text(max_arriving_time - 180, 1.1,r'$\mu=%.4f$'%(meanstatistics))
            plt.text(max_arriving_time - 180, 1.05,r'$RSD=%.4f$'%(rtdstatistics))
            plt.show()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.fileNameLabel.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.analysisButton.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total IMS scans:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mass scans / IMS:", None))
        self.totalMassScanNumberLabel.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.arrivingPlotButton.setText(QCoreApplication.translate("MainWindow", u"Arriving Time", None))
        self.linearRadioButton.setText(QCoreApplication.translate("MainWindow", u"Linear", None))
        self.smoothRadioButton.setText(QCoreApplication.translate("MainWindow", u"Smooth", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start from mass sacn:", None))
        self.startMassEdit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.loadInterestedMassButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.saveInterestedMassButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

