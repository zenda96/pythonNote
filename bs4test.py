#-*- coding:utf-8 -*-

from urllib import request
from urllib import error
import re


class Tool:
    '''工具类'''
    removeImg = re.compile('<img.*?>| {7}')
    removeA = re.compile('<a.*?>|</a>')
    replaceLine=re.compile('<tr>|<div>|</div>|<p>')
    replaceTd = re.compile('<td>')
    replacePara =re.compile('<p.*?>')
    replaceBr = re.compile('<br><br>|<br>')
    removeTag = re.compile('<.*?>')
    def replace(self,x):
        x=re.sub(self.removeImg,"",x)
        x=re.sub(self.removeA,"",x)
        x=re.sub(self.replaceLine,"\n",x)
        x=re.sub(self.replaceTd,"\t",x)
        x=re.sub(self.replacePara,"\n",x)
        x=re.sub(self.replaceBr,"\n",x)
        x=re.sub(self.removeTag,"",x)
        return x.strip()
class BDTB:
    '''百度贴吧爬虫'''
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()
        self.floor=1
        self.file=None
        self.defaultTitle='百度贴吧'

    #传入页码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+self.seeLZ+'&pn='+str(pageNum)
            req = request.Request(url)
            rep = request.urlopen(req)
            # with open('a.txt','w') as f:
            #     f.write(rep.read().decode('utf-8'))
            return (rep.read().decode('utf-8'))
        except error.HTTPError as e:
            print('链接失败，原因:',e)
    #获取帖子标题
    def getTitle(self,page):
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
    #获取帖子页数
    def getPageNum(self,page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            # print(result.group(1).strip())
            return result.group(1).strip()
        else:
            return None
    #获取每层楼的帖子内容
    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents=[]
        for item in items:
            content = "\n"+self.tool.replace(item)+"\n"
            contents.append(content)
        return contents
    def setFileTitle(self,title):
        if title is not None:
            self.file =open(title+'.txt','w+')
        else:
            self.file = open(self.defaultTitle+'.txt','w+')
    def writeData(self,contents):
        for item in contents:
            self.file.write('\n-------------第'+str(self.floor)+'楼-------------------------\n')
            self.file.write(item)
            self.floor +=1
    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title=self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum ==None:
            print('链接已失效')
            return
        try:
            print("共"+str(pageNum)+"页")
            for i in range(1,int(pageNum)+1):
                print("正在写入"+str(i))
                page = self.getPage(i)
                contents=self.getContent(page)
                self.writeData(contents)
        except IOError as e:
            print("写入异常"+e)
        finally:
            print("写入完成")



baseURL = 'http://tieba.baidu.com/p/4931959529'
bdtb = BDTB(baseURL,1)
bdtb.start()



