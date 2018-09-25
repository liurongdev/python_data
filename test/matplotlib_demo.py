

import matplotlib.pyplot as plt

data=1,4,9,16,25
data2=1,2,3,4,5

plt.plot(data2,data,linewidth=3)
plt.title("Title",fontsize=14)
plt.xlabel("xlable",fontsize=14)
plt.ylabel("ylable",fontsize=14)
plt.tick_params(axis='both',labelsize=10)
plt.show()

