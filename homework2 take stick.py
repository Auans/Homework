# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 00:14:14 2021

@author: Thanakorn
"""

# Homework 1 : "Take x sticks from the pile"
import random
N = int(input("How many sticks (N) in the pile: "))
print("There are", N, "sticks in the pile")
Name = input("What is your name: ")
print()

# magic number
x = []
for i in range (20):
    a = 3*i-1 
    x.append(a)      
y = []
for i in range (20):
    b = 3*i 
    y.append(b)  
    
for i in range(100):
#player1 take stick
  take_stick =  int(input( str(Name) + ", How many sticks you will take (1 or 2): ")) 
  
  if (0 < take_stick <= 2) and (take_stick <= N) : 
    N = N - take_stick      
    if (N == 0):
      print(str(Name) + ", take the last stick ")  
      print()
      print("I, smart computer, win !!!")
      break
    print(" There are", N, "sticks in the pile")       
    print()
    
#player2 take stick
    if N > 0:
        if N in x:
            bot_take = 1
        elif N in y: 
            bot_take = 2  
        else:
            bot_take = (random.randint(1,2))   
        N = N - bot_take 
        print("I, smart computer, take: ", bot_take)
        print("There are", N, "sticks in the pile")
        print()           
    elif N == 0:  
        print("I, smart computer, take the last stick ")  
        print()
        print(str(Name) + " win (I, smart computer, am sad T_T) ")
        break    
    
  elif (take_stick < 0):
    print(" No you cannot take less than 1 stick !")
  elif (take_stick > 2):       
    print(" No you cannot take more than 2 sticks !")  
  elif (take_stick == 0):
    print(" There are", N, "sticks in the pile")    
  elif (N < 0) or ( take_stick > N):
    print(" There is no enough sticks to take ! ")
