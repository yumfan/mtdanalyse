# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Logon_Windows.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Form(object):
    def setupUi(self, Main_Form):
        Main_Form.setObjectName("Main_Form")
        Main_Form.resize(382, 156)
        self.Query_Database = QtWidgets.QPushButton(Main_Form)
        self.Query_Database.setGeometry(QtCore.QRect(32, 60, 131, 31))
        self.Query_Database.setObjectName("Query_Database")
        self.Import_Database = QtWidgets.QPushButton(Main_Form)
        self.Import_Database.setGeometry(QtCore.QRect(190, 60, 131, 31))
        self.Import_Database.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Import_Database.setObjectName("Import_Database")
        self.Exit = QtWidgets.QPushButton(Main_Form)
        self.Exit.setGeometry(QtCore.QRect(130, 110, 93, 28))
        self.Exit.setObjectName("Exit")

        self.retranslateUi(Main_Form)
        QtCore.QMetaObject.connectSlotsByName(Main_Form)

    def retranslateUi(self, Main_Form):
        _translate = QtCore.QCoreApplication.translate
        Main_Form.setWindowTitle(_translate("Main_Form", "Main_Form"))
        self.Query_Database.setText(_translate("Main_Form", "Query_Database"))
        self.Import_Database.setText(_translate("Main_Form", "Import_Database"))
        self.Exit.setText(_translate("Main_Form", "Exit"))
