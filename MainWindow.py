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
    QPalette, QPixmap, QRadialGradient, QTransform, QIntValidator)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget, QFileDialog, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMessageBox, QRadioButton, QPlainTextEdit, QGroupBox, QHBoxLayout)

from pymsfilereader import MSFileReader
import os
import matplotlib.pyplot as plt
import statistics
import numpy as np
import csv
from scipy.interpolate import make_interp_spline

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 603)
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
        self.listWidget.setGeometry(QRect(230, 30, 321, 192))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(570, 90, 91, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(570, 50, 101, 21))

        self.totalImsEdit = QLineEdit(self.centralwidget)
        self.totalImsEdit.setObjectName(u"totalImsEdit")
        self.totalImsEdit.setGeometry(QRect(670, 90, 113, 24))
        self.totalImsEdit.setValidator(QIntValidator())

        self.massPerImsEdit = QLineEdit(self.centralwidget)
        self.massPerImsEdit.setObjectName(u"massPerImsEdit")
        self.massPerImsEdit.setGeometry(QRect(670, 50, 113, 24))
        self.massPerImsEdit.setValidator(QIntValidator())

        self.totalMassScanNumberLabel = QLabel(self.centralwidget)
        self.totalMassScanNumberLabel.setObjectName(u"totalMassScanNumberLabel")
        self.totalMassScanNumberLabel.setGeometry(QRect(570, 15, 211, 21))
        self.arrivingPlotButton = QPushButton(self.centralwidget)
        self.arrivingPlotButton.setObjectName(u"arrivingPlotButton")
        self.arrivingPlotButton.setGeometry(QRect(410, 520, 80, 24))
        self.arrivingPlotButton.clicked.connect(MainWindow.arrivingPlot_clicked)

        self.loadInterestedMassButton = QPushButton(self.centralwidget)
        self.loadInterestedMassButton.setObjectName(u"loadInterestedMassButton")
        self.loadInterestedMassButton.setGeometry(QRect(100, 520, 80, 24))
        self.loadInterestedMassButton.clicked.connect(MainWindow.loadInterestedMass_clicked)

        self.saveInterestedMassButton = QPushButton(self.centralwidget)
        self.saveInterestedMassButton.setObjectName(u"saveInterestedMassButton")
        self.saveInterestedMassButton.setGeometry(QRect(275, 520, 80, 24))
        self.saveInterestedMassButton.clicked.connect(MainWindow.saveInterestedMass_clicked)

        self.saveInterestedMassButton = QPushButton(self.centralwidget)
        self.saveInterestedMassButton.setObjectName(u"saveInterestedMassButton")
        self.saveInterestedMassButton.setGeometry(QRect(275, 520, 80, 24))
        self.interestedMassTextEdit = QPlainTextEdit(self.centralwidget)
        self.interestedMassTextEdit.setObjectName(u"interestedMassTextEdit")
        self.interestedMassTextEdit.setGeometry(QRect(100, 340, 251, 171))

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(500, 382, 31, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(610, 382, 21, 16))
        self.fromRangeLineEdit = QLineEdit(self.centralwidget)
        self.fromRangeLineEdit.setObjectName(u"fromRangeLineEdit")
        self.fromRangeLineEdit.setGeometry(QRect(532, 380, 71, 24))
        self.fromRangeLineEdit.setValidator((QIntValidator()))

        self.toRangeLineEdit = QLineEdit(self.centralwidget)
        self.toRangeLineEdit.setObjectName(u"toRangeLineEdit")
        self.toRangeLineEdit.setGeometry(QRect(630, 380, 71, 24))
        self.toRangeLineEdit.setValidator((QIntValidator()))

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(412, 390, 81, 16))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 310, 121, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(230, 10, 161, 16))

        self.massRangeGroupBox = QGroupBox(self.centralwidget)
        self.massRangeGroupBox.setObjectName(u"massRangeGroupBox")
        self.massRangeGroupBox.setGeometry(QRect(400, 310, 220, 65))
        self.horizontalLayout = QHBoxLayout(self.massRangeGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fullRangeRadioButton = QRadioButton(self.massRangeGroupBox)
        self.fullRangeRadioButton.setObjectName(u"fullRangeRadioButton")
        self.fullRangeRadioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.fullRangeRadioButton)

        self.customeRangeRadioButton = QRadioButton(self.massRangeGroupBox)
        self.customeRangeRadioButton.setObjectName(u"customeRangeRadioButton")

        self.horizontalLayout.addWidget(self.customeRangeRadioButton)

        self.plotSettingGroupBox = QGroupBox(self.centralwidget)
        self.plotSettingGroupBox.setObjectName(u"plotSettingGroupBox")
        self.plotSettingGroupBox.setGeometry(QRect(400, 430, 154, 65))
        self.horizontalLayout_2 = QHBoxLayout(self.plotSettingGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.linearRadioButton = QRadioButton(self.plotSettingGroupBox)
        self.linearRadioButton.setObjectName(u"linearRadioButton")
        self.linearRadioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.linearRadioButton)

        self.smoothRadioButton = QRadioButton(self.plotSettingGroupBox)
        self.smoothRadioButton.setObjectName(u"smoothRadioButton")

        self.horizontalLayout_2.addWidget(self.smoothRadioButton)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(580, 460, 49, 16))
        self.mzPlotRangeLineEdit = QLineEdit(self.centralwidget)
        self.mzPlotRangeLineEdit.setObjectName(u"mzPlotRangeLineEdit")
        self.mzPlotRangeLineEdit.setGeometry(QRect(630, 457, 61, 24))
        self.mzPlotRangeLineEdit.setValidator((QIntValidator()))

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

    def saveInterestedMass_clicked(self):
        file = QFileDialog.getSaveFileName(self,
            "Save interested mass list file", "", "Text Files (*.txt)")
        fileName = file[0]
        print(fileName)
        if fileName:
            with open(fileName, "w") as f:
                f.write(self.interestedMassTextEdit.toPlainText())

    def loadInterestedMass_clicked(self):
        file = QFileDialog.getOpenFileName(self,
            "Open interested mass list file", "", "Text Files (*.txt)")
        fileName = file[0]
        print(fileName)
        if not fileName:
            print("cancelled")
        else:
            with open(fileName, "r") as f:
                self.interestedMassTextEdit.setPlainText(f.read())

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
            return

        if self.customeRangeRadioButton.isChecked() and ( not self.fromRangeLineEdit.text() or not self.toRangeLineEdit.text()):
            QMessageBox.warning(self, "Warning", "Custome ranage is not available")
            return

        imsScanNum = int(self.totalImsEdit.text())
        msNumInIms = int(self.massPerImsEdit.text())
        #massScanRange = (100, 1100) if flex else (600, 1600)

        peaksInterestedPlainText = self.interestedMassTextEdit.toPlainText()
        peaksInterested = [float(line.strip()) for line in peaksInterestedPlainText.split()]

        if not peaksInterested:
            QMessageBox.warning(self, "Warning", "No mass list available!")
            return

        if not self.mzPlotRangeLineEdit.text():
            QMessageBox.warning(self, "Warning", "No mz plot range available!")
            return
        mzPlotRange = int(self.mzPlotRangeLineEdit.text().strip())

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
                if self.customeRangeRadioButton.isChecked():
                    if not (scanStart >= int(self.fromRangeLineEdit.text().strip()) and scanStart <= int(self.toRangeLineEdit.text().strip()) - msNumInIms):
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
            plt.text(max_arriving_time - mzPlotRange * 0.9, 1.1,r'$\mu=%.4f$'%(meanstatistics))
            plt.text(max_arriving_time - mzPlotRange * 0.9, 1.05,r'$RSD=%.4f$'%(rtdstatistics))
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
        self.loadInterestedMassButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.saveInterestedMassButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))

        self.fullRangeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Full Range", None))
        self.customeRangeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Custome Range", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"To", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"List of interested m/s", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"scan: start time", None))
        self.plotSettingGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Plot setting:", None))
        self.massRangeGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mass scan range:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"mz (+/-):", None))
        self.mzPlotRangeLineEdit.setText(QCoreApplication.translate("MainWindow", u"200", None))
    # retranslateUi

