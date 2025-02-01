"""
a=23
txt=f'something {a+5}'
print(txt)
print("hello \"new\" world ") #" "
print('It\'s alright')#\'
print("this is one insert \\ (backslash).") #\
print('hello\nworld')#\n new line
print('hi\rguys')#\r carriage return
print('hi\tguys')#\t tabulation
#This example erases one character (backspace):
t = "Hello \bWorld!"
print(t)
#A backslash followed by three integers will result in a octal value:
tx = "\110\145\154\154\157"
print(tx)
#A backslash followed by an 'x' and a hex number represents a hex value:
txt1 = "\x48\x65\x6c\x6c\x6f"
print(txt1)
"""
#txt = "H\te\tl\tl\to"
txt="d\to\to\tg"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))