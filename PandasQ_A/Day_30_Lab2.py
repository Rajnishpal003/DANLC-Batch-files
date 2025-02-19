# Q.2 Scenario: Suppose you're working in a retail store you have some customer data.
# Please write a program to display the marital status wise customer count and
# also display the bar chart using python pandas and matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
#read data from csv file
df=pd.read_csv('customer_data.csv')


result=df['Marital_status'].value_counts()
print("Marital_status wise Student count:\n",result)

#plot the graph
plt.figure(figsize=(8,5))
plt.pie(result,labels=result.index,colors=['blue','orange'],autopct='%1.1f%%')
plt.title('Marital_status wise Student count')
plt.show()
