# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MCVL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(535, 311)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_6 = QVBoxLayout(self.tab_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(self.tab_1)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_12)

        self.horizontalSpacer = QSpacerItem(1, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.minecrafpathenit = QLineEdit(self.groupBox)
        self.minecrafpathenit.setObjectName(u"minecrafpathenit")

        self.horizontalLayout_2.addWidget(self.minecrafpathenit)

        self.mcpathfine = QToolButton(self.groupBox)
        self.mcpathfine.setObjectName(u"mcpathfine")

        self.horizontalLayout_2.addWidget(self.mcpathfine)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setTextFormat(Qt.AutoText)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_13)

        self.horizontalSpacer_2 = QSpacerItem(30, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.javapathenit = QLineEdit(self.groupBox)
        self.javapathenit.setObjectName(u"javapathenit")

        self.horizontalLayout_3.addWidget(self.javapathenit)

        self.javapathsearch = QToolButton(self.groupBox)
        self.javapathsearch.setObjectName(u"javapathsearch")

        self.horizontalLayout_3.addWidget(self.javapathsearch)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_14)

        self.horizontalSpacer_3 = QSpacerItem(23, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.MCVer = QLineEdit(self.groupBox)
        self.MCVer.setObjectName(u"MCVer")

        self.horizontalLayout_4.addWidget(self.MCVer)

        self.mcversionnamefind = QToolButton(self.groupBox)
        self.mcversionnamefind.setObjectName(u"mcversionnamefind")

        self.horizontalLayout_4.addWidget(self.mcversionnamefind)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_15)

        self.horizontalSpacer_4 = QSpacerItem(17, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.PlayerName = QLineEdit(self.groupBox)
        self.PlayerName.setObjectName(u"PlayerName")

        self.horizontalLayout_5.addWidget(self.PlayerName)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SaveJson = QPushButton(self.groupBox)
        self.SaveJson.setObjectName(u"SaveJson")

        self.horizontalLayout.addWidget(self.SaveJson)

        self.F5Json = QPushButton(self.groupBox)
        self.F5Json.setObjectName(u"F5Json")

        self.horizontalLayout.addWidget(self.F5Json)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.VersionInStart = QLabel(self.tab_1)
        self.VersionInStart.setObjectName(u"VersionInStart")

        self.gridLayout.addWidget(self.VersionInStart, 0, 2, 1, 1)

        self.progressBar = QProgressBar(self.tab_1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 0, 1, 1, 1)

        self.StartGames = QPushButton(self.tab_1)
        self.StartGames.setObjectName(u"StartGames")

        self.gridLayout.addWidget(self.StartGames, 0, 3, 1, 1)

        self.label_16 = QLabel(self.tab_1)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget_3 = QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_5 = QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ZSB_New_L = QLabel(self.tab_5)
        self.ZSB_New_L.setObjectName(u"ZSB_New_L")

        self.verticalLayout_5.addWidget(self.ZSB_New_L)

        self.ZSBLIST = QListView(self.tab_5)
        self.ZSBLIST.setObjectName(u"ZSBLIST")

        self.verticalLayout_5.addWidget(self.ZSBLIST)

        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_8 = QVBoxLayout(self.tab_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.KZB_New_L = QLabel(self.tab_6)
        self.KZB_New_L.setObjectName(u"KZB_New_L")

        self.verticalLayout_8.addWidget(self.KZB_New_L)

        self.KZBLIST = QListView(self.tab_6)
        self.KZBLIST.setObjectName(u"KZBLIST")

        self.verticalLayout_8.addWidget(self.KZBLIST)

        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_10 = QVBoxLayout(self.tab_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.OLDLIST = QListView(self.tab_7)
        self.OLDLIST.setObjectName(u"OLDLIST")

        self.verticalLayout_10.addWidget(self.OLDLIST)

        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.verticalLayout_7 = QVBoxLayout(self.tab_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.QT_Text = QTextEdit(self.tab_10)
        self.QT_Text.setObjectName(u"QT_Text")

        self.verticalLayout_7.addWidget(self.QT_Text)

        self.tabWidget_3.addTab(self.tab_10, "")

        self.verticalLayout_3.addWidget(self.tabWidget_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.AboutTitle = QLabel(self.tab_3)
        self.AboutTitle.setObjectName(u"AboutTitle")

        self.verticalLayout_2.addWidget(self.AboutTitle)

        self.Name = QLabel(self.tab_3)
        self.Name.setObjectName(u"Name")

        self.verticalLayout_2.addWidget(self.Name)

        self.Version = QLabel(self.tab_3)
        self.Version.setObjectName(u"Version")

        self.verticalLayout_2.addWidget(self.Version)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget_2 = QTabWidget(self.tab_4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_9 = QVBoxLayout(self.tab_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.F5GG = QPushButton(self.tab_8)
        self.F5GG.setObjectName(u"F5GG")

        self.verticalLayout_9.addWidget(self.F5GG)

        self.GGtext = QTextEdit(self.tab_8)
        self.GGtext.setObjectName(u"GGtext")

        self.verticalLayout_9.addWidget(self.GGtext)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_4 = QVBoxLayout(self.tab_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lcdNumber = QLCDNumber(self.tab_9)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setProperty("value", 0.000000000000000)
        self.lcdNumber.setProperty("intValue", 0)

        self.verticalLayout_4.addWidget(self.lcdNumber)

        self.F5RPZ = QPushButton(self.tab_9)
        self.F5RPZ.setObjectName(u"F5RPZ")

        self.verticalLayout_4.addWidget(self.F5RPZ)

        self.lookRPZcode = QPushButton(self.tab_9)
        self.lookRPZcode.setObjectName(u"lookRPZcode")

        self.verticalLayout_4.addWidget(self.lookRPZcode)

        self.tabWidget_2.addTab(self.tab_9, "")

        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout_7.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MCVL Alpha", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u" MCVL  \u542f\u52a8\u914d\u7f6e", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u".minecraft\u8def\u5f84\uff1a", None))
        self.mcpathfine.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u" Java\u8def\u5f84\uff1a", None))
        self.javapathsearch.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"mc\u7248\u672c\u540d\u79f0\uff1a", None))
        self.mcversionnamefind.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"   \u89d2\u8272\u540d\u79f0\uff1a", None))
        self.PlayerName.setText(QCoreApplication.translate("MainWindow", u"MCVL\u7528\u6237", None))
        self.SaveJson.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.F5Json.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u914d\u7f6e", None))
        self.VersionInStart.setText(QCoreApplication.translate("MainWindow", u"MCVL Beta 0.0.5664", None))
        self.StartGames.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u6e38\u620f", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u8fdb\u5ea6\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u6e38\u620f", None))
        self.ZSB_New_L.setText(QCoreApplication.translate("MainWindow", u"\u6700\u65b0\u7248\u672c\uff1a", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u6b63\u5f0f\u7248", None))
        self.KZB_New_L.setText(QCoreApplication.translate("MainWindow", u"\u6700\u65b0\u5feb\u7167\uff1a", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u5feb\u7167\u7248\u672c", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u8001\u7248\u672c", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Request\u4fe1\u606f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.AboutTitle.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e MCVL Alpha", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"\u5168\u540d\uff1aMiner MineCraft Java Version Launcher For Windows Alpha", None))
        self.Version.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c\uff1a  Alpha 0.0.5665", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1\u4eba\u5458\uff1a\u5c0f\u9093\u5b66\u7f16\u7a0b\u3001\u718a\u718a\u7cd6\u679c\u3001\u670d\u4f5c\u8005", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u54c1\uff1aMiner \u5de5\u4f5c\u5ba4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME\uff1a<a href=\"http://minerstudio.xyz/\">http://minerstudio.xyz/</a>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1\u8bed\u8a00\uff1aPython3", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u73af\u5883\uff1a WinALL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.F5GG.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u516c\u544a", None))
        self.GGtext.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"MCVL\u516c\u544a\u677f", None))
        self.F5RPZ.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u4eca\u65e5\u4eba\u54c1\uff08\u767e\u5206\u5236\uff09", None))
        self.lookRPZcode.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u8bc6\u522b\u7801", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u4eba\u54c1\u503c\u6d4b\u8bd5\u5668", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
    # retranslateUi

