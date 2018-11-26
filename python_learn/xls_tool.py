"""
Author ：SunJie
从xls中获取数据：
先找到xls和对应的sheet，返回dict
"""
import xlrd


class Tools:

    def __init__(self, xls, sheetname):
        self.xls = xls
        self.sheetname = sheetname

    def get_data(self):
        data = xlrd.open_workbook(self.xls, 'rb')
        data_sheetname = data.sheet_by_name(self.sheetname)
        temp_dict={}
        for i in range(data_sheetname.ncols):
            temp_dict.setdefault(data_sheetname.row_values(0)[i],data_sheetname.row_values(1)[i])
        return temp_dict


if __name__ == '__main__':
    data = Tools('myword.xlsx', 'test')
    temp = data.get_data()
    print(temp)