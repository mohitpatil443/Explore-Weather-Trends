import matplotlib.pyplot as plt
import pandas as pd

#Replaced the backward slash by forward slash
#data frame
df = pd.read_csv('C:/Users/MOHIT/Desktop/Udacity Data Analytics/1 Intro To Data Science/Project 1/results.csv')

plt.plot(df['year'], df['global_avg'], label='Global')
plt.plot(df['year'], df['local_avg'], label='Delhi')
plt.legend()
plt.title('Moving Average Temperature Comparison')
plt.xlabel('Year')
plt.ylabel('Moving Average Temperature')



plt.show()



