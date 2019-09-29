cats=['狸花猫','橘猫','美国短毛猫','英国短毛猫']
for cat in cats:
    print(cat+"是猫")
print("希望各位能得到属于自己的猫猫\n")#列表简单操作


for value in range(1,5):
    print(value)

number = list(range(1,5))
print(number) #利用list将数字转换成数字列表

step =list(range(1,22,5))
print(step)

squre=[]
for value in range(1,22,5):#1,6,11,16,21
    squre.append(value**2)
print(squre)
print(max(squre))
print(min(squre))
print(sum(squre))

exp_20=list(range(1,21))  #4-3数列20
print(exp_20)

list_100W=[]
for value in range(1,1000001):
    list_100W.append(value)
# print(list_100W) #4-4一百万
print(min(list_100W))
print(max(list_100W))
print(sum(list_100W))  #4-5计算1-100W总和

jishu=[value for value in range(1,20,2)]
print(jishu) #1-20的奇数

three_times=[]
for value in range(3,31):
    if value%3==0:
        three_times.append(value)
print(three_times) #4-7 3的倍数


sum_time=[]
for value in range(1,11):
    sum_time.append(value**3)
print(sum_time) #4-8 立方

sum_times=[value**3 for value in range(1,11)]
print(sum_times)  #4-9 立方解析


#列表的切片

print("我最喜欢的猫是：")
print(cats[0:3])

#复制列表

my_favorite_cat=cats[:]
my_favorite_cat.append('缅因猫')
cats.append('豹猫')
for mycat in my_favorite_cat:
    print(mycat)
for cat in cats:
    print(cat)

#元组：不可更改的列表

sex=('male','female')
# sex[0]='middle' #不能被修改
print(sex[0])

#遍历

sex=('male','female')
for s in sex:
    print(s)

#修改元组变量：虽然不能修改元组的值，但可以重新定义整个元组

menu=('宫保鸡丁','地三鲜','锅包肉','鱼香肉丝','软炸里脊')
for food in menu:
    print(food)
print("\n")
menu=('宫保鸡丁','地三鲜','锅包肉','鱼香茄子','香煎小黄鱼')
for food in menu:
    print(food) #4-13自助餐




