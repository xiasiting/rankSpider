# -*- coding:utf-8 -*-
#!/usr/bin/env python
# __auth__ = '无名小妖'
import json
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

with open('items.json') as f:
    rownum = 0
    new_list = json.load(f)
    for i in new_list:
        rownum += 1
        print("""line{}:  title:{},  author:{},  reply:{}.""".format(rownum,
                                                                     i['title'][0],
                                                                     i['author'][0],
                                                                     i['reply'][0]))