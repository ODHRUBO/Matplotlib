from matplotlib import pyplot as plt
x1=[1,2,3,4,5]
y1=[1,3,8,6,1]
y2=[0,1,0,2,7]
x2=[5,4,3,2,1]
y3=[0,1,0,4,7]
x3=[5,4,2,1,1]
plt.plot(x1,x2,x3,y2,y1,y3,lw=2,ls=":",marker="o",markersize=10,mec="k",mfc="c")
plt.show()