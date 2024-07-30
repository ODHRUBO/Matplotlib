from matplotlib import pyplot as plt
y=[20,85,90,23,10]
mylabels=["Apple","Banana","Grapes","Weed","Tobacco"]
myexplod=[0,0.1,0.2,0,0.1]
mycolors=["black","blue","cyan","magenta","green"]
plt.pie(y,labels=mylabels,explode=myexplod,shadow=False,colors=mycolors)
plt.legend(title="Fruits")
plt.show()