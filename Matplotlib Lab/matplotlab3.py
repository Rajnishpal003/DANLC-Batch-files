#lab3
import matplotlib.pyplot as plt

segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]
colors=['pink','lightblue','lightgreen','lightyellow']
#creating pie chart
plt.pie(revenue_percentages,labels=segments,colors=colors,autopct='%1.1f%%')
plt.title('Distribution of Company Revenue by Business Segment')
plt.show()