import os
import os.path
import time
import datetime

import pandas as pd
import sys


# 根据测试路径列举出芯片
from numpy import unicode
from pandas.tests.scalar import timestamp


def list_chip_paths(sys_path):
    each_chip_lists = []
    chip_sn_lists = []
    if os.path.exists(sys_path):
        chip_path_lists = os.listdir(sys_path)
        for each_chip in chip_path_lists:
            each_path = os.path.join(sys_path, each_chip)

            # 判断当前的路径是否是文件夹且判断是否为空（或者根据文件数量初步筛选测试结果）
            if os.path.isdir(each_path) and len(os.listdir(each_path)):
                each_chip_lists.append(each_path)
                chip_sn_lists.append(each_path.split('\\')[-1])
        return each_chip_lists
    else:
        raise FileExistsError

def list_sn(sys_path):
    each_chip_lists = []
    chip_sn_lists = []
    if os.path.exists(sys_path):
        chip_path_lists = os.listdir(sys_path)
        for each_chip in chip_path_lists:
            each_path = os.path.join(sys_path, each_chip)

            # 判断当前的路径是否是文件夹且判断是否为空（或者根据文件数量初步筛选测试结果）
            if os.path.isdir(each_path) and len(os.listdir(each_path)):
                each_chip_lists.append(each_path)
                chip_sn_lists.append(each_path.split('\\')[-1])
        return chip_sn_lists
    else:
        raise FileExistsError







# 如果当前路径下有多个.xl1文件,获取最新的那一个
def get_latest_file(item_path):
    file_path_lists = []
    files_c_time = []
    for __ in os.listdir(item_path):
        if os.path.splitext(__)[1] == '.xl1':
            current_file_path = os.path.join(item_path, __)
            file_path_lists.append(current_file_path)
            files_c_time.append(os.path.getctime(current_file_path))

            return file_path_lists[files_c_time.index(max(files_c_time))]


#   单芯片测试项解析
def test_items_parsing(chip_path):
    test_items_paths = []
    for _ in os.listdir(chip_path):
        item_path = os.path.join(chip_path, _)
        if os.path.isdir(item_path):
            test_items_paths.append(get_latest_file(item_path))

    # 记录每个测试项具体路径的列表
    return test_items_paths


def parsing_xl1(item_path,chip_name,test_time):
    # single_item_data用于存放芯片测试数据, 两个列表用于存放测试名称和测试结果
    single_item_data = pd.DataFrame()



    with open(item_path) as f:
        tmp_dict, count = {}, 0
        for each_line in f:
            count += 1
            tmp_dict[count] = each_line.split('\t')
            single_item_data = pd.DataFrame(tmp_dict).transpose()

    # 测试文件case形状 (rows * cols)
    file_shape = single_item_data.shape
    test_final_all=[]
    for row in range(1, file_shape[0]):
        if single_item_data.iloc[row, 0] == "TestSettingsData":   #find the data row

            #   临时存放测试数据和测试状态
            temp_data_info = []
            temp_status_info = []
            test_info_all = []
            test_info_data = []
            test_info_status = []

            for col in range(6, 14, 2):              #from the specmin1 to specmax4
                if single_item_data.iloc[row, col] != 'Na':                      #confirm the specmin1 !=0
                    temp_data_info.append(single_item_data.iloc[row + 2, col - 5])  #find the status1
                    temp_status_info.append(single_item_data.iloc[row + 2, col - 4]) #find the Result1
            test_info_data.extend(temp_data_info)
            test_info_status.extend(temp_status_info)
    #取出整行测试条件及spec，插入测试数据和结果到同一个list
            for col in range(2, 14):
                if col != 5:
                    test_info_all.append(single_item_data.iloc[row, col])        #take test condition raw

            if len(test_info_data)==1:
                test_info_all.insert(4, test_info_data)
                test_info_all.insert(7, "Na")
                test_info_all.insert(10, "Na")
                test_info_all.insert(13, "Na")
            else:
                if len(test_info_data) == 2:
                    test_info_all.insert(4,test_info_data[0])
                    test_info_all.insert(7,test_info_data[1])
                    test_info_all.insert(10, "Na")
                    test_info_all.insert(13, "Na")
                else:
                    if len(test_info_data) == 3:
                        test_info_all.insert(4, test_info_data[0])
                        test_info_all.insert(7, test_info_data[1])
                        test_info_all.insert(10, test_info_data[2])
                        test_info_all.insert(13, "Na")
                    else:
                        if len(test_info_data) == 4:
                            test_info_all.insert(4, test_info_data[0])
                            test_info_all.insert(7, test_info_data[1])
                            test_info_all.insert(10, test_info_data[2])
                            test_info_all.insert(13, test_info_data[3])
            test_info_all.insert(4, test_info_status[0])                #insert single case test status to a row
            test_info_all.insert(0, chip_name)                          #insert SN to a row
            test_info_all.insert(1, test_time)                          #insert test time to a row
            test_final_all.append(test_info_all)                        #append a row data to a row arrary
    '''
    for i in range(4):
        if i == 0:
            test_info_all.insert(4,test_info_data[0])
        if i == 1:
            test_info_all.insert(7, test_info_data[1])
        if i == 2:
            test_info_all.insert(10, test_info_data[2])
        if i == 3:
            test_info_all.insert(13, test_info_data[3])
    '''
    #test_info_all.insert(len(test_info_all),test_info_status[0])
    #test_info_all.insert(0,chip_name)
    #test_info_all.insert(1,test_time)
    return test_final_all
    #return [test_info_data, test_info_status]




