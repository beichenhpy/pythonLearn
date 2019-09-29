import matplotlib.pyplot as plt
#scatter 画散点图
# plt.scatter(2,4,s=200) #(2,4)这个点
input_xvalues=[1,2,3,4,5,6]
input_yvalues=[1,4,9,16,25,36]
plt.scatter(input_xvalues,input_yvalues,s=100,c=input_yvalues,cmap=plt.cm.Blues,edgecolors='none')
# input_x=list(range(1,1001))
# input_y=(x**2 for x in input_x)
# plt.scatter(input_x,input_y,s=40)
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
# plt.axis([0,1100,0,1100000])
plt.show()