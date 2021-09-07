# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:37:03 2021

@author: Thanakorn
"""
import pandas as pd
avocado = pd.read_csv("avocado.csv")

#1)Which region sold the largest amount of avocado ?
larggest_region = avocado.groupby('region')[['Total Volume']].max()
larggest_region.sort_values(by = 'Total Volume')
#Region which sold the largest amount of avocado is West with 11274749.11 of Total Volume
wast_region = avocado[['4046', '4225','4770','region']]
wast_region[wast_region['region'] == 'West' ].max()
# The biggest lot of sold avocado came from 4046 with 4.37754e+06

#2)Which region sold the smallest amount of avocado ?
# from larggest_region.sort_values 
#Region which sold the largest amount of avocado is Syracuse with 113023.35 of Total Volume
Syracuse_region = avocado[['4046', '4225','4770','region']]
Syracuse_region[Syracuse_region['region'] == 'Syracuse' ].max()
# The biggest lot of sold avocado came from 4225 with 78340.7

#3) Which region sold the highest price of avocado in average ?
highest_price = avocado.groupby('region')[['AveragePrice']].max()
highest_price.sort_values(by = 'AveragePrice')
#region which sold the highest price of avocado in average is SanFrancisco 

#4) Find the total amount of income (Avg_Price*Total_Volume) of each region.
volume_price = avocado.groupby('region')[['Total Volume','AveragePrice']].max()
income = volume_price['Total Volume']*volume_price['AveragePrice']

#5) Let AVOCADO  Average Weight : 4046 => 4 ounces, 4225 => 9 ounces, 4770 => 12 ounces
weight = avocado.groupby('region')[['4046', '4225','4770']].mean()
number_4046 = weight['4046']/4
number_4225 = weight['4225']/9
number_4770 = weight['4770']/12
number = pd.DataFrame({'number_4046':number_4046,'number_4225':number_4225,'number_4770':number_4770 })
number['total number'] = number['number_4046'] +number['number_4225'] + number['number_4770']
number.sort_values(by = 'total number')
#The region that sold the largest of number of avocadoes is SouthCentral 

#6) Normally, the customers buy the avocados by unit or in a bags ?
avocado['Total unit'] = avocado['4046'] + avocado['4225'] + avocado['4770']
volume = avocado[['Total Volume','Total unit','Total Bags']]
volume.sum()
#Normally, the customers buy the avocados by unit.