def save_excel(each_chip):
    pd_data = pd.DataFrame(pd.read_excel(r"E:\MC05\Demo.xlsx"))
    top_path = r"E:\MC05"
    count = 1
    for each_chip in list_chip_paths(top_path):
        one_chip_info = []
        one_chip_data = []
        one_chip_status = []
        chip_name = os.path.split(each_chip)[1]

        for each_file in test_items_parsing(each_chip):
            one_chip_info.append(parsing_xl1(each_file))
        for each in one_chip_info:
            one_chip_data.extend(each[0])
            one_chip_status.extend(each[1])
        if len(one_chip_data) != 88:
            continue
        else:
            if 'fail' in one_chip_status:
                one_chip_data.insert(0, " ")
                one_chip_data.insert(0, "Fail")
            else:
                one_chip_data.insert(0, " ")
                one_chip_data.insert(0, "Pass")
            pd_data[chip_name] = one_chip_data
        print("File finished ----{}".format(count))
        count += 1
    pd_data.to_excel("E:/MC05/temp_result.xlsx")
'''
if __name__ == "__main__":
    main()
'''

def list_chip_sn_time(sys_path):
    each_folder = list_chip_paths(sys_path)
    chip_sn_lists=list_sn(sys_path)
    list_sn_time = []
    for i in range(len(each_folder)):
        list_sn_time.append(chip_sn_lists[i] + "," + get_FileCreateTime(each_folder[i]))
        #print(list_sn_time[i])
        #print(type(list_sn_time[i]))
    print(list_sn_time)
    return list_sn_time

'''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
def TimeStampToTime(timestamp):
       timeStruct = time.localtime(timestamp)
       #print(timeStruct)
       return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

'''获取文件的创建时间'''
def get_FileCreateTime(filePath):
    #filePath = unicode(filePath,'utf8')
    #filePath=filePath
    t = os.path.getctime(filePath)
    #print(t)
    return TimeStampToTime(t)

'''获取文件的修改时间'''
def get_FileModifyTime(filePath):
    #filePath = unicode(filePath,'utf8')
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)

'''获取文件的访问时间'''
def get_FileAccessTime(filePath):
    #filePath = unicode(filePath,'utf8')
    t = os.path.getatime(filePath)
    return TimeStampToTime(t)


'''获取文件的大小,结果保留两位小数，单位为MB'''
def get_FileSize(filePath):
    filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,2)

def each_chip_test_result(each_chip,chip_name):
        one_chip_info = []
        test_time=get_FileCreateTime(each_chip)
        for each_file in test_items_parsing(each_chip):
            one_chip_info.append(parsing_xl1(each_file,chip_name,test_time))
        return one_chip_info


def summary_one_chip_data(one_chip_data):
    one_chip_test_status="pass"
    for i in range(len(one_chip_data[:])):
        for j in range(len(one_chip_data[:][i])):
            for k in range(len(one_chip_data[:][i][j])):
                temp = one_chip_data[:][i][j][k]
                if(one_chip_data[:][i][j][k]=="fail"):
                    one_chip_test_status="fail"
    return one_chip_test_status
    '''
    for i in one_chip_data:
        if (isinstance(i, list)):
            summary_one_chip_data(i)
        else:
            #print(i)
            if (i=="fail"):
                one_chip_test_status = "fail"
    '''





