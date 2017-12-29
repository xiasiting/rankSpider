#!/usr/bin/python
# -*- encoding:utf-8 -*-
from openpyxl import *

# 写入excel表格
wb = Workbook()
ws1 = wb.get_sheet_by_name("Sheet")
# 给第一行、第一列赋值，此处不同版本，起始行号可能不同
ws1.cell(row=1, column=2).value = "qwer"

wb.save(filename="empty_book1.xlsx")
# 载入文件
# wb = load_workbook("empty_book1.xlsx")
# # 显示创建文件时自带的文件名称
# print wb.get_sheet_names()
# # 获取名为“Sheet”的工作表
# ws = wb.get_sheet_by_name("Sheet")
# print ws.cell(row=1, column=1).value
# # 遍历ws中的内容
# for a, b, c in ws["A1":"C3"]:
#     print a.value, b.value, c.value
# # 工作表的长、宽
# print len(ws.columns), len(ws.rows)

