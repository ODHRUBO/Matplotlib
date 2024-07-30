 # Scatter
from matplotlib import pyplot as plt
x1 = [1,2,3,4,5]
y1 = [0,1,5,2,5]
x2 = [1,2,3,4,5]
y2 = [0,2,5,2,1]
color = ["hotpink","yellow","cyan","magenta","green"]

# First One
plt.subplot(1,2,1)
plt.scatter(x1,y1,c="cyan")
plt.title("First")

# Second One
plt.subplot(1,2,2)
plt.scatter(x2,y2,c=color)
plt.title("Second")

# Final
plt.suptitle("Data Sets")
plt.show()