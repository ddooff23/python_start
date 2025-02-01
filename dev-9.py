# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:55:38 2025
If-Else
@author: Doniyor
"""
"""
avtolar=['audi', 'bmw','volvo','hundai']
for avto in avtolar:
    if avto=='bmw':
        print(avto.upper())
    else:
        print(avto.capitalize())
ism=input('Ismingizni kiriting: ')
if ism.lower()!='ali':
    print(f'Uzur {ism.title()} biz Alini kutyabmiz')
else:
    print('Salom Ali')

javob=float(input("12*9 nechiga teng >>> "))
if javob!=108:
    print('Javob notogri')

yosh=int(input("Yoshingiz nechida? >>> "))   
if yosh<18:
    print("Detskiy ekamsan ukam!")
else:
    print("Xush kelding")
login=input("Loginni kirit >>> ")
if len(login)<5:
    print("Login 5ta harfdan kop bolishi kerak!")
else:
    print("Xush kelding")

x, y=25,50
print("x>y") if x>y else print("x<y")

#Amaliyot if-else
cars=["toyota","mazda","hyundai","gm","kia"]
for avto in cars:
    if avto!='gm':
        print(avto.capitalize())
    else:
        print(avto.upper())
login=input("Loginni kiriting >>> ")
if login=='admin':
    print("Xush kelibsiz, Admin.\nFoydalanuvchilar royhatini korasizmi?")
else:
    print(f"Xush kelibsiz,{login}!")
a=int(input("birinchi butun sin kiriting = "))
b=int(input("ikkinchi butun son kiriting = "))
if a==b:
    print("sonlar teng ekan")
son=float(input("Istalgan son kiriting = "))
if son<0:
    print("Manfiy son ekan")
else:
    print("Musbat son ekan")
"""
number=float(input('Son kiriting = '))
if number<0:
    print('Musbat kiriting!')
else:
    print(f"{number} ildizi = {number**0.5}ga teng")













































 