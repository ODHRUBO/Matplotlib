from matplotlib import pyplot as plt
x1=[1,2,3,4,5,6,7,8,9]
y1=[0,2,1,4,5,3,2,10,0]
plt.plot(x1,y1,ls="-.",lw=3,ms=10,mec="r",marker="o",mfc="k")
plt.xlabel("Prise",fontsize=12,color="y")
plt.ylabel("Increase",fontsize=12)

#plt.title("laptop prise",fontsize=20)
plt.title("Laptop Price",fontsize=20,color="g",loc="left")
plt.show()