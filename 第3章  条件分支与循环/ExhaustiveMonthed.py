#  演示线性查找的方式

fish_record = "鲫鱼5条、鲤鱼8条、鲢鱼7条、草鱼2条、黑鱼6条、乌龟1只"  #  注意发现鱼名出现的规律是0,5,10,15,20,25
print("字符串的长度是：%d个字符"%len(fish_record))
print("-"*50)
i=0
while i < len(fish_record):
    if fish_record[i:i+2] == "乌龟":
        if int(fish_record[i+2])%2 == 0:
            print("乌龟找到了，是%d只，偶数"%int(fish_record[i+2]))
        else:
            print("乌龟找到了，是%d只，奇数"%int(fish_record[i+2]))
    i += 5