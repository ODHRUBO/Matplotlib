from matplotlib import pyplot as plt
x1=[1,2,3,4,5,6,7,8,9]
y1=[0,3,2,4,9,3,3,5,0]
plt.plot(x1,y1,marker="o",mfc="k")
plt.xlabel("Price",fontsize=12)
plt.ylabel("Increase",fontsize=20)
plt.title("Laptop Price",fontsize=20,loc="left")
plt.grid()
plt.grid(axis="y")
plt.grid(axis="y",linewidth=0.5,color="m",ls="-.")
plt.show()