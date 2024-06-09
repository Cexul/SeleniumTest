#coding:utf-8
import os.path

import xlrd
from xlutils.copy import copy

class ExcelUtil(object):

    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = '/Users/chenxuliang/PycharmProjects/selenium/config/casedata.xls'
        else:
            self.excel_path = excel_path
        if index ==None:
            index = 0
            # print(excel_path)
        self.data = xlrd.open_workbook(self.excel_path)
        # print(self.data)
        # 表格内容
        self.table = self.data.sheets()[index]
        # [[],[]]

    # 获取Excel数据，每行一个list
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:

            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    def get_lines(self):
        # 拿到表格的行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取单元格数据
    def get_col_value(self,row,col):
        if self.get_lines() > row:

            data = self.table.cell(row,col).value
            return data
        return None


    # 写入数据
    def write_value(self,row,value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.excel_path)

# if __name__ == '__main__':
#     excl = ExcelUtil('/Users/chenxuliang/PycharmProjects/selenium/config/keyword.xls')
#     print(excl.get_col_value(10,1))
