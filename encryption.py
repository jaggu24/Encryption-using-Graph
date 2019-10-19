# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:50:09 2019

@author: hanum
"""
print("Decrypt")
import numpy as np
a1=np.array([[836,302,-624,476,450],[352,280,-180,476,450],[352,-688,-244,406,217],[836,-666,-744,198,77],[242,-605,-158,133,49]])
a2=np.array([[0,22,0,0,0],[22,0,-22,27,11],[0,-22,0,4,28],[0,27,4,0,7],[0,11,28,7,0]])
file=open("encrypt.txt",'w')
for i in a1:
    for j in i:
        file.write(str(j))
        file.write(" ")
for i in a2:
    for j in i:
        file.write(str(j))
        file.write(" ")
file.close()
#ss=[]
print("Decryption")
with open("encrypt.txt",'r') as file1:
    data=file1.readlines()
    for i in data:
        ss=i.split()
for i in range(len(ss)):
    ss[i]=int(ss[i])
a=len(ss)/2
b=np.sqrt(a)
c=[]
d=[]
b1=int(0)
b2=int(b)
while b2<=a:
    c1=ss[b1:b2]
    c.append(c1)
    b1+=int(b)
    b2+=int(b)
b1=int(a)
b2=int(a)+int(b)
while b2<=len(ss):
    c1=ss[b1:b2]
    d.append(c1)
    b1+=int(b)
    b2+=int(b)
k=[]
for i in range(int(b)):
    k1=[]
    for j in range(i):
        k1.append(int(0))
    for j in range(int(b)-i):
        k1.append(int(1))
    k.append(k1)
k=np.array(k)
d=np.array(d)
c=np.array(c)
k2=np.linalg.inv(k)
m3=np.dot(k2,c)
m1=np.linalg.inv(d)
m2=np.dot(m1,m3)
s="A"
k1=int(0)
j=int(1)
for i in range(len(m2)-1):
#    for j in range(1,len(m2)):
    if abs(m2[i][j]-m2[j][i])<=2:
        s+=chr(ord(s[k1])+int(m2[j][i]))
        k1+=1
        j+=1
        print(j)
    else:        
        s+=chr(ord(s[k1])+int(m2[i][j]))
        k1+=1
        j+=1
        print(j)
        break
s+=chr(ord(s[k1])+int(m2[len(d)-2][len(d)-1]))
print(s)
#
#print(m2)