

import matplotlib.pyplot as plt



x_value=list(range(1,1000))
y_value=[ x**2 for x in x_value]

plt.scatter(x_value,y_value,edgecolor="none",c="red",s=40)


plt.savefig("test.png",bbox_inches="tight")
plt.show()


