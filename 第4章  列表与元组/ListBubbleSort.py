#  冒泡排序法将鱼的数量从小排到大

fish_records = [18,8,7,2,3,6,1,1]
i = 0
cmpare = 0
fish_len = len(fish_records)
while i < fish_len:
    j = 1
    while j < fish_len-i:
        if fish_records[j-1] > fish_records[j]:
            cmpare=fish_records[j-1]
            fish_records[j-1]=fish_records[j]
            fish_records[j]=cmpare
        j+=1
    i+=1
print(fish_records)












# 下面只是一个小测试
# n = "18+8+7+2+3+6+1+1"
# m = n.split("+")
# print(m)
# new_m = []
# for i in range(len(m)):
#     new_m.append(int(m[i]))
# print(new_m)
# print(type(new_m[0]))