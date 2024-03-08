# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 02:35:49 2024

@author: Asus
"""
'''
The questions
1. Which region has the average lowest and highest prices of Avocado?
2. What is the highest region of avocado production?
3. What is the average avocado prices in each year?
4. What is the average avocado volume in each year?
'''

#importing lib
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing dataset
data=pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\python\AI & ML models  practise sets\ML\0. RESUME PROJECT -- PRICE PREDICTION\avocado.csv")

#checking info & miss values

data.info()
data.head()
data.isnull()
data.tail()
data.shape
data.columns
data.isnull().sum()
data.describe

#answering the first ques
#1. Which region has the average lowest and highest prices of Avocado?
#extracting the columns needed according to question

df=data[['region','AveragePrice']].copy()

#extracting/duplicating the extracted dataframe as backup
#now applying the SPLIT APPLY AND COMBINE method 
#using group by fn as we have lots of similar/repeatative rows with different values so grouping them
#using mean function to get the average

sorted_data=df.groupby('region')['AveragePrice'].mean().sort_values(ascending=False)
sorted_data=sorted_data.reset_index().rename({'region':'region', 'AveragePrice':'AveragePrice'})

#Visualizing the data
plt.figure(figsize=(10, 8)) 
sns.barplot(data=sorted_data,x="region",y="AveragePrice")
plt.xlabel("Region")
plt.xticks(rotation='vertical')
plt.show()

#now 2 ques
#2. What is the highest region of avocado production?
#repeating the same process

highest_data=data[['region','Total Volume']].copy()
highest_data.head()

# Lets creatte the new datframe with this result by reseting index and renaming 

highest_data.groupby('region')['Total Volume'].mean().sort_values(ascending=True).reset_index().rename({'region':'region','Total Volume':'Total Volume'})

#Visualizing the data
plt.figure(figsize=(10,8))
sns.barplot(data=highest_data,x='region',y='Total Volume')
plt.xticks(rotation='vertical')
plt.xlabel('region')
plt.show()

#Insight:Totalus is high production volume of avocado, From the figure we saw this bar is realy high than other region, it can be ouliar, Lets check in box plot to confirm

#3. What is the average avocado prices in each year?

avg_price=data[['year','AveragePrice']].copy()

# Lets creatte the new datframe with this result by reseting index and renaming 

avg_price.groupby('year')['AveragePrice'].mean().sort_values(ascending=True).reset_index().rename({'year':'year','AveragePrice':'AveragePrice'})
sns.barplot(data=avg_price,x='year',y='AveragePrice')

#Visualizing the data
plt.xlabel('year')
plt.xticks(rotation='vertical')
plt.show()
# we see the in 2017 is slightly high avcado price

#4. What is the average avocado volume in each year?

avg_vol=data[['year','Total Volume']].copy
avg_vol.groupby('year')['Total Volume'].mean().sort_values(ascending=True).reset_index().rename({'year':'year','Total Volume':'Total Volume'})

#Visualizing the data
sns.barplot(data=avg_vol,x='year',y='Total Volume')
plt.xlabel('year')
plt.xticks(rotation='vertical')
plt.show()