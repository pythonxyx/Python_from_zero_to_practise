#  利用内建范围函数即range，实现for循环

fish_record = "鲫鱼5条、鲤鱼8条、鲢鱼7条、草鱼2条、黑鱼6条、乌龟1只"
count1 = 0
count2 = 0
for i in range(len(fish_record)):
    if fish_record[i] == "鱼":
        count1 = count1 + int(fish_record[i+1])
        count2 = count2 + 1
print("三酷猫钓上的鱼有%d条，统计鱼%d次，乌龟没有统计！"%(count1,count2))


if "乌龟" in fish_record:
    print("乌龟在字符串里！")
else:
    print("乌龟没有在字符串里面")