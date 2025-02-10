#Lab1
# Lab1: Write a Pandas program to create a dataframe from a dictionary and
# display it.

import pandas as pd

#dictionary data
score={'Math':[78,85,96,80,86],
       'English':[84,94,89,83,86],
       'Hindi':[86,97,96,72,83]}

#data frame from dictionary
df=pd.DataFrame(score)
#display
print("Data Frame:\n",df)


