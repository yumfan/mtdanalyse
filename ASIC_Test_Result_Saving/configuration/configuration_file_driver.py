import os
import re

current_path = os.path.dirname(__file__)

class configuration():
    def __init__(self):
        self.filename =current_path+"\configuration.ini"

    def open_configuration_file(self):
        f = open(self.filename,'r')
        value=f.read()
        f.close()
        #print(value)
        return value

    def get(self,item,reading):
        result=re.findall(item, reading)
        #print(reading)
        #print(result)
        return result

class read_configuration():
    a=configuration()
    reading=a.open_configuration_file()
    host_name=a.get("host=(.*?)A",reading)                 #匹配两个字符串A与B中间的字符串包：
    host_name=' '.join(host_name)                          #将列表转换成字符串
    user_name=a.get("user=(.*?)A",reading)
    user_name=' '.join(user_name)
    password_value=a.get("password=(.*?)A",reading)
    password_value=' '.join(password_value)
    database=a.get("db=(.*?)A",reading)
    database=' '.join(database)
    #print(host_name)
    #print(user_name)
    #print(password_value)
    #print(database)

