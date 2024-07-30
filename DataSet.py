from matplotlib import pyplot as plt
x1=[1,2,3,4,5]
y1=[0,2,5,2,1]
x2=[1,2,3,4,5]
y2=[0,2,5,2,1]

plt.subplot(2,2,1)
plt.plot(x1,y1,marker="X")
plt.grid(axis="y",lw=1,color="m",ls=":")
plt.title("sports")

plt.subplot(2,2,2)
plt.plot(x2,y2,marker="o",mec="k",mfc="y")
plt.grid(axis="y",color="b",ls="-.",lw=1)
plt.title("Swimming")

plt.suptitle("Data sets")
plt.show()
