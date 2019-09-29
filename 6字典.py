#example1 alien:
current_users=['jone','honr','huawei','sansumg','xiaomi']
aliens={'color':'green','points':4,'user':current_users}  #字典键-值对应-----值可以为任意对象  user就是列表对象
print(aliens)
print(aliens['user'])
# green
# ['jone', 'honr', 'huawei', 'sansumg', 'xiaomi']


#添加键-值

aliens['x-positions']=25
aliens['y-positions']=10
print(aliens)
# {'color': 'green', 'points': 4, 'user': ['jone', 'honr', 'huawei', 'sansumg', 'xiaomi'], 'x-positions': 25, 'y-positions': 10}


#通常先创建一个空字典。

#修改字典中的值
aliens['color']='yellow'
print(aliens['color'])
# yellow


print("初始坐标为："+str(aliens['x-positions']))
aliens['speed']='medium'
if aliens['speed']=='slow':
    x_increment=1
elif aliens['speed']=='medium':
    x_increment=2
else:
    x_increment=3
aliens['x-positions']=aliens['x-positions']+x_increment
print("新的坐标为："+str(aliens['x-positions']))
# 初始坐标为：25
# 新的坐标为：27

#删除键-值

del aliens['user']
print(aliens)
# {'color': 'yellow', 'points': 4, 'x-positions': 27, 'y-positions': 10, 'speed': 'medium'}

zhongxiaomiao={
    '姓名':'钟小淼',
    '年龄':'22',
    '居住城市':'哈尔滨'
}
print(zhongxiaomiao)#6-1 人

#遍历字典

for option,information in zhongxiaomiao.items():  #items()方法包含键和值
    print("\n"+option+":"+information)

for option in zhongxiaomiao.keys():  #key()包含键  默认是遍历键-->for option in zhongxiaomiao
    print("\n"+option)

for information in zhongxiaomiao.values():  #values()包含值
    print("\n"+information)


favorite_languages={
    'xiaoming':'Ruby',
    'xiaogui':'python',
    'xiaotou':'C#',
    'xiaohuo':'C',
    'xiaojia':'java'
}
mans=['xiaoming','xiaogui','xiaoli','xiaotou','xiaoxue']
for man in mans:
    if man in favorite_languages.keys():
        print(man+"感谢参与调查")
    else:
        print(man+"请参与调查") #6-6


# alien_0={'color':'green','points':4}
# alien_1={'color':'blue','points':5}
# alien_2={'color':'white','points':2}
#
# aliens=[alien_0,alien_1,alien_2]
#
# for alien in aliens:
#     print(alien)


aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':4}
    aliens.append(new_alien)
for alien in aliens:
    print(alien)
print("总共外星人数："+str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']='6'
for alien in aliens[0:5]:
    print(alien)


favorite_languages={
    'xiaoming':['Ruby','C'],
    'xiaogui':['python','java'],
    'xiaotou':['C#'],
    'xiaohuo':['C'],
    'xiaojia':['java']
}
for names,languages in favorite_languages.items():
    if len(languages)>1:
        print(names.title()+"favorite langueges are")
        for language in languages:
            print(language)
    else:
        print(names.title()+"favorite langueges is  ")
        for language in languages:
            print(language)


many_users={
   'zhongxiaomiao':{
       'first':'xiaomiao',
       'last':'zhong',
       'local':'haerbin'
   },
    'hanpengyu':{
        'first':'pengyu',
        'last':'han',
        'local':'haerbin'
    }
}
for username,userinfo in many_users.items():
    print("username:"+username)
    fullname=userinfo['first']+userinfo['last']
    location=userinfo['local']
    print("username:"+fullname)
    print("userinfo:"+location)