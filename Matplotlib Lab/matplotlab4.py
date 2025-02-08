#lab4
import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000,
                              36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000,
                            23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000,
                              25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000,
                                  19000, 20000, 21000, 22000, 23000])

fig,axs=plt.subplots(2,2,figsize=(12,10))
#first plot
axs[0,0].plot(months,electronics_sales,marker='o',color='blue')
axs[0,0].set_xlabel('Month')
axs[0,0].set_ylabel('Sales Amount')
axs[0,0].set_title('Electronics')
axs[0,0].legend()

#second plot
axs[0,1].plot(months,clothing_sales,marker='o',color='green')
axs[0,1].set_xlabel('Month')
axs[0,1].set_ylabel('Sales Amount')
axs[0,1].set_title('Clothing')
axs[0,1].legend()

#third plot
axs[1,0].plot(months,home_garden_sales,marker='o',color='red')
axs[1,0].set_xlabel('Month')
axs[1,0].set_ylabel('Sales Amount')
axs[1,0].set_title('Home & Garden')
axs[1,0].legend()

#fourth plot
axs[1,1].plot(months,sports_outdoors_sales,marker='o',color='purple')
axs[1,1].set_xlabel('Month')
axs[1,1].set_ylabel('Sales Amount')
axs[1,1].set_title('Sports & Garden')
axs[1,1].legend()

#super title
plt.suptitle('Sales Performance by Product Categories')
plt.tight_layout()
plt.show()



