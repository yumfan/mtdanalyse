import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog, QMainWindow, qApp
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.Main_Window import Ui_MainWindow
import pandas as pd
import os
import glob
import numpy as np
import matplotlib.pyplot as plt


class MyMain(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMain, self).__init__()
        self.setupUi(self)


    def show_MainWindow():
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui=MyMain()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyMain()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        #show_MainWindow()
        #show_MainWindow()
        #path=root
        # visitDir(path)

