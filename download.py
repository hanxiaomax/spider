#coding:utf-8
import urllib2
import re
from datetime import datetime
from bs4 import BeautifulSoup
import os
#首先访问教师列表页
response = urllib2.urlopen('http://me.seu.edu.cn/test_12331/list.htm')

try:
    html=response.read()
    soup = BeautifulSoup(html)#创建搜索对象
    #创建文件夹
    dirname="teacher_pages"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    #使用正则表达式去找到5个tab标签
    for targetd_tab in soup.find_all('div',attrs={"id" : re.compile("tab[1-5]")}):
        print "---------------"
        #依次获取标签中的<a>
        for i ,a in enumerate(targetd_tab.find_all('a')):
            start=datetime.now()
            print i,a.string,a["href"]
            req=urllib2.urlopen(a["href"].replace("htm","psp"))#替换超链接地址htm为psp：不知道为什么htm无法访问
            teacher_page=req.read()
            #保存该页面

            with open("teacher_pages/"+a.string.strip(" ")+".html","w") as f:
                bs=BeautifulSoup(teacher_page)#创建beautifulsoup对象
                f.write(unicode(bs.prettify()).encode('utf-8'))

            end=datetime.now()
            print u"耗时:%d ms"%((end-start).microseconds/1000.0)

except urllib2.URLError,e:
    print e.reason

