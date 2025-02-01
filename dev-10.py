# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:03:31 2025
if-elif-else
@author: Doniyor
"""
"""
yosh=int(input("Yoshingiz nechchida: "))
if yosh<=4:
    price=0
elif yosh<=12:
    price=5000
elif yosh<65:
    price=10000    
else:
    price=8000
print(f'Sizga kirish {price} so\'m') 
   
kun=input("Bugun qanaqa kun? ")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni!')
else:
    print("Bugun ish kuni!")
menu=['osh','kozonkabob','norin','chuchvara','shashlik']
buyurtmakar=['osh','somsa','shashlik','manti']
if buyurtmakar:
 for taom in buyurtmakar:
    if taom in menu:
        print(f"menuda {taom} bor")
    else:
        print(f'menuda {taom} yoq')
else:
    print("Buyurtma yoq")
num=int(input("Juft son kiriting = "))
if num%2==0:
    print('Rahmat')
else:
    print('Bu toq son')        
yosh=int(input("Yoshiz nechida?>>> "))
if yosh<4 or yosh>60:
    price=0
elif yosh<18:
    price=10000
else:
    price=20000
print(f'Sizdan {price} som')    
son=float(input("Birinchi sonni kiriting = "))
son2=float(input("Ikkinchi sonni kiriting = "))
if son>son2:
    print(f'{son} > {son2}')
elif son<son2:
    print(f'{son} < {son2}')
else:
    print(f'{son} = {son2}')        
      
mahsulot=['nok','piyoz','qovoq','sabzi','olma','un','yog','makaron']
savat=[]
for i in range(5):
    savat.append(input(f"Savatga {i+1} mahsulotni kiriting = "))
for l in savat:
    if l in mahsulot:
        print(f'Dokonimizda {l} bor')
    else:
        print(f'Dokonimizda {l} yoq')

mahsulotlar=['nok','olma','piyoz','sabzi','shakar']
savat=[]
bor_mahsulotlar=[]
mavjud_emas=[]
for i in range(5):
    savat.append(input(f'Savatga {i+1} mahsulotni qo\'shing = '))
    
for mahsulot in savat:
    if mahsulot in mahsulotlar:
       bor_mahsulotlar.append(mahsulot)
    else:
       mavjud_emas.append(mahsulot)
if mavjud_emas:
    print('Dokonimizda quyidagi mahsulotlar yoq:')
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print('Siz soragan barcha mahsulot dokonimizda bor')
    
foydalanuvchilar=['alisher','aziza','bilol','noir','shaxboz']
user=input("Yangi login tanlang: ")
if user in foydalanuvchilar:
    print("Bu login band, iltimos boshka login tanlang!")
else:
    print(f"Xush kelibsiz, {user.title()}")
"""
son=int(input("Butun son kiriting = "))
for n in range(2,11):
    if not (son%n):
        print(f'{son} soni {n} ga qoldiqsiz bolinadi!')





