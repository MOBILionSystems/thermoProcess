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
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.openFileButton = QPushButton(self.centralwidget)
        self.openFileButton.setObjectName(u"openFileButton")

        self.horizontalLayout_5.addWidget(self.openFileButton)

        self.analysisButton = QPushButton(self.centralwidget)
        self.analysisButton.setObjectName(u"analysisButton")

        self.horizontalLayout_5.addWidget(self.analysisButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.fileNameLabel = QLabel(self.centralwidget)
        self.fileNameLabel.setObjectName(u"fileNameLabel")

        self.verticalLayout_3.addWidget(self.fileNameLabel)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.totalMassScanNumberLabel = QLabel(self.centralwidget)
        self.totalMassScanNumberLabel.setObjectName(u"totalMassScanNumberLabel")

        self.verticalLayout.addWidget(self.totalMassScanNumberLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.massPerImsEdit = QLineEdit(self.centralwidget)
        self.massPerImsEdit.setObjectName(u"massPerImsEdit")

        self.horizontalLayout_3.addWidget(self.massPerImsEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.totalImsEdit = QLineEdit(self.centralwidget)
        self.totalImsEdit.setObjectName(u"totalImsEdit")

        self.horizontalLayout_4.addWidget(self.totalImsEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.interestedMassTextEdit = QPlainTextEdit(self.centralwidget)
        self.interestedMassTextEdit.setObjectName(u"interestedMassTextEdit")

        self.verticalLayout_4.addWidget(self.interestedMassTextEdit)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.loadInterestedMassButton = QPushButton(self.centralwidget)
        self.loadInterestedMassButton.setObjectName(u"loadInterestedMassButton")

        self.horizontalLayout_7.addWidget(self.loadInterestedMassButton)

        self.saveInterestedMassButton = QPushButton(self.centralwidget)
        self.saveInterestedMassButton.setObjectName(u"saveInterestedMassButton")

        self.horizontalLayout_7.addWidget(self.saveInterestedMassButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_12.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.massRangeGroupBox = QGroupBox(self.centralwidget)
        self.massRangeGroupBox.setObjectName(u"massRangeGroupBox")
        self.horizontalLayout = QHBoxLayout(self.massRangeGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fullRangeRadioButton = QRadioButton(self.massRangeGroupBox)
        self.fullRangeRadioButton.setObjectName(u"fullRangeRadioButton")
        self.fullRangeRadioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.fullRangeRadioButton)

        self.customeRangeRadioButton = QRadioButton(self.massRangeGroupBox)
        self.customeRangeRadioButton.setObjectName(u"customeRangeRadioButton")

        self.horizontalLayout.addWidget(self.customeRangeRadioButton)


        self.verticalLayout_5.addWidget(self.massRangeGroupBox)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.fromRangeLineEdit = QLineEdit(self.centralwidget)
        self.fromRangeLineEdit.setObjectName(u"fromRangeLineEdit")

        self.horizontalLayout_8.addWidget(self.fromRangeLineEdit)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.toRangeLineEdit = QLineEdit(self.centralwidget)
        self.toRangeLineEdit.setObjectName(u"toRangeLineEdit")

        self.horizontalLayout_8.addWidget(self.toRangeLineEdit)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.plotSettingGroupBox = QGroupBox(self.centralwidget)
        self.plotSettingGroupBox.setObjectName(u"plotSettingGroupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.plotSettingGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.linearRadioButton = QRadioButton(self.plotSettingGroupBox)
        self.linearRadioButton.setObjectName(u"linearRadioButton")
        self.linearRadioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.linearRadioButton)

        self.smoothRadioButton = QRadioButton(self.plotSettingGroupBox)
        self.smoothRadioButton.setObjectName(u"smoothRadioButton")

        self.horizontalLayout_2.addWidget(self.smoothRadioButton)


        self.horizontalLayout_10.addWidget(self.plotSettingGroupBox, 0, Qt.AlignBottom)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.mzPlotRangeLineEdit = QLineEdit(self.centralwidget)
        self.mzPlotRangeLineEdit.setObjectName(u"mzPlotRangeLineEdit")

        self.horizontalLayout_9.addWidget(self.mzPlotRangeLineEdit)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.arrivingPlotButton = QPushButton(self.centralwidget)
        self.arrivingPlotButton.setObjectName(u"arrivingPlotButton")

        self.verticalLayout_5.addWidget(self.arrivingPlotButton)


        self.horizontalLayout_12.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 21))
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
        self.analysisButton.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.fileNameLabel.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"scan: start time", None))
        self.totalMassScanNumberLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mass scans / IMS:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total IMS scans:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"List of interested m/s", None))
        self.loadInterestedMassButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.saveInterestedMassButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.massRangeGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mass scan range", None))
        self.fullRangeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Full Range", None))
        self.customeRangeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Custome Range", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.fromRangeLineEdit.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.toRangeLineEdit.setText(QCoreApplication.translate("MainWindow", u"1100", None))
        self.plotSettingGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Plot setting:", None))
        self.linearRadioButton.setText(QCoreApplication.translate("MainWindow", u"Linear", None))
        self.smoothRadioButton.setText(QCoreApplication.translate("MainWindow", u"Smooth", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"mz (+/-):", None))
        self.mzPlotRangeLineEdit.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.arrivingPlotButton.setText(QCoreApplication.translate("MainWindow", u"Arriving Time", None))
    # retranslateUi

