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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

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
        self.fileNameLabel = QLabel(self.centralwidget)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(10, 70, 201, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 30, 80, 24))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(230, 0, 321, 192))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(570, 90, 91, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(570, 50, 101, 21))
        self.totalmsEdit = QLineEdit(self.centralwidget)
        self.totalmsEdit.setObjectName(u"totalmsEdit")
        self.totalmsEdit.setGeometry(QRect(670, 90, 113, 24))
        self.massPerImsEdit = QLineEdit(self.centralwidget)
        self.massPerImsEdit.setObjectName(u"massPerImsEdit")
        self.massPerImsEdit.setGeometry(QRect(670, 50, 113, 24))
        self.totalMassScanNumberLabel = QLabel(self.centralwidget)
        self.totalMassScanNumberLabel.setObjectName(u"totalMassScanNumberLabel")
        self.totalMassScanNumberLabel.setGeometry(QRect(570, 15, 211, 21))
        self.arrivingPlotButton = QPushButton(self.centralwidget)
        self.arrivingPlotButton.setObjectName(u"arrivingPlotButton")
        self.arrivingPlotButton.setGeometry(QRect(410, 400, 80, 24))
        self.linearRadioButton = QRadioButton(self.centralwidget)
        self.linearRadioButton.setObjectName(u"linearRadioButton")
        self.linearRadioButton.setGeometry(QRect(410, 310, 91, 22))
        self.smoothRadioButton = QRadioButton(self.centralwidget)
        self.smoothRadioButton.setObjectName(u"smoothRadioButton")
        self.smoothRadioButton.setGeometry(QRect(530, 310, 91, 22))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 360, 121, 16))
        self.startMassEdit = QLineEdit(self.centralwidget)
        self.startMassEdit.setObjectName(u"startMassEdit")
        self.startMassEdit.setGeometry(QRect(530, 357, 51, 24))
        self.loadInterestedMassButton = QPushButton(self.centralwidget)
        self.loadInterestedMassButton.setObjectName(u"loadInterestedMassButton")
        self.loadInterestedMassButton.setGeometry(QRect(100, 510, 80, 24))
        self.saveInterestedMassButton = QPushButton(self.centralwidget)
        self.saveInterestedMassButton.setObjectName(u"saveInterestedMassButton")
        self.saveInterestedMassButton.setGeometry(QRect(275, 510, 80, 24))
        self.interestedMassTextEdit = QPlainTextEdit(self.centralwidget)
        self.interestedMassTextEdit.setObjectName(u"interestedMassTextEdit")
        self.interestedMassTextEdit.setGeometry(QRect(100, 310, 251, 171))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 876, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.openFileButton.clicked.connect(MainWindow.openFile_clicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.fileNameLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total IMS scans:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mass scans / IMS:", None))
        self.totalMassScanNumberLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.arrivingPlotButton.setText(QCoreApplication.translate("MainWindow", u"Arriving Time", None))
        self.linearRadioButton.setText(QCoreApplication.translate("MainWindow", u"Linear", None))
        self.smoothRadioButton.setText(QCoreApplication.translate("MainWindow", u"Smooth", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start from mass sacn:", None))
        self.startMassEdit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.loadInterestedMassButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.saveInterestedMassButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

