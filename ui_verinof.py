# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'verinof.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Verinof(object):
    def setupUi(self, Verinof):
        if not Verinof.objectName():
            Verinof.setObjectName(u"Verinof")
        Verinof.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Verinof)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Ver = QLabel(Verinof)
        self.Ver.setObjectName(u"Ver")

        self.verticalLayout.addWidget(self.Ver)

        self.label = QLabel(Verinof)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.Time = QLabel(Verinof)
        self.Time.setObjectName(u"Time")

        self.verticalLayout.addWidget(self.Time)

        self.Server = QPushButton(Verinof)
        self.Server.setObjectName(u"Server")

        self.verticalLayout.addWidget(self.Server)

        self.down = QPushButton(Verinof)
        self.down.setObjectName(u"down")

        self.verticalLayout.addWidget(self.down)


        self.retranslateUi(Verinof)

        QMetaObject.connectSlotsByName(Verinof)
    # setupUi

    def retranslateUi(self, Verinof):
        Verinof.setWindowTitle(QCoreApplication.translate("Verinof", u"Minecraft Info", None))
        self.Ver.setText(QCoreApplication.translate("Verinof", u"\u7248\u672c", None))
        self.label.setText(QCoreApplication.translate("Verinof", u"\u7c7b\u578b", None))
        self.Time.setText(QCoreApplication.translate("Verinof", u"\u53d1\u5e03\u65f6\u95f4", None))
        self.Server.setText(QCoreApplication.translate("Verinof", u"\u4e0b\u8f7d\u670d\u52a1\u7aef", None))
        self.down.setText(QCoreApplication.translate("Verinof", u"\u4e0b\u8f7d\u5ba2\u6237\u7aef", None))
    # retranslateUi

