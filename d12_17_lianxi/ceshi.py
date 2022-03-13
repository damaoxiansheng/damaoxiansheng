# 导入读取xlsx包
import openpyxl

# 导入封装好的包
from guanjianzi_qudong import guanjianzi_qudong

# 创建一个读取xlsx的对象
excel = openpyxl.load_workbook("ceshi.xlsx")

# 创建一个excel表里sheet1的对象
# sheet = excel["Sheet1"]

# 创建一个字典，后续存放excel的数据
dict1 = {}

# 循环遍历excel表里所有sheet页
for sheets in excel.sheetnames:
    sheet = excel[sheets]

    # 循环遍历excel表里所有的数据
    for i in sheet.values:

        # 去掉第一行title数据
        if type(i[0]) is int:
            # 字典插入三个键名，使值插入对应的键名
            dict1["name"] = i[2]
            dict1["value"] = i[3]
            dict1["txt"] = i[4]

            # 遍历字典，去掉为空的键名
            for j in list(dict1.keys()):
                if dict1[j] is None:
                    del dict1[j]
            print(dict1)

            #
            if i[1] == "dakai_driver":
                guanjianzi_qudong = guanjianzi_qudong(**dict1)
            else:
                getattr(guanjianzi_qudong, i[1])(**dict1)
