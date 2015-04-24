#使用说明

- `spider.py` 用于下载当前全部教师的个人页面
- `porcess.py` 用于删除其中旧版页面并生成新的页面

产生的新页面基于`htmlgnerator` 模块

#TODO:
- [ ] 改进`style.css`，实现良好的重新排版效果
- [ ] 分解部分代码为函数
- [ ] Be more pythonic
- [ ] 是否能剔除影响排版的空格

  
#Trouble Shooting

- 如果出现profile表信息错误，可能是因为有空的td



**首先使用这个脚本生成全部可以生成的也页面，然后检查他们的正确性，对于不正确的，使用更新网站重新排版**
