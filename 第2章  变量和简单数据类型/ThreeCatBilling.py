num1, num2, num3 = 5, 6, 9
price1, price2, price3 = 8.1, 8.2, 8
fish1, fish2, fish3 = "鲫鱼", "鲤鱼", "草鱼"
date = "2017年12月"
total_num = num1+num2+num3
total_amount = num1*price1+num2*price2+num3*price3
print("-----"*4+"三酷猫记账单"+"-----"*4)
print("钓鱼地点\t钓鱼日期\t鱼名\t数量(条)\t单价(元)")
print("左小河\t"+date+"1日"+"\t"+fish1+"\t"+str(num1)+"\t\t\t"+str(price1))
print("右小河\t"+date+"2日"+"\t"+fish2+"\t"+str(num2)+"\t\t\t"+str(price2))
print("长江\t"+date+"3日"+"\t"+fish3+"\t"+str(num3)+"\t\t\t"+str(price3))
print("-"*52)
print("鱼数总计%d条,市场价格总计%.2f元,每天平均钓鱼数量约%d条(%.2f条)"%(total_num,total_amount,int(total_num/3),total_num/3))
