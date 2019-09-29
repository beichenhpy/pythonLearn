class cat():

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name+" is sitting now")
    def info(self):
        print("my cat are "+str(self.age)+" monthes")
my_cat=cat('tom',6)
my_cat.sit()
my_cat.info()


# class Restaurant():
#     def __init__(self,restarant_name,cuisine_type):
#         self.name=restarant_name
#         self.type=cuisine_type
#     def describe_restarant(self):
#         print(self.name,self.type)
#     def open_restarant(self):
#         print("restarant is opening")
#
# restarant=Restaurant('翠苑','school')
#
# print(restarant.name,restarant.type)
#
# restarant.describe_restarant()
# restarant.open_restarant()  #9-1餐馆

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

        self.odmoter_reading=0 #默认值

    def get_description(self):
        long_name=str(self.year)+' '+str(self.model)+' '+str(self.make)
        return long_name
    def read(self):
        print("行驶公里数："+str(self.odmoter_reading))
    def update_odmoter(self,milege):   #通过方法修改属性值
        if milege>=self.odmoter_reading:
            self.odmoter_reading=milege  #限制条件
        else:
            print("无法更新 ")
    def increment_odmoter(self,miles):
        if miles>=0:
            self.odmoter_reading +=miles
        else:
            print("禁止回拨")
my_new_car=Car('2019','a8','audi')
name=my_new_car.get_description()
print(name)
my_new_car.odmoter_reading=23 #直接修改属性值
my_new_car.read()
my_new_car.update_odmoter(46)#通过方法修改属性值
my_new_car.read()
my_new_car.update_odmoter(16)
my_new_car.increment_odmoter(20)
my_new_car.read()
my_new_car.increment_odmoter(-5)


# class Restaurant():
#     def __init__(self,restarant_name,cuisine_type):
#         self.name=restarant_name
#         self.type=cuisine_type
#         self.number_served=0
#     def describe_restarant(self):
#         print(self.name,self.type)
#     def open_restarant(self):
#         print("restarant is opening")
#     def set_number_served(self,counts):
#         self.number_served=counts
#     def increment_number_served(self,count):
#         self.number_served += count #9-4



#继承
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe(self):
        print("电瓶容量为 "+str(self.battery_size))

class Cars():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.odmoter_reading = 0  # 默认值

    # def get_description(self):
    #     long_name = str(self.year) + ' ' + str(self.model) + ' ' + str(self.make)
    #     return long_name
    #
    # def read(self):
    #     print("行驶公里数：" + str(self.odmoter_reading))
    #
    # def update_odmoter(self, milege):  # 通过方法修改属性值
    #     if milege >= self.odmoter_reading:
    #         self.odmoter_reading = milege  # 限制条件
    #     else:
    #         print("无法更新 ")
    #
    # def increment_odmoter(self, miles):
    #     if miles >= 0:
    #         self.odmoter_reading += miles
    #     else:
    #         print("禁止回拨")
    def fill_gas(self):
        print(self.make)
        print("加97号")
# class electricCar(Car):
#
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)  #超类，帮助将父类和子类相连 里面放的是父类的全部属性
#         self.battery_size=70
#         self.battery=Battery()  #将battery这个实例作为属性
#     def dianping(self):
#         print("特斯拉电瓶容量为"+str(self.battery_size)+"KWH")
#     def fill_gas(self):#重写父类方法
#         print("这个车没有油箱")
# my_tesla=electricCar('tesla','model3','2018')
# print(my_tesla.get_description())
# my_tesla.dianping()
#
# my_tesla.battery.describe()
car=Car('tesla','model3','2018')



class Restaurant():
    def __init__(self,restarant_name,cuisine_type):
        self.name=restarant_name
        self.type=cuisine_type
        self.number_served=0
    def describe_restarant(self):
        print(self.name,self.type)
    def open_restarant(self):
        print("restarant is opening")
    def set_number_served(self,counts):
        self.number_served=counts
    def increment_number_served(self,count):
        self.number_served += count #9-4
class IceCreamStand(Restaurant):
    def __init__(self,restarant_name,cuisine_type):
        super().__init__(restarant_name,cuisine_type)
        self.flavors=['草莓','芒果','香橙']
    def show(self):
        for a in self.flavors:
            print(a)

my_ice=IceCreamStand('iceland','icecream')
my_ice.show()



