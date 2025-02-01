# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:52:19 2025
Lists practice
@author: Doniyor
"""
"""
ismlar=['Aziz','Nurik','Nari','Tima','Nur']
#print(f"Salom {ismlar[0]}, bugun choyxona bormi?")
print('Salom', ismlar[0],', bugun choyxona bormi?')
print(ismlar[1],'choyxonaga boramizmi?')
print('Nega?',ismlar[2],'kemiman daysan?')
print(ismlar[3],': "Kechro borman bolla, uzur aa"')
print('Bu safar umuman ilojim yoq',ismlar[4])
sonlar=[12,-2,0,-5.6,3.2]
sonlar[0]+=3
sonlar[2]-=5
print(sonlar)
print(sonlar[0]+sonlar[2])
sonlar.append(45.10)
print(sonlar)
sonlar.insert(1, 32)
print(sonlar)
print(sonlar.remove(-2))
print(sonlar)
del sonlar[1]
print(sonlar)

t_shaxslar=['Imom Buxoriy','Amir Temur','Enshteyn']
z_shaxslar=['Ilon Mask','Khabib Nurmagameddov','Trump']
print(f"Men tarixiy shaxslardan {t_shaxslar[2]} bilan,\
      zamonaviy shaxslardan esa {z_shaxslar[1]} bilan \
          suhbat qilishni istar edim")
print("Men tarixiy shaxslardan",t_shaxslar.pop(2),"bilan,\
      zamonaviy shaxslardan esa",z_shaxslar.pop(1),"bilan \
          suhbat qilishni istar edim")
          """
friends=[]
friends.append('Nur')
friends.append('Jorka')
friends.append('Noza')    
print(friends)
friends.remove('Jorka')
print(friends)
friends.insert(0, "Xasan")
friends.append("Guzal")
print(friends)
friends.insert(2, 'Tima') 
print(friends)   
 
mehmonlar=[]
print('mehmonlar:\n')   
#bir listdan boshqa listga element utqazish
a=friends.pop(0)
b=friends.pop(3)
c=friends.pop(2)
print(friends)  
print(mehmonlar) 
mehmonlar.append(a)
mehmonlar.append(b)
mehmonlar.append(c)
print(mehmonlar)
mehmonlar.append(friends.pop(0))
print("Kelgan mehmonlar: ",mehmonlar)
          
          
          
          
          
          
          
          
          
          
          
          
          
          

