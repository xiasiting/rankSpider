#!/usr/bin/python
# -*- encoding:utf-8 -*-

'''
源网址：http://hz.house.ifeng.com/detail/2014_10_28/50087618_1.shtml
项目来源：https://www.zhihu.com/question/26385408
时间：2016-05-19
'''
# pip install requests
# Successfully installed certifi-2017.11.5 chardet-3.0.4 requests-2.18.4 urllib3-1.22

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
'''
我想去掉面积中的那个㎡，可是报了
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe3 in position 0: ordinal not in range(128)
这个错误，所以就加上了下面三句，解决
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_info():
    xuhao=[]
    project_name=[]
    project_strict=[]
    project_sale_num=[]
    project_order_num=[]
    project_sale_area=[]
    project_ave_price=[]

    baseurl='http://hz.house.ifeng.com/detail/2014_10_28/50087618_'

    page_num=1
    url=baseurl+str(page_num)+'.shtml'
    response=requests.get(url)
    response.encoding = 'utf-8' #将requests强制编码为utf_8
    # print response.encoding   查看requests的编码方式

    soup=BeautifulSoup(response.text,'lxml')
    arcicle=soup.find('div',{'class':'article'})
    tr=arcicle.find_all('tr')
    for i in range(2,len(tr)-1):
        td=tr[i].find_all('td')

        xuhao.append(td[0].string.strip())
        project_name.append(td[1].string.strip())
        project_strict.append(td[2].string.strip())
        project_sale_num.append(td[3].string.strip())
        project_order_num.append(td[4].string.strip())
        project_sale_area.append(td[5].string.replace('㎡','').strip())
        project_ave_price.append(td[6].string.strip())

    df=DataFrame(xuhao,columns=['xuhao'])
    df['name']=DataFrame(project_name)
    df['strict']=DataFrame(project_strict)
    df['sale_num']=DataFrame(project_sale_num)
    df['order_num']=DataFrame(project_order_num)
    df['area']=DataFrame(project_sale_area)
    df['ave_price']=DataFrame(project_ave_price)
    return df


if __name__=='__main__':

    page=get_info()
    print page