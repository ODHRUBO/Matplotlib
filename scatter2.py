from matplotlib import pyplot as plt
from random import uniform as U

x1=[1,2,3,4,5]
y1=[0,1,5,2,5]
x2=[1,2,3,4,5]
y2=[0,2,5,2,1]

color=["hotpink","yellow","cyan","magenta","green"]
sizes=[500,200,100,300,550]
a=U(0,1)

#First one
plt.subplot(1,2,1)
plt.scatter(x1,y1,c="cyan",s=sizes,alpha=a)
plt.title("First")

#Second one
plt.subplot(1,2,2)
plt.scatter(x2,y2,c=color,alpha = a)
plt.title("Second")

#Final
plt.suptitle("Data sets")
plt.show()