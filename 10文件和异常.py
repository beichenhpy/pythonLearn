with open('F:\pythontest\pi_digits.txt') as file_object:  #open()函数，接受一个要打开文件的名称，在当前执行的文件所在目录寻找指定的文件。 with在不需要访问文件时，将其关闭
    contents=file_object.read() #read()方法，将文件中的字符串保存在变量 contents 中
    print(contents)   #打印会多出一个空行，是因为read()方法，到文件末尾时返回一个空串，要删除，使用rstrip()


print("\n\n\n\n\n")
#逐行读取
filename='pi_digits.txt'

with open(filename) as file:
    for line in file:
        print(line.rstrip())


#为了在with open()外访问，创建一个列表存储读取的信息
#并使用文件内容，存到字符串中

filename = 'pi_digits.txt'
pi_string = ''
with open(filename) as file:
        lines = file.readlines()

for line in lines:
    pi_string += line.strip()
print(pi_string[:12])


lines=''
with open('learning_python.txt') as python:
    line=python.readlines()

    for n in line:
        lines += n.strip()
for l in line:
    print(l)
lines=lines.replace('Python','C')
print(lines)  #10-1 10-2

#写入文件
lin=['you are good\n','you are bad\n']
with open('learning_python.txt','w') as lp:  #打开文件，清空，然后重新写入，不是追加写入  w写入模式
    lp.write('In python you can do any thing\nIn Python you can fxxk your mother\nIn Python you can fxxk yourself\n')
    lp.writelines(lin)

# a 附加模式，不会清空，而是添加到末尾

with open('learning_python.txt','a') as lp_2:
    lp_2.write("\nlife is short , i use python ")

# def visiter_record():
#     inputs=input("请输入姓名：")
#     with open('user_record.txt','a') as user:
#         user.write("\n"+inputs)
# visiter_record()   #10-4 访客

#异常 ZeroDivisionError

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("除零异常")
#
# while True:
#     first = input("输入第一个数")
#     if( first == 'q' ):
#         break
#     second = input("输入第二个数")
#     if( second == 'q' ):
#         break
#     try:
#         result = int(first)/int(second)
#     except ZeroDivisionError:
#         print("除数不能为0")
#     else:
#         print(result)

# FileNotFoundError 异常处理  找不到文件
try:
    with open('不存在的文件.txt') as test:
        content=test.read()
except FileNotFoundError:
    print("找不到文件")
    # pass #不执行任何操作

#分析文本

title="the avangers"
print(title.split())  #split()以空格分割
print(len(title.split()))

# def add():
#     while True:
#         try:
#             first=int(input("输入第一个数"))
#         except ValueError:
#             print("请输入数字")
#         else:
#             try:
#                 second = int(input("输入第二个数"))
#             except ValueError:
#                 print("请输入数字")
#             else:
#                 result=first+second
#                 return result
# print(add())  #10-6

#存储数据

#模块 JSON

import json
number=[2,3,4,5,6]
filename='number.json'
with open(filename,'w') as f_ob:
    json.dump(number,f_ob)

with open(filename) as f_load:
    load=json.load(f_load)

print(load)


# import json
#
# def get_name():
#     filename='username.json'
#     try:
#         with open(filename) as user:
#             username=json.load(user)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
# def get_newname():
#     username=input("请输入你的姓名")
#     filename='username.json'
#     with open(filename,'w') as user:
#         json.dump(username,user)
#     return username
# def greet_user():
#     username=get_name()
#     if username:
#         print("欢迎您 "+username)
#     else:
#         username=get_newname()
#         print("您的信息已经记录")
#
# greet_user()

# import json
# def load_number():
#     filename='userfavoritenumber.json'
#     try:
#         with open(filename) as number1:
#             number = json.load(number1)
#     except FileNotFoundError:
#         return None
#     else:
#         return number
# def get_number():
#     number=input("请输入你喜欢的数字： ")
#     filename='userfavoritenumber.json'
#     with open(filename,'w') as user_number:
#         json.dump(number,user_number)
#     return number
# def show_number():
#     number=load_number()
#     if number:
#         print("i know your favorite number! it's "+number)
#     else:
#         number=get_number()
#         print("已记录")
# show_number()  #10-11喜欢的数字


import json

def get_name():
    filename='username.json'
    try:
        with open(filename) as user:
            username=json.load(user)
    except FileNotFoundError:
        return None
    else:
        return username
def get_newname():
    username=input("请输入你的姓名")
    filename='username.json'
    with open(filename,'w') as user:
        json.dump(username,user)
    return username
def greet_user():
    username=get_name()
    if username:
        judge = input("您的名字是" + username + "吗？")
        if judge=="是":
            print("欢迎您 "+username)
        else:
            username=get_newname()
            print("您的信息已经更新 "+username+"先生")
    else:
        username=get_newname()
        print("您的信息已经记录")

greet_user()  #10-13验证用户