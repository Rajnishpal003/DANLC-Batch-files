#Lab1
import matplotlib.pyplot as plt
import numpy as np

square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])
#creating scatterplot
plt.scatter(square_footage,selling_prices,color='green',marker='o')
plt.xlabel('Square Footage(sq.ft.)')
plt.ylabel('Selling Prices($000s)')
plt.title('Housing Prices vs. Square Footage')
plt.legend()
plt.grid(True)
plt.show()