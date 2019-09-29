# #第一个函数
# # def hello_world():
# #     print("hello  world")
# # hello_world()
#
# #传递参数的函数
# from typing import List, Any
#
#
# def hello(username):
#     print("hello"+username)
# hello('xiaoming')
#
# #username 为形参
# #‘xiaoming’ 为实参  调用函数时传递给函数的信息   使用时，'xiaoming'被传递给了形参 username
#
# def favorite_books(title):
#     print("我最喜欢的一本书是："+title.title())
# favorite_books('alice') #8-2 喜欢的图书
#
#
# #位置实参
#
# def pets(name,kind):
#     print("i have a pet,name's "+name)
#     print("he is a "+kind)
# pets('Tom','dog')
#
# #调用函数多次
# pets('thomas','dog')
# pets('jack','cat')
#
# #关键字实参
#
# pets(name='xiaojie',kind='ji ba')
#
# #默认值
#
# def cats(name,kind='中华田园猫'):
#     print("i have a pet,name's " + name)
#     print("he is a " + kind)
#
# cats('kat')
#
# def make_shirt(size,container):
#     print("你的T-shirt尺码是："+size)
#     print("上面要打印的内容是:"+container)
# make_shirt('xl','我是你爹') #8-3 T-shirt
#
# def make_shirt_2rd(size,container="i love python"):
#     print("一件印有"+container+"的"+size+"T-shirt")
# make_shirt_2rd('大号')
# make_shirt_2rd('中号')
# make_shirt_2rd('任意','其他字') #8-4 T-shirt 2
#
# #返回值
#
# #返回简单值
#
# def get_fullname(first_name,last_name):
#     full_name=first_name+' '+last_name
#     return full_name.title()
# name=get_fullname('jim','brant')
# print(name)
#
#
# #让实参可选
#
# def get_fullname_2(first_name,last_name,middle_name=''):
#     if middle_name:
#         full_name=first_name+' '+middle_name+' '+last_name
#     else:
#         full_name=first_name+' '+last_name
#     return full_name.title()
# name=get_fullname_2('jim','dulk','fuck')
# name1=get_fullname_2('jim','fuck')
# print(name)
#
# #返回字典
#
# # def person_info(first_name,last_name,sex,age):
# #     person={'姓':last_name,'名':first_name,'年龄':age,'性别':sex}
# #     return person
# # persons=person_info('鹏宇','韩','21','男')
# # for first,last in persons.items():
# #     print(first,last)
#
# #结合函数使用while循环
#
# # def person_info(name,sex,age):
# #     person={'姓名':name,'年龄':age,'性别':sex}
# #     return person
# # while True:
# #     name=input("请输入你的姓名：")
# #     age=input("请输入你的年龄：")
# #     sex=input("请输入你的性别")
# #     quit=input("退出请输入'退出',按回车继续输入")
# #     if quit == '退出':
# #         break
# # persons=person_info(name,age,sex)
# # for label,info in persons.items():
# #     print(label)
#
#
# def make_album(singer_name,album_name,song=''):
#     albums={
#         '歌手名':singer_name,
#         '专辑名':album_name,
#         '歌曲数目':song
#     }
#     return albums
# album1=make_album('林俊杰','江南','10')
# album2=make_album('周杰伦','范特西','10')
# album3=make_album('周杰伦','等你下课','1')
# for label,info in album1.items():
#     print(label,info)
# for label,info in album2.items():
#     print(label,info)
# for label,info in album3.items():
#     print(label,info)  #8-7 专辑
#
# #传递列表
#
# def greet_users(names):
#     for name in names:
#         print(name)
# user_lists=['job','bos','jobs']
# greet_users(user_lists)
#
# #函数中修改列表
# #创建两个函数
#
# #打印设计的工作
#
# def print_design(unprinted_design,completed_designs):
#     while unprinted_design:
#         current_printed=unprinted_design.pop()
#         print(current_printed)
#         completed_designs.append(current_printed)
# def show_printed(completed_designs):
#     for completed_design in completed_designs:
#         print(completed_design)
# unprined_design=['2','3','4']
# completed_designs=[]
# print_design(unprined_design,completed_designs)
# show_printed(completed_designs)



# def make_great(magicians,great_magicians):
#     while magicians:
#         magician=magicians.pop()
#         great_magician="the Great "+magician
#         great_magicians.append(great_magician)
# def show_magicians(great_magicians):
#     for a in great_magicians:
#         print(a)
# magicians=['tom','jerry','thomas']
# great_magicians=[]
# make_great(magicians[:],great_magicians)
# show_magicians(great_magicians)
# show_magicians(magicians)  #8-11 魔术师


#传递任意数量的实参

def pizza(*order):
    print(order)

pizza('big','small','cheese')

#结合使用位置实参和任意数量实参

def pizza_hut(size,*toppings):
    print("\nmake a "+str(size)+"-inch pizza,toppings are :")
    for topping in toppings:
        print("-"+topping)

pizza_hut(18,'onion','garlic','cheese','beef','chicken')


#使用任意数量的关键字实参

def user(fullname,**userinfo):
    profile={}
    profile['name']=fullname
    for key , value in userinfo.items():
        profile[key]=value
    return profile
userinfos=user('thomas',sex='male',age=18,location='haerbin')
for key,value in userinfos.items():
    print(str(key)+":"+str(value))


def sandwitchs(*toppings):
    print("食材为：")
    for topping in toppings:
        print(topping)
sandwitchs('onion','garlic','vegetables','sauce') #8-12


def build_profile(firstname,lastname,**userinfo):
    profiles={}
    profiles['firstname']=firstname
    profiles['lastname']=lastname

    for key ,value in userinfo.items():
        profiles[key]=value
    return profiles

introduce=build_profile('pengyu','han',sex='male',age=20,exp='2 years')
for key,value in introduce.items():
    print(key+":"+str(value)) #8-13


def make_car(kind,maker,**info):
    profiles={}
    profiles['制造商']=maker
    profiles['品牌']=kind
    for key , value in info.items():
        profiles[key]=value
    return profiles
car=make_car('subaru','outback',color='blue',tow_package=True)
for key,value in car.items():
    print(key+":"+str(value))  #8-13


