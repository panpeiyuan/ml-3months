password=input("password:pan")
if password=="panpeiyuan":
    print("Welcome")
else:
    print("fail to log in")

#转义字符
#制表符：\t 通常表示空4个字符，也称缩进
print('six\tsixsix')
#\n 换行符
print('hh\nxx')
#\R 回车，表示将当前位置，移到本行开头
print('123\r456')
#\\ 反斜杠符号
print('abc\trfj')
print('abc\\tefj')
print('abc\\\tefj')
print(r'abc\\')
print('abc\\')
a=input()
b=input()
print(a+b,a-b,a/b,a//b,a%b)