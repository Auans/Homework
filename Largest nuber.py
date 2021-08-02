# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:05:47 2021

@author: Thanakorn
"""

def LargeNumber(number):
    Cal = ""
    List = []
    
    for i in number:
        x = str(i)*2
        List.append((x[:], i))
        List.sort(reverse= True)
        
    for i in List:
        Cal += str(i[1])

    return Cal


list1 = [50,20,1,9]
list2 = [10,1]
print(LargeNumber(list1))    
print(LargeNumber(list2))            
        
        