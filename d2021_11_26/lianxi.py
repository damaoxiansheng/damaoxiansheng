# a=open(r"D:\pythonzuoye\d2021_11_26\单词.txt","r",encoding="utf-8")
# b=a.readlines()
# import time
# for i in b:
#     time.sleep(1)
#     print(i,end="") 
# a.close



# with open(r"D:\pythonzuoye\d2021_11_26\单词.txt","r",encoding="utf-8") as b:
#     print(b.readlines())


# import json
# # list1=[{"xm":"张云辉","nj":"28","cs":"宣化"},{"xm":"二哥","nj":"22","cs":"大同"}]
# # with open(r"d:\asd.txt","a",encoding="utf-8") as a:
# #     b=json.dump(list1,a)

# with open(r"d:\asd.txt","r",encoding="utf-8") as d:
#     f=json.load(d)


# f.append({'xm': '三哥', 'nj': '12', 'cs': '啊同'})
# print(f)


import xlrd
table = xlrd.open_workbook(r"d:\aaa.xlsx")