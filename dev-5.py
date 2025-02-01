# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:18:10 2025
LIST
@author: Doniyor
"""
fruits=['olma', 'nok','Shaftoli']
print('birinchi element ', fruits[0].title())
print('ikkinchi element',fruits[1].upper())
print('uchinchi element', fruits[2].lower())
costs=[12000,11000,10000,4000,32000]
print(costs[3]+costs[4])
print(costs[-1])
fruits.append('GILOS')
print(fruits)
costs[0]+=1000
costs[1]-=1000
costs[-1]-=30000
print(costs)
fruits.insert(1, "behi")
print(fruits)
del fruits[2]#delete with index
print(fruits)
costs.remove(10000)#delete with value
print(costs)
bozorlik=['piyoz','non','gosht','kolbasa','saryog\'']
print(bozorlik)
x=bozorlik.pop(2)
print(x.title(), "sotib oldim endi kolgan mahsulotlarni olaman")
print("qolgan mahsulotlar\n",bozorlik)
print(bozorlik.pop())