# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:37:03 2021

@author: Thanakorn
"""

import pandas as pd
import numpy as np
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
