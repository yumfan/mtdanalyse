# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(220, 270, 93, 28))
        self.Exit.setObjectName("Exit")
        self.Save_Result = QtWidgets.QPushButton(self.centralwidget)
        self.Save_Result.setGeometry(QtCore.QRect(90, 270, 93, 28))
        self.Save_Result.setObjectName("Save_Result")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(480, 260, 72, 15))
        self.label_1.setObjectName("label_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSelect_Test_Result_Folder = QtWidgets.QAction(MainWindow)
        self.actionSelect_Test_Result_Folder.setObjectName("actionSelect_Test_Result_Folder")
        self.toolBar.addAction(self.actionSelect_Test_Result_Folder)

        self.retranslateUi(MainWindow)
        #self.Exit.clicked.connect(QtCore.QCoreApplication.instance().exit)
        self.Save_Result.clicked.connect(self.Save)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ASIC Test Result Analysis System"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.Save_Result.setText(_translate("MainWindow", "Save_Result"))
        self.label_1.setText(_translate("MainWindow", "TextLabel"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSelect_Test_Result_Folder.setText(_translate("MainWindow", "Select Test Result Folder"))

    def Save(self):
        self.label_1.setText("9")