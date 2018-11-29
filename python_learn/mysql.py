'''
Author ：SunJie
'''
#!/usr/bin/python
#coding=utf8

import cx_Oracle as oracle
from python_learn.tools.xls_tool import Tools


class OraTool:

    def __init__(self, xls, sheet, sql):
        data = Tools(xls, sheet)
        dict = data.get_data()
        self.sql = sql
        self.ipaddr = dict.get('ipaddr')
        self.username = dict.get('username')
        self.password = dict.get('password')
        self.oracle_port = dict.get('oracle_port')
        self.oracle_service = dict.get('oracle_service')

    def oraclesql(self, cursor):
        fp = open(str(self.sql))
        fp_sql = fp.read()
        cursor.execute(fp_sql)
        data = cursor.fetchall()
        return data

    def getdata(self):
        try:
            db = oracle.connect(self.username+"/"+self.password+"@"+self.ipaddr+":"+self.oracle_port+"/"+self.oracle_service)
        except Exception as e:
            print('1',e)
        else:
            cursor = db.cursor()
            data = self.oraclesql(cursor)
            cursor.close()
            db.close()
            return data


if __name__ == '__main__':
    ora = OraTool(xls='data/oracle.xlsx', sheet='test', sql='data/my.sql')
    print(ora.getdata())