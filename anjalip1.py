# -*- coding: utf-8 -*-
"""anjalip1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OL8chjD56JNtZNYWNmnlOUFoWIN-1Otx

workshop 1
"""

45+56

a=4

print('hello colors')

print(4)

b='hello dear code'

b

print(b)

from google.colab import drive
drive.mount('/content/drive')

#this is a command to asignvalues to the variabe
# a=4
b=4     #here 4 value is assigned to the var b

c=6
d=56
e=9

#k= keywords
#def
#none
#true
#False

#I =Identifiers

a=4
b=4.5
c='coders'
d=3+5j
e=5**3
f=9/2
g=9//2
h= None

d.real

d.imag

True+ False

f

g

a+b

if a <6 or a>9:
  print('raghav')

if a<6 and b>9:
 print('raghav')

food = 'pasta'

if food is None:
  print('just in some time, let the class finish')
else:
    print('here,is',food )

age=15
if age > 20:
  print('you might be right')
elif 21<age<23:
    print('age will definately  lies between this range')
else:
      print(' i anjali verify that my age is:',age)

for anjali in[0,1,2,3,]:
  print(anjali**2)

for i in range(4):
  print(i**2)

for i in range(-3,4):
  print(i**2)

n= []
sq= []
cb = []

for i in range(20):
  a=i
  b=i**2
  c=i**3

  n.append(a)
  sq.append(b)
  cb.append(c)

n

sq

cb

import matplotlib.pyplot as plt 
plt.plot(n,sq,'.-',n,cb,'*-')
plt.show()