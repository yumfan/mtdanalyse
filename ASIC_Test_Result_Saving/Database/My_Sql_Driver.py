import pymysql
import os
import sys
from configuration.configuration_file_driver import read_configuration


class database_operation():
        def __init__(self):
                self
        def connect_database(self):
                a=read_configuration()
                host='127.0.0.1'
                user='root'
                password='123456'
                database='mc05_test_result'
                #conn = pymysql.connect(host=host, user=user,passwd=password, db=database)
                conn = pymysql.connect(host=a.host_name, user=a.user_name,passwd=a.password_value, db=a.database)
                #print(read_configuration.host_name)
                return conn



        def query_database(self,command):
                result_temp=[]
                connection=self.connect_database()
                cur = connection.cursor()
                cur.execute(command)
                #for r in cur:
                #print(connection)
                result=cur.fetchall() # 获取所有的数据
                #for (row,) in result:
                        #result_temp.append(row)
                #for test_result in result:
                        #test_result.append(test_result)
                #print(result)
                cur.close()
                connection.close()
                return result


        def insert_data(self,table,column,data):
                connection=self.connect_database()
                cur = connection.cursor()
                command= "INSERT IGNORE INTO " + table +" " + column + " VALUES " + data   #ingore dup key
                #print(command)
                cur.execute(command)
                #        print(r)

                cur.connection.commit()
                cur.close()
                connection.close()

        def list_col(self,table):
                connection = self.connect_database()
                cur = connection.cursor()
                cur.execute("select * from %s" % table)
                col_name_list = [tuple[0] for tuple in cur.description]
                connection.close()
                col_name=','.join(col_name_list)
                col_name="(" + col_name +")"
                #print(col_name)
                return col_name

        def list_fileld(self,table):
                connection = self.connect_database()
                cur = connection.cursor()
                cur.execute("select * from %s" % table)
                fileld_list = [tuple[0] for tuple in cur.description]
                connection.close()
                return fileld_list


