# i=1 #定义初始值，记录循环次数
# while i<=100:
#     print("好好学习","天天向上",sep="//",end='11')
#     i+=1
#while循环计算1-100的和
# i=0
# j=0
# while i<100:
#     i+=1
#     j+=i
# print(j)
# s=0
# for i in range(1,101):
#     s+=i
# print(s)

#break和continue只能放在循环内部
#break:条件满足时退出循环
# i=1
# while i<=5:
#     print(f"在吃第{i}个苹果")
#     i+=1
#     if i==3:
#         print("结束")
#         break
#continue：退出本次循环，下一次循环继续执行
i=0
while i<=5:
    i+=1
    if i==3:
        continue #跳过3，结束了i=3的循环，继续下一个循环
    print(f"小明在吃第{i}个苹果")





