#lab2
import matplotlib.pyplot as plt

income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

colors=['lightgreen','lightblue','lightcoral','yellow','pink']
#create pie chart
plt.pie(monthly_income,labels=income_sources,colors=colors,autopct='%1.1f%%')
plt.title('Distribution of Monthly Income by Source')

plt.show()