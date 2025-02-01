# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:38:47 2025
Lists
@author: Doniyor
"""
"""
countries=['Uzbekistan','America','Canada','Japan','Russia','Portuguese']
print(countries)
print(len(countries))
print("To'g'ri tartibda: ",sorted(countries))
print("Teskari tartibda: ",sorted(countries,reverse=True))
print(countries)
countries.reverse()
print("Ortdan boshlangan ro'yhat: ",countries)
countries.sort()
print("Alifbo buicha: ",countries)
countries.sort(reverse=True)
print("Alifboga taskari tartibda: ",countries)
juft_sonlar=list(range(120,1200,2))
print("Juft sonlar 120-1200: ",juft_sonlar)
print("sonkar yegindisi: ",sum(juft_sonlar))
print("max - min = ",max(juft_sonlar)-min(juft_sonlar))
print("elementlar soni: ",len(juft_sonlar))
middle_element=len(juft_sonlar)/2
print(middle_element)
print("boshidan 20 element: ",juft_sonlar[:20])
print( "Oxiridan 20 element",juft_sonlar[-20:])
print("Ortasidan 20 element: ",juft_sonlar[260:280)
"""
taomlar=['manti','osh','norin','chuchvara','shorvo']
nonushta=taomlar[0:]
nonushta.remove('osh')
del nonushta[0]
nonushta.append('tuhum')
nonushta.insert(0,"omlet")
print(taomlar)
print(nonushta)
nonushta=tuple(nonushta)
#nonushta[0]="qaymoq va non" #tuplega qiymat ozgartirib bolmaydi!
print(nonushta)

