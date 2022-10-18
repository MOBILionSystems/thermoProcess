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
    QListWidgetItem, QMessageBox)

from pymsfilereader import MSFileReader
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 663)
        self.rawFile = None
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
        self.label.setGeometry(QRect(570, 50, 91, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(570, 90, 101, 21))

        self.totalImsEdit = QLineEdit(self.centralwidget)
        self.totalImsEdit.setObjectName(u"totalImsEdit")
        self.totalImsEdit.setGeometry(QRect(670, 50, 113, 24))
        self.massPerImsEdit = QLineEdit(self.centralwidget)
        self.massPerImsEdit.setObjectName(u"massPerImsEdit")
        self.massPerImsEdit.setGeometry(QRect(670, 90, 113, 24))
        self.totalMassScanNumberLabel = QLabel(self.centralwidget)
        self.totalMassScanNumberLabel.setObjectName(u"totalMassScanNumberLabel")
        self.totalMassScanNumberLabel.setGeometry(QRect(570, 15, 211, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 752, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def openFile_clicked(self):
        file = QFileDialog.getOpenFileName(self,
            "Open Thermo file", "", "RAW Files (*.raw)")
        fileName = file[0]
        print(fileName)
        if not fileName:
            print("cancelled")
        else:
            self.rawFile = MSFileReader(fileName)
            self.fileNameLabel.setText(os.path.basename(fileName))

    def analysis_clicked(self):
        if not self.rawFile:
            QMessageBox.warning(self, "Warning", "No raw file loaded!")
        else:
            numSpectra = self.rawFile.GetNumSpectra()
            self.totalMassScanNumberLabel.setText("Total mass scans: %i" %(numSpectra))
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.fileNameLabel.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.analysisButton.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total IMS scans:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mass scans / IMS:", None))
        self.totalMassScanNumberLabel.setText(QCoreApplication.translate("MainWindow", u"", None))
    # retranslateUi

