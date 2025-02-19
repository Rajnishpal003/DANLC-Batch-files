# Q.1 Scenario: Suppose you're working in a school you have some student data.
# Please write a program to display the Major subject wise students count and
# also display the pie chart using python pandas and matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
#read data from csv file
df=pd.read_csv('student_data.csv')

#count of student grp by subj
result=df['Major'].value_counts()
print("City-wise Student count:\n",result)

#plot the chart
plt.figure(figsize=(8,5))
colors=['orange','blue','red','purple','green']
plt.pie(result,colors=colors,autopct='%1.1f%%',labels=result.index)
plt.title('City-wise Student Count')
plt.show()