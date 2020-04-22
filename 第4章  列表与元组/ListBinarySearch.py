# 利用二分查找法来查找相关数据
import re


text = '1月1日，鲫鱼，18,10.5,1月1日，鲤鱼，8,6.2,1月1日，鲢鱼，7,4.7,1月2日，草鱼，2,7.2,1月2日，鲫鱼，3,12,' \
       '1月2日，黑鱼，6,15,1月3日，乌龟，1,71,1月3日，鲫鱼，1,9.8'
fish_records = re.split(',|，',text)
flag=2
while flag <len(fish_records):
    fish_records[flag]=int(fish_records[flag])
    fish_records[flag+1]=float(fish_records[flag+1])
    flag += 4
#  上面是自找麻烦，不想输入过多的单引号造成的。


stat_list = ['1月1日','',0,0]
j = 0
while j<len(fish_records):
    get_list=fish_records[j:j+4]
    if get_list[0] == stat_list[0]:
        if get_list[2]%2 == 0:
            stat_list[2] += get_list[2]
        print(get_list)
    else:
        print('%s,偶数累计为%d'%(stat_list[0],stat_list[2]))
        stat_list=get_list
        print(get_list)
        stat_list[1]=''
        if get_list[2]%2 != 0:
            stat_list[2] = 0
    j+=4
print('%s,偶数累计为%d'%(stat_list[0],stat_list[2]))

