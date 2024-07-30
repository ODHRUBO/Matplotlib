from matplotlib import pyplot as plt
x=["A","B","C","D","E"]
y=[1,2,3,4,5]
c=["magenta","yellow","green","red","cyan"]
plt.bar(x,y,color=c,width=0.5)
plt.title("Bar",loc="left")
plt.xlabel("Letters")
plt.ylabel("Numbers")
plt.show()