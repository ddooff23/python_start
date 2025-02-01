#import sys
#print(sys.version)
#if 5>3:
#    print('5 is greater than 3')
""""
x=3
print(type(x))
y='3'  #casting
print(type(y))
y=int(y)
print(type(y))
"""
#print('hello me')
"""
a,b,c='doni', 'ali','gani'
print(a)
print(b)
print(c)
x=y=z='odil'
print(x)
print(y)
print(z)

#raspakovka s lista

fruits=['apple','banana','cherry']
x,y,z=fruits
print(x)
print(y)
print(z)

x='python'
y='is'
z='awesome'
print(x,y,z)
print(x+y+z)

x="good"
def myfunc():
    global x
    x='bad'
    print(x+" job")
print(x,'job')    
myfunc()
"""
#types of data
a='any string' #string
b=4 #int
c=4.0 #float
d=12j+12  #complex
print(d)
print(type(d))
e=['one','two','three'] #list
print(e)
print(type(e))
f=('four','five','six')  #tuple
print(f)
print(type(f))
g=range(6)
print(g)
print(type(g))
h={'name':'john','age':36} #dict
print(h)
print(type(h))
i={'seven','eight','nine'} #set
print(i)
print(type(i))
g=frozenset({'ten','eleven','twelve'}) #frozenset
print(g)
print(type(g))
k=b'hello' #bytes
print(k)
print(type(k))
l=bytearray(3) #bytearray
print(l)
print(type(l))
m=memoryview(bytes(5)) #memoryview
print(m)
print(type(m))
o=None #nonetype
print(o)
print(type(o))




