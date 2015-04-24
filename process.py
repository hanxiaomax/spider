#coding:utf-8
import re
from datetime import datetime
from bs4 import BeautifulSoup
import os
from glob import glob
from htmlgenerator import Generator
from pyh import *
#profile table 错位可能是有空白的td，删除后重新运行
#TODO: 对所有的页面，防止td内部标签打断。
#TODO: 论文排版
#FIXME:对于没有按规则排版页面，重新生成的页面也是乱的
files=glob(u'teacher_pages/*-output.html')
print u"清理旧的output文件...."
for _file in files:
    os.remove(_file)
print u"完成！"

#首先删除全部旧版文件
print u"分析并清除旧版页面...."
files=glob(u'teacher_pages/*.html')
for _file in files:
    f=open(_file,'r')
    html=f.read()
    soup=BeautifulSoup(html)
    articlebody=soup.find("div",attrs={"class" : "Article_Content"})

    tables=articlebody.find_all("table")

    filename=os.path.basename(_file).split(".")[0]
    #print tables[0].get_text(":",strip=True).split(':')
    if u"序号" in tables[0].get_text("#",strip=True).split('#'):
        print os.path.basename(_file)+u"为旧版文件\t\t删除"
        f.close()
        os.remove(_file)
    elif u"近期部分科研成果"  in tables[1].get_text("#",strip=True).split('#'):

        print os.path.basename(_file)+u"为旧版文件\t\t删除"
        f.close()
        os.remove(_file)
    elif u"个人简介"  in tables[1].get_text("#",strip=True).split('#'):

        print os.path.basename(_file)+u"为旧版文件\t\t删除"
        f.close()
        os.remove(_file)


print u"准备生成新页面.."
os.system('pause')
#依次处理新版页面
files=glob(u'teacher_pages/*.html')
for _file in files:
    filename=os.path.basename(_file).split(".")[0]
    print filename,
    with open(_file,'r') as f:
        page = PyH('My wonderful PyH page')
        page.addStyleSnippet("style.css")
        # page.addStyleSnippet('style.css') ＃或者可以把style.css中的代码插入html中
        g=Generator()#表格生成器
        _list=[]
        subtitles1=[u"项目名称",u"项目类别",u"项目时间",u"工作类别",u"项目金额"]
        subtitles2=[u"专利号",u"专利名称",u"专利类型"]


        html=f.read()
        soup=BeautifulSoup(html)

        articlebody=soup.find("div",attrs={"class" : "Article_Content"})

        tables=articlebody.find_all("table")


        for i in range(0,len(tables)):
            #fb.write(unicode(tables[i].prettify()).encode("utf-8"))
            #处理 profile table
            if i==0:
                _list=[]
                table=tables[0]
                trs=table.find_all('tr')
                for tr in trs:
                    #获取行内字符串用：分割，再用：分割成为列表
                    content=tr.get_text(":",strip=True).split(':')

                    if len(content)<2:#去掉空行或没有填写信息的行
                        pass
                    else:
                        _list.append((content[0],content[1]))
                #生成重新排版的 profile table
                page<<g.makeprofile(_list)

            #处理其他表格（每个人可能不一样
            else:
                table=tables[i]
                trs=table.find_all('tr')#获取表中全部列，其中trs[0]为标题,trs[1]需要判断是内容还是副标题

                title=trs[0].get_text("\n",strip=True)#获取表头

                if title == u"科研项目":#有副标题处理副标题
                    _trinfo=[]#存放一个表格中各列的数据
                    for i in range(2,len(trs)):
                        _tdinfo=[]#存放一行中各列的数据
                        tds=trs[i].find_all("td")
                        for td in tds:#进入到td层，否则会产生过多的碎片
                            info=td.get_text("#",strip=True).split('#')#以td层为单位分割成list
                            info="".join(info)#把list连接为字符串，这个字符串就是一个td中的纯文本内容
                            _tdinfo.append(info)#字符串加入列表
                        _trinfo.append(_tdinfo)
                    page<<g.makeTableWithSub(title,subtitles1,_trinfo)

                elif title == u"专利":
                    _trinfo=[]
                    for i in range(2,len(trs)):
                        _tdinfo=[]
                        tds=trs[i].find_all("td")
                        for td in tds:
                            info=td.get_text("#",strip=True).split('#')
                            info="".join(info)
                            _tdinfo.append(info)
                        _trinfo.append(_tdinfo)
                    page<<g.makeTableWithSub(title,subtitles2,_trinfo)

                else:
                    _trinfo=[]
                    for i in range(1,len(trs)):
                        _trinfo.append(trs[i].get_text(strip=True))
                    page<<g.makeTable(title,_trinfo)


        page.printOut(u'teacher_pages/'+filename+'-output.html')
        print u"\t成功"


