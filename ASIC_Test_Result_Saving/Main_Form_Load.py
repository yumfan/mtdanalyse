import os
from logging import warning

import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog, QTableView
from PyQt5 import QtCore, QtGui, QtWidgets, Qt,QtSql
from GUI.Main_Form import Ui_Form
import sys
from Database.My_Sql_Driver import database_operation
from data_plot.Normal_distribution_Plot import curve_plot
import Excel.Excel_operation
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib
from pylab import *  # 支持中文

matplotlib.style.use('ggplot')

DUT_sn="All"
DUT_time="All"
DUT_result="All"
DUT_case="All"
Test_Configuration="All"
Case_Result="All"
time="All"


root=""
fileNum = 0
#sn_row=0
#time_row=0
#result_row=0
#case_row=0
table1 = "status_result"
table2 = "test_result"
Test_Configuration="All"

class MyMain(QWidget,Ui_Form):
    def __init__(self):
        super(MyMain, self).__init__()
        self.QSqlDatabase = None
        self.setupUi(self)
        #self.tableView.setHidden(True)
        #self.tableView.hide()
        self.textEdit_2.setHidden(True)
        self.Exit.clicked.connect(QtCore.QCoreApplication.instance().exit)       # close为内置
        self.Import_DUT.clicked.connect(self.save_database)     # 建立信号和槽，Import_DUT即为按钮2的objectName，save_database为槽也就是自定义的方法
        self.select.clicked.connect(self.select_folder)
        self.Query_Database.clicked.connect(self.query)
        # 单击QListView列表触发自定义的槽函数
        self.sn_list.clicked.connect(self.sn_clicked)
        self.test_time_list.clicked.connect(self.time_clicked)
        self.Result_List.clicked.connect(self.result_clicked)
        self.Test_Case_List.clicked.connect(self.case_clicked)
        self.Plot_Series.clicked.connect(self.Do_Plot_Series)
        self.Plot_Nor_Distribution.clicked.connect(self.Do_Plot_Normal_Distribution)
        self.Plot_Histogram.clicked.connect(self.Do_Plot_Histogram)
        self.Test_Config_List.clicked.connect(self.config_List_clicked)
        self.Case_Result_List.clicked.connect(self.C_Result_List_clicked)
        self.ShowData.clicked.connect(self.showData)

    def Do_Plot_Normal_Distribution(self):
        global DUT_sn, DUT_time, DUT_result, DUT_case, Test_Configuration,Case_Result
        # print(sn_row,time_row,result_row,case_row)
        # print(case_row)

        f = database_operation()
        if DUT_case=="All":
            QMessageBox.warning(self,"Error","please select a test case",QMessageBox.Yes)              #only can analyse the assigned test case and it will be fail when case is all
            return
        if Test_Configuration=="All":
            QMessageBox.warning(self,"Error","please select a test configuration",QMessageBox.Yes)     #must select the test confdiguration
            return
        result1_array = []
        sn_array = []
        min1_array = []
        max1_array = []
        b = f.query_database(
            "SELECT Result1 FROM " + table2 + " where Test_Case= " + "\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        a = f.query_database(
            "SELECT SN FROM " + table2 + " where Test_Case= " + "\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        c = f.query_database(
            "SELECT SpecMin1 FROM " + table2 + " where Test_Case= " + "\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        d = f.query_database(
            "SELECT SpecMax1 FROM " + table2 + " where Test_Case= " + "\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        #Test_Configuration = "All"
        for i in range(len(b)):
            temp = list(b[i][:1])  # b[i][:1] remove the ,  from ((32888,),(300002,),.....) to list format
            temp_str = temp[0]  # get the value from the list [32800]
            result1_array.append(temp_str)  # convert the mysql query result to [x,x,x....] format
            temp = list(a[i][:1])
            temp_str = temp[0]
            sn_array.append(temp_str)
            temp = list(c[i][:1])
            temp_str = temp[0]
            min1_array.append(temp_str)
            temp = list(d[i][:1])
            temp_str = temp[0]
            max1_array.append(temp_str)
        g = curve_plot()
        g.plot_Nor_Distribution(result1_array,min1_array[0],max1_array[0],DUT_case,Test_Configuration)
        Test_Configuration = "All"

    def Do_Plot_Histogram(self):
        global DUT_sn, DUT_time, DUT_result, DUT_case, Test_Configuration,Case_Result
        # print(sn_row,time_row,result_row,case_row)
        # print(case_row)

        f = database_operation()
        if DUT_case=="All":
            QMessageBox.warning(self,"Error","please select a test case",QMessageBox.Yes)
            return
        if Test_Configuration=="All":
            QMessageBox.warning(self,"Error","please select a test configuration",QMessageBox.Yes)
            return
        result1_array = []
        sn_array = []
        min1_array = []
        max1_array = []
        b = f.query_database(
            "SELECT Result1 FROM " + table2 + " where Test_Case= " + "\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        a = f.query_database(
            "SELECT SN FROM " + table2 + " where Test_Case= " + "\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        c = f.query_database(
            "SELECT SpecMin1 FROM " + table2 + " where Test_Case= " + "\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        d = f.query_database(
            "SELECT SpecMax1 FROM " + table2 + " where Test_Case= " + "\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        #Test_Configuration = "All"
        for i in range(len(b)):
            temp = list(b[i][:1])  # b[i][:1] remove the ,  from ((32888,),(300002,),.....) to list format
            temp_str = temp[0]  # get the value from the list [32800]
            result1_array.append(temp_str)  # convert the mysql query result to [x,x,x....] format
            temp = list(a[i][:1])
            temp_str = temp[0]
            sn_array.append(temp_str)
            temp = list(c[i][:1])
            temp_str = temp[0]
            min1_array.append(temp_str)
            temp = list(d[i][:1])
            temp_str = temp[0]
            max1_array.append(temp_str)
        g = curve_plot()
        g.plot_historm(result1_array,min1_array[0],max1_array[0],DUT_case,Test_Configuration)
        Test_Configuration = "All"

    def Do_Plot_Series(self):
        global  DUT_sn,DUT_time,DUT_result,DUT_case,Test_Configuration,Case_Result
        #print(sn_row,time_row,result_row,case_row)
        #print(case_row)
        print(DUT_case,Test_Configuration)
        f = database_operation()
        if DUT_case=="All":
            QMessageBox.warning(self,"Error","please select a test case",QMessageBox.Yes)
            return
        if Test_Configuration=="All":
            QMessageBox.warning(self,"Error","please select a test configuration",QMessageBox.Yes)
            return
        result1_array=[]
        sn_array=[]
        min1_array=[]
        max1_array=[]
        b = f.query_database("SELECT Result1 FROM " + table2 + " where Test_Case= " +"\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        a = f.query_database("SELECT SN FROM " + table2 + " where Test_Case= " +"\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        c = f.query_database("SELECT SpecMin1 FROM " + table2 + " where Test_Case= " +"\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        d = f.query_database("SELECT SpecMax1 FROM " + table2 + " where Test_Case= " +"\"" + DUT_case + "\"" + " and Test_Configuration=" + "\"" + Test_Configuration + "\"")
        #b = f.query_database("SELECT Result1 FROM " + table2 + " where Test_Case= " +"\"" + DUT_case + "\"" +" and Status='pass'")
        #a = f.query_database("SELECT SN FROM " + table2 + " where Test_Case= " +"\"" + DUT_case + "\"" +" and Status='pass'")
        #c = f.query_database("SELECT SpecMin1 FROM " + table2 + " where Test_Case= " +"\"" + DUT_case + "\"" +" and Status='pass'")
        #d = f.query_database("SELECT SpecMax1 FROM " + table2 + " where Test_Case= " +"\"" + DUT_case + "\"" +" and Status='pass'")

        for i in range(len(b)):
            temp=list(b[i][:1])                           #b[i][:1] remove the ,  from ((32888,),(300002,),.....) to list format
            temp_str=temp[0]                              #get the value from the list [32800]
            result1_array.append(temp_str)                #convert the mysql query result to [x,x,x....] format
            temp = list(a[i][:1])
            temp_str = temp[0]
            sn_array.append(temp_str)
            temp = list(c[i][:1])
            temp_str = temp[0]
            min1_array.append(temp_str)
            temp = list(d[i][:1])
            temp_str = temp[0]
            max1_array.append(temp_str)
        array_x=list(a)
        range_length=range(len(result1_array))
        #print(range_length)
        #print(a)
        #print(b)
        plt.figure(figsize=(10, 6))
        plt.title(DUT_case + "\n test configuration:%s \n total quantity=%s"%(Test_Configuration,len(result1_array)))          #set the title
        #plt.bar(range_length, result1_array)
        plt.plot(range_length,result1_array,'-b',label='result',linewidth=1.0)                                #range_length make sure how much x axis value:for example 1~100
        plt.plot(range_length, min1_array,'-r',label='min',linewidth=1.5)
        plt.plot(range_length, max1_array,'-r',label='max',linewidth=1.5)
        plt.xticks(range_length, array_x,rotation=30, fontsize='small')                                       #assign the x axis vaule with the str
        plt.xlabel('SN')
        plt.ylabel("123")
        plt.legend()
        plt.show()
        Test_Configuration = "All"
        '''
        arange=b
        #arange=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        print(type(arange))
        plt.plot(np.arange(5))
        plt.show()
        '''
    def query(self):
        print('正在点击按钮2')
        f = database_operation()
        b = f.query_database("SELECT * FROM " + table1)
        b=list(b)
        temp1 =[]
        temp2 =[]
        temp3=[]
        temp4=[]
        temp5=[]
        temp6=[]
        for i in range(len(b)):
            temp1 = list(b[:][i][1])                           #get the SN and convert form touple to listh
            temp2.append("".join(temp1))                       #remove the touple('f','a','n') to 'fan' and add the list
            temp3 = list(b[:][i][0].strftime('%Y-%m-%d %H:%M:%S'))
            temp4.append("".join(temp3))
            temp5=list(b[:][i][2])
            temp6.append("".join(temp5))
        temp2.insert(0,"All")
        temp4.insert(0,"All")
        temp6.insert(0,"All")
        # 实例化列表模型，添加数据列表
        self.model_1 = QtCore.QStringListModel()
        self.model_2 = QtCore.QStringListModel()
        self.model_3 = QtCore.QStringListModel()
        self.model_4 = QtCore.QStringListModel()
        self.model_5 = QtCore.QStringListModel()
        self.model_6 = QtCore.QStringListModel()
        # 添加列表数据
        self.model_1.setStringList(temp2)
        self.sn_list.setModel(self.model_1)
        self.sn_list = temp2
        self.model_2.setStringList(temp4)
        self.test_time_list.setModel(self.model_2)
        self.test_time_list=temp4
        self.model_3.setStringList(temp6)
        self.Result_List.setModel(self.model_3)
        self.Result_List=temp6
        temp7=[]
        temp8=[]
        temp9=[]
        temp10=["All"]
        temp11=[]
        temp12=["All"]

        b = f.query_database("SELECT distinct Test_Case FROM " + table2)
        for i in range(len(b)):
            temp7 = list(b[:][i])
            temp8.append("".join(temp7))
        temp8.insert(0, "All")
        self.model_4.setStringList(temp8)
        self.Test_Case_List.setModel(self.model_4)
        self.Test_Case_List = temp8
        self.model_5.setStringList(temp10)
        self.Test_Config_List.setModel(self.model_5)
        self.Test_Config_List = temp10
        self.model_6.setStringList(temp12)
        self.Case_Result_List.setModel(self.model_6)
        self.Case_Result_List = temp12



    def save_database(self):
        print('正在点击按钮2')
        self.textEdit_2.setHidden(False)
        self.Test_Case_List.setHidden(True)
        self.test_time_list.setHidden(True)
        self.Result_List.setHidden(True)
        f = database_operation()
        b = f.query_database("SELECT * FROM " + table1)
        chip_sn_time=Excel.Excel_operation.list_chip_sn_time(root)
        print(chip_sn_time)
        one_chip_test_result = []
        for each_chip in Excel.Excel_operation.list_chip_paths(root):
            chip_name = os.path.split(each_chip)[1]
            one_chip_test_result = Excel.Excel_operation.each_chip_test_result(each_chip,chip_name)
            one_chip_status=Excel.Excel_operation.summary_one_chip_data(one_chip_test_result)
            status_result_table_data="(\"%s\", \"%s\",\"%s\")"%(''.join(one_chip_test_result[:][0][0][1]),''.join(one_chip_test_result[:][0][0][0]),one_chip_status)
            columns = f.list_col(table1)
            f.insert_data(table1,columns,status_result_table_data)
            print(chip_name + "done")
            for i in range(len(one_chip_test_result[:])):
                result_str = ""
                for j in range(len(one_chip_test_result[:][i])):
                     result_str = ""
                     for k in range(len(one_chip_test_result[:][i][j])):
                        if ''.join(one_chip_test_result[:][i][j][k])=="Na" or ''.join(one_chip_test_result[:][i][j][k])=="Inf":
                             temp="0"
                        else:
                             temp=''.join(one_chip_test_result[:][i][j][k])
                        if k==len(one_chip_test_result[:][i][j])-1:
                             result_str=result_str+"\"" + temp+ "\""
                        else:
                             result_str = result_str + "\"" + temp + "\"" + ","
                     result_str="(" + result_str + ")"
                     columns = f.list_col(table2)
                     f.insert_data(table2, columns, result_str)
            self.textEdit_2.insertPlainText(chip_name + " Done"+ "\n")
            #QApplication.processEvents()                                              #refresh frame
                    #print(result_str)
        QMessageBox.information(self, "information", "Import Done", QMessageBox.Yes)

        #for i in range (1):
            #insert_command="INSERT INTO `mc05_test_result`.`status_result` (`SN`, `Status`) VALUES ('fa', 'fas')"
            #f.insert_data(table,columns,"('2020-03-02 12:14:34','fa330011jhg2ff22ddkaa', 'fas')")


    def select_folder(self, mylist=None):
        print('正在点击按钮3')
        global root
        root = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        self.textEdit.setText(root)
        mylist = Excel.Excel_operation.list_sn(root)
        # 实例化列表模型，添加数据列表
        self.model = QtCore.QStringListModel()
        # 添加列表数据
        self.model.setStringList(mylist)
        self.sn_list.setModel(self.model)
        self.sn_list = mylist

    def sn_clicked(self, qModelIndex):
        #global root
        #sql_command_option=self.check_query_option("sn")
        global  DUT_sn,DUT_time,DUT_result,DUT_case,Test_Configuration,Case_Result                  #set the global var
        sn_row = qModelIndex.row()                                                                  #get the clicked row index
        #self.model_1.removeRow(sn_row)         #删除点击的行
        # 获取当前选中行的数据
        DUT_sn = str(self.sn_list[sn_row])                                                          #get the content with the assigned row
        f = database_operation()                                                                    #open the database
        temp2=[]
        temp4=[]
        temp6=[]
        temp7=[]
        temp8=[]
        if DUT_sn=="All":
            DUT_time=DUT_result=DUT_case=Test_Configuration=Case_Result="All"
            b = f.query_database("SELECT * FROM " + table1)                                        #query all data from status_result table
            for i in range(len(b)):
                temp1 = list(b[i][1])  # get the SN and convert form touple to listh
                temp2.append("".join(temp1))  # remove the touple('f','a','n') to 'fan' and add the list,joint the f and a with ""
                temp3 = list(b[i][0].strftime('%Y-%m-%d %H:%M:%S'))
                temp4.append("".join(temp3))
                temp5 = list(b[i][2])
                temp6.append("".join(temp5))
            temp2.insert(0, "All")                                                                #add the "all" in first element
            temp4.insert(0, "All")
            temp6.insert(0, "All")
            self.model_1.setStringList(temp2)
            self.sn_list = temp2                                                                  #set the qlistlist to assigned list
            self.model_2.setStringList(temp4)
            self.test_time_list = temp4
            self.model_3.setStringList(temp6)
            self.Result_List = temp6
            print(DUT_sn)
            b = f.query_database("SELECT * FROM " + table2)
            self.showData(b)
        else:                                                                                            #if clicked the assigned DUT S/N need put the configuration and case detail in qlist
            b = f.query_database("SELECT * FROM " + table1 + " Where SN=" +"\"" + DUT_sn +"\"")
            for i in range(len(b)):
                temp1 = list(b[i][1])                           #get the SN and convert form touple to listh
                temp2.append("".join(temp1))                       #remove the touple('f','a','n') to 'fan' and add the list
                temp3 = list(b[i][0].strftime('%Y-%m-%d %H:%M:%S'))
                temp4.append("".join(temp3))
                temp5=list(b[i][2])
                temp6.append("".join(temp5))
        # 添加列表数据
            self.model_2.setStringList(temp4)                                                            #display the DUT test time and result in qlist
            self.test_time_list=temp4
            self.model_3.setStringList(temp6)
            self.Result_List=temp6
            b = f.query_database("SELECT Status FROM " + table2 + " Where SN=" +"\"" + DUT_sn +"\"")
            for i in range(len(b)):
                temp7 = list(b[i])  # get the SN and convert form touple to listh
                temp8.append("".join(temp7))  # remove the touple('f','a','n') to 'fan' and add the list
            # 添加列表数据
            temp8.insert(0, "All")
            self.model_6.setStringList(temp8)
            self.Case_Result_List = temp8
            b = f.query_database("SELECT * FROM " + table2 + self.check_query_option("sn") )
            self.showData(b)
            print(DUT_sn)
        return DUT_sn

    def time_clicked(self, qModelIndex):
        #global root
        global  DUT_sn,DUT_time,DUT_result,DUT_case,Test_Configuration
        time_row=qModelIndex.row()
        #print(time_row)
        # 获取当前选中行的数据
        DUT_time = str(self.test_time_list[time_row])
        #c=root + '/' + str(self.Result_List[qModelIndex.row()])
        #df = pd.DataFrame(pd.read_excel(a))
        #self.textEdit.setText(str(df))
        print(DUT_time)
        return DUT_time

    def result_clicked(self, qModelIndex):
        #global root
        global  DUT_sn,DUT_time,DUT_result,DUT_case,Test_Configuration
        result_row=qModelIndex.row()
        print(result_row)
        #print(result_row)
        # 获取当前选中行的数据
        DUT_result = str(self.Result_List[result_row])
        print(self.Result_List)
        print(DUT_result)
        f = database_operation()
        temp2=[]
        temp4=[]
        temp6=[]
        if DUT_result=="All":
            b = f.query_database("SELECT * FROM " + table1)
            for i in range(len(b)):
                temp1 = list(b[i][1])  # get the SN and convert form touple to listh
                temp2.append("".join(temp1))  # remove the touple('f','a','n') to 'fan' and add the list
                temp3 = list(b[i][0].strftime('%Y-%m-%d %H:%M:%S'))
                temp4.append("".join(temp3))
                temp5 = list(b[i][2])
                temp6.append("".join(temp5))
            temp2.insert(0, "All")
            temp4.insert(0, "All")
            temp6.insert(0, "All")
            self.model_1.setStringList(temp2)
            self.sn_list = temp2
            self.model_2.setStringList(temp4)
            self.test_time_list = temp4
            self.model_3.setStringList(temp6)
            self.Result_List = temp6
        else:
            b = f.query_database("SELECT * FROM " + table1 + " Where result=" +"\"" + DUT_result +"\"")
            for i in range(len(b)):
                temp1 = list(b[i][1])                           #get the SN and convert form touple to listh
                temp2.append("".join(temp1))                       #remove the touple('f','a','n') to 'fan' and add the list
                temp3 = list(b[i][0].strftime('%Y-%m-%d %H:%M:%S'))
                temp4.append("".join(temp3))
                temp5=list(b[i][2])
                temp6.append("".join(temp5))
        # 添加列表数据
            temp2.insert(0, "All")
            self.model_1.setStringList(temp2)
            self.sn_list = temp2
            temp4.insert(0, "All")
            self.model_2.setStringList(temp4)
            self.test_time_list=temp4
            if DUT_result=="pass":
                self.model_3.setStringList(["All","pass"])
                self.Result_List=["All","pass"]
            else:
                self.model_3.setStringList(["All", "fail"])
                self.Result_List = ["All", "fail"]
            print(self.Result_List)
        #print(DUT_sn)
        #c=root + '/' + str(self.Result_List[qModelIndex.row()])
        #df = pd.DataFrame(pd.read_excel(a))
        #self.textEdit.setText(str(df))
        #print(DUT_result)
        QApplication.processEvents()
        return DUT_result

    def case_clicked(self, qModelIndex):
        #global root
        global  DUT_sn,DUT_time,DUT_result,DUT_case,Test_Configuration
        case_row=qModelIndex.row()
        #print(case_row)
        # 获取当前选中行的数据
        DUT_case = str(self.Test_Case_List[case_row])
        temp7=[]
        temp8=[]
        temp9=[]
        temp10=[]
        temp11=[]
        temp12=[]
        temp13=[]
        temp14=[]
        f = database_operation()
        if DUT_case=="All":
            b = f.query_database("SELECT distinct Test_Case FROM " + table2)
            for i in range(len(b)):
                temp7 = list(b[:][i])
                temp8.append("".join(temp7))
            temp8.insert(0, "All")
            self.model_4.setStringList(temp8)
            self.Test_Case_List = temp8
        else:
            b = f.query_database("SELECT distinct Test_Configuration FROM " + table2 + " where Test_Case=" + "\""+DUT_case+"\"")
            for i in range(len(b)):
                temp13 = list(b[:][i])
                temp14.append("".join(temp13))
            temp14.insert(0, "All")
            self.model_5.setStringList(temp14)
            self.Test_Config_List = temp14
            if DUT_sn!="All" and DUT_time!="All" and DUT_case!="All":
                b = f.query_database("SELECT Status,Test_Configuration FROM " + table2 + " Where SN=" + "\"" + DUT_sn + "\"" + " and Time=" +"\"" + DUT_time + "\"" + " and Test_Case=" +"\"" + DUT_case + "\"")
                for i in range(len(b)):
                    temp9 = list(b[i][0])  # get the SN and convert form touple to listh
                    temp10.append("".join(temp9))  # remove the touple('f','a','n') to 'fan' and add the list
                    temp11 = list(b[i][1])  # get the SN and convert form touple to listh
                    temp12.append("".join(temp11))  # remove the touple('f','a','n') to 'fan' and add the list
            # 添加列表数据
                temp10.insert(0, "All")
                temp12.insert(0, "All")
                self.model_6.setStringList(temp10)
                self.Case_Result_List = temp10
                self.model_5.setStringList(temp12)
                self.Test_Config_List=temp12
                self.model_4.setStringList(["All",DUT_case])
                self.Test_Case_List = ["All",DUT_case]
                b = f.query_database("SELECT * FROM " + table2 + self.check_query_option("case"))
                self.showData(b)
            else:
                if DUT_sn == "All":
                   b = f.query_database("SELECT * FROM " + table2 + self.check_query_option("case"))
                   self.showData(b)
                else:
                    QMessageBox.warning(self, "Error", "please select the test time", QMessageBox.Yes)
                    return
        #c=root + '/' + str(self.Result_List[qModelIndex.row()])
        #df = pd.DataFrame(pd.read_excel(a))
        #self.textEdit.setText(str(df))
        return DUT_case

    def config_List_clicked(self, qModelIndex):
        global DUT_sn, DUT_time, DUT_result, DUT_case, Test_Configuration,Case_Result
        config_row = qModelIndex.row()
        # print(case_row)
        # 获取当前选中行的数据
        Test_Configuration = str(self.Test_Config_List[config_row])
        temp7=[]
        temp8=[]
        temp9=[]
        temp10=[]
        temp11=[]
        temp12=[]
        temp13=[]
        temp14=[]
        f = database_operation()
        b = f.query_database("SELECT * FROM " + table2 + self.check_query_option("config"))
        self.showData(b)
        return Test_Configuration

    def C_Result_List_clicked(self, qModelIndex):
        global DUT_sn, DUT_time, DUT_result, DUT_case, Test_Configuration,Case_Result

        print(DUT_sn)
        print("0")

    def check_query_option(self,select_option):
        #check the clicked item status
        sn_value=""
        time_value=""
        dut_result_value=""
        dut_case_value=""
        dut_configuration_value=""
        dut_case_result_value=""
        query_option=""
        sn_value_list=[]
        time_value_list=[]
        global DUT_sn, DUT_time, DUT_result, DUT_case, Test_Configuration, Case_Result
        if select_option=="sn" and DUT_sn!="All":
            sn_value=" SN=" +"\"" + DUT_sn +"\""
            query_option = " where" + sn_value
        if select_option == "case" and DUT_sn == "All":
            case_value = " Test_Case=" + "\"" + DUT_case + "\""
            query_option = " where" + case_value
        else:
            if select_option == "case" and DUT_sn != "All":
                case_value = " Test_Case=" + "\"" + DUT_case + "\"" + " AND SN=" + "\"" + DUT_sn + "\"" + " AND Time=" + "\"" + DUT_time + "\""
                query_option = " where" + case_value
        if select_option == "config" and DUT_sn == "All":
                case_value = " Test_Case=" + "\"" + DUT_case + "\"" + " And Test_Configuration=" +"\""+  Test_Configuration + "\""
                query_option = " where" + case_value
        else:
            if select_option == "config" and DUT_sn != "All":
                    case_value = " Test_Case=" + "\"" + DUT_case + "\"" + " AND SN=" + "\"" + DUT_sn + "\"" + " AND Time=" + "\"" + DUT_time + "\"" + " And Test_Configuration=" + "\""+ Test_Configuration + "\""
                    query_option = " where" + case_value


            '''
            if select_option=="test_time"and DUT_time!="All":
                  time_value=" Time=%s "%(DUT_time)
            if select_option=="dut_result" and DUT_result!="All" and DUT_sn!="All" and DUT_time=="All":
                  sn_value=" SN=%s "%(DUT_sn)
                  time_value = " Time=%s " % (DUT_time)
            else:
                if DUT_result=="All":
                    f = database_operation()
                    b = f.query_database("SELECT SN,Time FROM " + table1)
                    for data in b:
                        sn_value_list.append(data[:][1])
                        time_value_list.append(data[:][0])
                if DUT_result!="All":
                    f = database_operation()
                    b = f.query_database("SELECT SN,Time FROM " + table1 + " where result=%s"%(DUT_result))
                    for data in b:
                        sn_value_list.append(data[:][1])
                        time_value_list.append(data[:][0])
            if select_option == "case" and DUT_case != "All":
                dut_case_value = " Test_Case=%s " % (DUT_case)
            if select_option == "configuration" and Test_Configuration != "All":
                dut_configuration_value = " Test_Configuration=%s " % (Test_Configuration)
            if select_option == "case_result" and Case_Result != "All":
                dut_case_result_value = " Status=%s " % (Case_Result)
            '''
        return query_option
    '''
    class My_logon_Main(QWidget,Ui_Main_Form):
    def __init__(self):
        super(My_logon_Main, self).__init__()
        self.setupUi(self)
        self.Exit.clicked.connect(QtCore.QCoreApplication.instance().exit)
        self.Query_Database.clicked.connect(self.open_query_database)

    def open_query_database(self):
        open_window=MyMain()
        self.popwin = self.createPopwin(open_window)
        self.popwin.show()
    '''


    def showData(self,data):
        #display the data in qtable
        f = database_operation()
        columns = f.list_fileld(table2)                          #get the table2 fileld name
        fail_list=[]
        temp_fail_list=[]
        # 准备数据模型
        self.sm = QtGui.QStandardItemModel()                     #set the qtable model

        # 设置数据头栏名称
        for i in range(len(columns)):
            self.sm.setHorizontalHeaderItem(i, QtGui.QStandardItem("".join(columns[i])))       #set the head name for the qtable
        #self.sm.setHorizontalHeaderItem(1, QtGui.QStandardItem("NO."))

        # 设置数据条目
        for i in range(len(data)):
            for j in range(len(data[:][i])):
                    #value_type=type(data[i][j])                        get the type
                    if j==1:
                        temp=data[i][j].strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        if j>4:
                            temp=str(data[i][j])            #convert the int & double to str
                        else:
                            temp=data[i][j]
                    if temp=="fail":                                      #get the fail row&coulum index
                        temp_fail_list=[i,j]
                        fail_list.append(temp_fail_list)
                        #self.sm.item(i, j).setBackground(QtGui.QBrush(QtGui.QColor(255, 255, 0)))
                    self.sm.setItem(i, j, QtGui.QStandardItem(temp))                                      #set the each cloumn data
        '''           
        self.sm.setItem(0, 0, QtGui.QStandardItem("张三"))
        self.sm.setItem(0, 1, QtGui.QStandardItem("20120202"))

        self.sm.setItem(1, 0, QtGui.QStandardItem("李四"))
        self.sm.setItem(1, 1, QtGui.QStandardItem("20120203000000000000000"))

        self.sm.setItem(2, 0, QtGui.QStandardItem("李四"))
        self.sm.setItem(2, 1, QtGui.QStandardItem("20120203000000000000000"))

        self.sm.setItem(3, 0, QtGui.QStandardItem("李四"))
        self.sm.setItem(3, 1, QtGui.QStandardItem("20120203000000000000000"))

        self.sm.setItem(4, 0, QtGui.QStandardItem("李四"))
        self.sm.setItem(4, 1, QtGui.QStandardItem("20120203000000000000000"))

        self.sm.setItem(5, 0, QtGui.QStandardItem("李四"))
        self.sm.setItem(5, 1, QtGui.QStandardItem("20120203000000000000000"))
     '''

    # 设置条目颜色和字体
        #self.sm.item(0, 0).setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
        #self.sm.item(0, 0).setFont(QtGui.QFont("Times", 10, QtGui.QFont.Black))
        for i in range(len(fail_list)):
            for j in range(len(data[:][0])):
                self.sm.item(fail_list[i][0],j).setBackground(QtGui.QBrush(QtGui.QColor(255, 255, 0)))              #set the color for the fail item(a row)

    # 按照编号排序
        self.sm.sort(1, QtCore.Qt.DescendingOrder)

    # 将数据模型绑定到QTableView
        self.tableView.setModel(self.sm)

    # QTableView
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #main=My_logon_Main()
    main = MyMain()
    main.show()
    sys.exit(app.exec_())
