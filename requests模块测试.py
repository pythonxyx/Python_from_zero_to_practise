import requests
import re
from bs4 import BeautifulSoup

URL = 'https://www.dytt8.net/'
response = requests.get(URL)
html = response.content.decode('GB2312')
html_soup = BeautifulSoup(html,'html.parser')
html_soup_find = html_soup.find_all('div',class_="co_content8")[0]
# print(html_soup_find[0])
ruler = re.compile(r'<a href="(/html/gndy/dyzz/\d+.*.html)">(.*?)</a><br/>')
item = str(html_soup_find)
find_txt = re.findall(ruler,item)
# print(list(find_txt[0]))

dizhilist = []
namelist = []

for i in range(len(find_txt)):
    new = list(find_txt[i])
    dizhilist.append(new[0])
    namelist.append(new[1])
print(dizhilist)
print(namelist)





# for x,y in enumerate(find_txt):
#     print(str(int(x)+1)+':',y)

# print(html_list)





# print(html_soup)
# print(html)
# print(response.apparent_encoding)