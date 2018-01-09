#!/usr/bin/python
# -*- encoding:utf-8 -*-
from openpyxl import *

prize_cate = 'The Nobel Prize Physics asnd df  1962'
l_split = len(prize_cate)
pos = prize_cate.find('in')
new_prize_cate = ''
for j in range(pos+3, l_split - 5):
    new_prize_cate += prize_cate[j]
print new_prize_cate

