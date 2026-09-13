# a=int(input())
# b=int(input())
# print(a+b,a-b,a/b,a//b,a%b)

score=int(input())
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=60:
    print('C')
elif score<60:
    print('D')

year=int(input())
if (year%4==0 and year%100!=0) or (year%400==0):
    print('闰年')
else:
    print('不是闰年')




