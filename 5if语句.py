# cars=['bmw','benz','suziki','toyota','subaru']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())   #例子
#
# for car in cars:
#     if car =='bmw' and car=='suziki':
#         print("you are better")
#     elif car =='benz' or car=='toyota':
#         print("you are best")
#     else:
#         print("you are weak")
# if 'subaru' in cars:
#     print("yes")
# if 'nissan' not in cars:
#     print("no")



current_users=['jone','honr','huawei','sansumg','xiaomi']
new_users=['jobs','renzhengfei','leijun','huawei','xiaomi']
for new_user in new_users:
    if new_user in current_users:
        print(str(new_user)+"请输入其他用户名，这个已经被使用")
    else:
        print(str(new_user)+"可以使用的用户名") #5-10 检查用户名


