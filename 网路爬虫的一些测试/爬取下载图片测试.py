import requests
import os
import re
from bs4 import BeautifulSoup

# 定义一个函数返回查询到的图片数量
def  result_info(html):
    find_form = re.compile(r'<div id="resultInfo">(.*?)</div>', re.S)
    results = re.findall(find_form, html)
    if not results:
        return '没有找到任何东西，请检测'
    else:
        return results[0]

print('-'*25+'本次查找是通过百度特大图查找'+'-'*25)
word = input('请输入你想要找的图片的明星姓名：')
URL = 'http://image.baidu.com/search/index?ct=201326592&z=9&tn=baiduimage&word='+word+'&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=ala&se=&sme=&width=0&height=0'
response = requests.get(URL)
n=response.content.decode(encoding=response.apparent_encoding)

# findrule = re.compile(r'"objURL":"(http://.*?)"')
# picURLfind = re.findall(findrule,str(n))
# print(len(picURLfind))
# for num, item in enumerate(picURLfind):
#     print(num, item)


# n_soup = BeautifulSoup(n,'html.parser')
# n_result = n_soup.find('div',id="resultInfo")
# n=result_info(str(n_result))
print(n)
# findrule = re.compile(r'"objURL":"(.*?.jpg)"')
# picURLfind = re.findall(findrule,str(n_soup))
# print(picURLfind[0])
# picfind = requests.get(picURLfind[17])
# with open("图片17.jpg",'wb') as file:
#     file.write(picfind.content)
#     print('下载成功')




#  定义一个函数来返回下载图片需要的URL
# def picURL(html):
#     findrule = re.compile(r'"objURL":"(.*?.jpg)"')
#     picURLfind = re.findall(findrule,str(html))
#     getpic = requests.get(picURLfind[0])
#     with open(" 方韵的图片.jpg",'wb') as file:
#         file.write(getpic.content)
#         print('下载成功')
#
# picURL(n)



#  定义一个函数来建立文件夹并保存下载的图片






# print(type(response),response.apparent_encoding)


# find_form = re.compile(r'<div id="resultInfo" style="visibility: visible; display: none;">(.*?)</div>')
# results = re.findall(find_form, html)
# print(results[0])

