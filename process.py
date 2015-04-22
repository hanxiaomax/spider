#coding:utf-8
import re
from datetime import datetime
from bs4 import BeautifulSoup
import os


with open(u'teacher_pages/张志胜.html','r') as f:
    html=f.read()
    soup=BeautifulSoup(html)

    articlebody=soup.find("div",attrs={"class" : "Article_Content"})

    tables=articlebody.find_all("table")
    for table in tables:
        print table.__class__
        with open(u'teacher_pages/张志胜-body.txt','a') as fb:
            content=unicode(table.get_text()).encode('utf-8')
            fb.write(content)

    # for t in tables:
    #     print t.get_text()
    #     #print content

    #     # while t.nextSibling.string is not None:
    #     #     print t.nextSibling.string
    #     with open(u'teacher_pages/张志胜-body.html','w') as fb:

    #         # fb.write(articlebody.prettify())
    #         fb.write(content)
