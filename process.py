#coding:utf-8
import re
from datetime import datetime
from BeautifulSoup import BeautifulSoup
import os


with open(u'teacher_pages/张志胜.html','r') as f:
    html=f.read()
    soup=BeautifulSoup(html)
    articlebody=soup.find("div",attrs={"class" : "Article_Content"})

    reg = re.compile("<[^>]*>")
    content = reg.sub('',articlebody.prettify())
        #print content

        # while t.nextSibling.string is not None:
        #     print t.nextSibling.string
    with open(u'teacher_pages/张志胜-body.txt','a') as fb:

            # fb.write(articlebody.prettify())
        fb.write(content)
