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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

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
        self.fileNameLabel = QLabel(self.centralwidget)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(10, 70, 201, 31))
        self.analysisButton = QPushButton(self.centralwidget)
        self.analysisButton.setObjectName(u"analysisButton")
        self.analysisButton.setGeometry(QRect(130, 30, 80, 24))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(230, 30, 301, 192))
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
        self.arrivingPlotButton.setGeometry(QRect(410, 520, 80, 24))
        self.loadInterestedMassButton = QPushButton(self.centralwidget)
        self.loadInterestedMassButton.setObjectName(u"loadInterestedMassButton")
        self.loadInterestedMassButton.setGeometry(QRect(100, 520, 80, 24))
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
        self.toRangeLineEdit = QLineEdit(self.centralwidget)
        self.toRangeLineEdit.setObjectName(u"toRangeLineEdit")
        self.toRangeLineEdit.setGeometry(QRect(630, 380, 71, 24))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 832, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.fileNameLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.analysisButton.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total IMS scans:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mass scans / IMS:", None))
        self.totalMassScanNumberLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.arrivingPlotButton.setText(QCoreApplication.translate("MainWindow", u"Arriving Time", None))
        self.loadInterestedMassButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.saveInterestedMassButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.fromRangeLineEdit.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.toRangeLineEdit.setText(QCoreApplication.translate("MainWindow", u"1100", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"List of interested m/s", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"scan: start time", None))
        self.massRangeGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mass scan range", None))
        self.fullRangeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Full Range", None))
        self.customeRangeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Custome Range", None))
        self.plotSettingGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Plot setting:", None))
        self.linearRadioButton.setText(QCoreApplication.translate("MainWindow", u"Linear", None))
        self.smoothRadioButton.setText(QCoreApplication.translate("MainWindow", u"Smooth", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"mz (+/-):", None))
        self.mzPlotRangeLineEdit.setText(QCoreApplication.translate("MainWindow", u"200", None))
    # retranslateUi

