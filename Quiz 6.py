# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:21:52 2021

@author: Thanakorn
"""

import pandas as pd

df = pd.read_csv("Salaries.csv")

df.head #first 5 records
#Quiz1
df.head(10) #first 10 records
df.head(20) #first 20 records
df.head(50) #first 50 records
df.tail()  #last few records

df['salary'].dtype #Check a particular column type
df.dtypes #Check types for all the columns

#groupby method
#Ex1
df_rank = df.groupby(['rank'])
#Ex2
df_rank.mean() #Calculate mean value for each numeric column per each group
#Ex3
df.groupby('rank')[['salary']].mean() #Calculate mean salary for each professor rank
#Ex4
df.groupby('rank', sort=False)[['salary']].mean() #Calculate mean salary for each professor rank

#filtering
#Ex5
df_sub = df[df['salary'] >120000] #select rows in which the salary value is greater than $120K
#Ex6
df_f = df[df['sex'] =='Female'] #select rows in which the sex is Female

#Slicing
#Ex7
df['salary'] #Select column salary
#Ex8
df[['rank','salary']] #Select column rank and salary

#Selecting rows
#Ex9
df[10:20] #Select rows by their position

#method loc
#Ex10
df_sub.loc[10:20,['rank','sex','salary']] #Select rows by their labels name

#method iloc 
#Ex11
df_sub.iloc[10:20,[0,3,4,5]] #Select rows by their labels index

#Sorting
#Ex12
df_sorted = df.sort_values(by='service') # Create a new data frame from the original sorted by the column service
df_sorted.head() #show the first 5 rows of this data frame
#Ex13
df_sorted2 = df.sort_values(by=['service','salary'], ascending = [True,False])
# Create a new data frame from the original sorted by ascending the column service and descending the column salary
df_sorted2.head(10) #show the first 10 rows of this data frame 