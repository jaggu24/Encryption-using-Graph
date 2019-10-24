import sys # Library for INT_MAX 
def printMST(parent,s1,V,graph): 
    print ("Edge \tWeight")
    for i in range(1, V): 
        print (parent[i], "-", i, "\t", graph[i][ parent[i] ]) 
        s1[parent[i]][i]=graph[i][ parent[i] ]
	
def minKey(V, key, mstSet): 

    min = 10000 
    
    for v in range(V): 
        if key[v] < min and mstSet[v] == False: 
            min = key[v] 
            min_index = v 
    return min_index 
 
def primMST(graph,V): 
 
    key = [10000] * V 
    parent = [None] * V 
    key[0] = -10
    mstSet = [False] * V 
    s1=[]
    for f1 in range(V):
        s=[0]*V
        s1.append(s)
    parent[0] = -1 
    
    for cout in range(V): 

        u = minKey(V,key, mstSet) 
        mstSet[u] = True
        for v in range(V): 
            if graph[u][v] !=0 and mstSet[v] == False and key[v] > graph[u][v]: 
                key[v] = graph[u][v] 
                parent[v] = u 

    printMST(parent,s1,V,graph)
    return s1

class node:
    def __init__(self):
        self.a=[]
        self.b=int(5)
c=node()
print(c.b)
a="A"
a1="PPLEA"
a+=a1
b=[]
d=int(0)
for i in range(len(a)):
    e=[]
    for j in range(len(a)):
        e.append((d))
    if i==len(a)-1:
        e[1]=ord(a[1])-ord(a[i])    #sub first with last coz cycle
        b.append(e)
        break
    e[i+1]=ord(a[i+1])-ord(a[i])
#    print(e)
    b.append(e)
import numpy as np
f=np.array(b)
b1=int(27)
for i in range(1,len(f)-2):
    for j in range(i-1+3,len(f)):
        if i==1 and j==len(f)-1:
            continue
        f[i][j]=b1
        b1+=1
f=f+np.transpose(f)
#print(f)
s=primMST(f,len(f)) 
#print(s)
s=np.array(s)
s2=s+np.transpose(s)
s=s+np.transpose(s)
for i in range(len(s)):
    s[i][i]=i
m3=np.dot(f,s)
#print(m3)
k=[]
for i in range(len(m3)):
    k1=[]
    for j in range(i):
        k1.append(int(0))
    for j in range(len(m3)-i):
        k1.append(int(1))
    k.append(k1)
k=np.array(k)
c=np.dot(k,m3)
file=open("encrypt.txt",'w')
for i in c:
    for j in i:
        file.write(str(j))
        file.write(" ")
for i in f:
    for j in i:
        file.write(str(j))
        file.write(" ")
file.close()
