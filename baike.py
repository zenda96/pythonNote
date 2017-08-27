# -*- coding: utf-8 -*-

import re

import requests
import xlwt
from bs4 import BeautifulSoup



wbk = xlwt.Workbook()
sheet1 = wbk.add_sheet('豆瓣TOP250', cell_overwrite_ok=True)

def set_style(bold):
    style = xlwt.XFStyle()
    return style

style = xlwt.easyxf('pattern: pattern solid, fore_colour ice_blue; font: bold on;')
sheet1.write(0, 0, '电影名', style)
sheet1.write(0, 1, '年份/国家/标签', style)
sheet1.write(0, 2, '评分', style)
sheet1.write(0, 3, '评价数', style)
sheet1.col(0).width = 8000
sheet1.col(1).width = 12000
class spider(object):
    def __init__(self):
        self.page = 0
        self.curURL="http://movie.douban.com/top250"
        print("开始...")
    def getAndWrite(self,page):
        print(self.curURL)
        r = requests.get(self.curURL)
        soup = BeautifulSoup(r.text, 'html.parser').find(id="content")
        hds = soup.find_all('div', {'class': 'hd'})
        bds = soup.find_all('div', {'class': 'bd'})

        num = (self.page+1)*25
        print(num)
        self.curURL="http://movie.douban.com/top250?start=%d&filter=&type=" %num

        colNum = 1+25*page
        for hd in hds:
            sheet1.write(colNum, 0, hd.find('span', class_='title').get_text())
            colNum += 1

        colNum2 = 1+25*page
        for bd in bds:
            textTemp = bd.find('p').get_text()
            pattern = re.compile(r'\d{4}.*')
            sheet1.write(colNum2, 1, pattern.findall(textTemp))
            colNum2 += 1

        colNum3 = 1+25*page
        for bd in bds:
            sheet1.write(colNum3, 2, bd.find('span', class_='rating_num').get_text())
            colNum3 += 1

        colNum4 = 1+25*page
        for bd in bds:
            sheet1.write(colNum4, 3, bd.find(text=re.compile('评价'))[:-3])
            colNum4 += 1
    def circle(self):
        while self.page <4:
            self.getAndWrite(self.page)
            self.page +=1

def main():
    print("准备...")
    myspider = spider()
    myspider.circle()

if __name__ =='__main__':
    main()

wbk.save('douban.xls')
print('ok')
