# username=input("请输入用户名:")
# password=input("请输入密码:")
# print(username+"\n"+password)

# height=input("请输入你的身高：")
# height=int(height)  #int()转换成数值类型
# if height>=160:
#     print("发育良好")
# else:
#     print("发育一般")

#求模运算符：%

# question=input("请输入一个数，系统将会告诉你是奇数还是偶数：")
# question=int(question)
# if question %2==0:
#     print(str(question)+"是偶数")
# else:
#     print(str(question)+"是奇数")

# dingdan=input("请问有多少人要订餐呢？")
# dingdan=int(dingdan)
# if dingdan > 8:
#     print("对不起，没有空桌了")
# else:
#     print("还有空桌可以进行订餐") #7-2餐馆订位置


#while 循环


#用户何时退出

# prompt="在键盘上输入'quit'就可以退出了"
# m=""
# while m != "quit":
#     m=input(prompt)
#     if m != "quit":
#         print(m)
# if m=="quit":
#     print("good boy")

#添加标志位来循环
# prompt="在键盘上输入'quit'就可以退出了"
# flag=True
# while flag:
#     m=input(prompt)
#     if m != "quit":
#         print(m)
#     else:
#         flag=False
#         print("good bye")



#使用 break 退出循环

# prompt="在键盘上输入'quit'就可以退出了"
# flag=True
# while flag:
#     m=input(prompt)
#     if m != "quit":
#         print(m)
#     else:
#         break

#在循环中使用 continue

#打印 1-50 中的 奇数

# for number in range(1,51):
#     if number % 2==0:
#         continue
#     else:
#         print(number)

# number=0
# while number <50:
#     number=number+1
#     if number % 2 == 0:
#         continue
#     else:
#         print(number)


#避免无限循环：


# pizza="请添加你想要吃的pizza配料："
# pizza+="\n输入'quit'退出"
#
# flag=True
# while flag:
#     m=input(pizza)
#     if m=="quit":
#         break
#     else:
#         print("我们将会添加您的选择的配料： "+m) #7-4比萨配料


# flag=True
# while flag:
#     age=input("请输入年龄，我将告诉你票价！")
#     age=int(age)
#     if age <3 and age>0:
#         print("免费票")
#     elif age>=3 and age<=12:
#         print("你的孩子今年"+str(age)+"岁了，你需要支付10美元")
#     elif age>12 and age<=120:
#         print("你的孩子今年"+str(age)+"岁了，你需要支付15美元")
#     else:
#         print("请输入正确的年龄，谢谢合作！")  #7-5 电影院门票

# while 1==1:
#     print("you are bad boy")  #7-7 无限循环


#使用 while 来修改列表

# user1=['xiaoming','xiaohong','xiaoli']
# user2=[]
# while user1:
#     user=user1.pop()
#     print(user)
#     user2.append(user)
# for user3 in user2:
#     print(user3)



#删除包含特定值的所有列表元素

# hack_current_view=['xiaoming','xiaohai','xiaoming','xiaohei','xiaoli','xiaoli','xiaoming']
# while "xiaoming" in hack_current_view:
#     hack_current_view.remove('xiaoming')
# print(hack_current_view)

#用用户输入填充字典
# response={}
# flag=True
# while flag:
#     name=input("请说出你的姓名:")
#     actor=input("请说出你喜欢的av女优:")
#
#     response[name]=actor
#
#     goon=input("\n是否继续回答:\n")
#     if goon == "否":
#         flag=False
# for name,actor in response.items():
#     print(name+"最喜欢"+actor)


# sandwich_orders=['tuna sandwich','chicken sandwich','pork sandwich','beef sandwich']
# finished_sandwiches=[]
# for sandwich_order in sandwich_orders:
#         print("i made your"+sandwich_order)
# while sandwich_orders:
#     finished_sandwich=sandwich_orders.pop()
#     finished_sandwiches.append(finished_sandwich)
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)  #7-8熟食店

# sandwich_orders=['tuna sandwich','chicken sandwich','pork sandwich','pastrami','pastrami','pastrami']
# finished_sandwiches=[]
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# for sandwich_order in sandwich_orders:
#         print("i made your"+sandwich_order)
# while sandwich_orders:
#     finished_sandwich=sandwich_orders.pop()
#     finished_sandwiches.append(finished_sandwich)
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)   #7-9 pastrami 卖完了

# response={}
# flag=True
# while flag:
#     name=input("你的姓名是？")
#     position=input("你最想去哪度假？")
#
#     response[name]=position
#     judegment=input("其他人是否继续回答")
#     if judegment == "否":
#         flag=False
# for name,position in response.items():
#     print(name+"最想去的地方是"+position)  #7-10度假圣地

