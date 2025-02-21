l=[1,5,9,10,16,98,"a"]
for i in range(len(l)-1, -1, -1):
    print("sto rimuovendo elemento all indice", i)
    l.remove(l[i])

l=[1,5,9,10,16,98,"a"]
while len(l)>0:
    x=l.pop()
    print("ho rimosso", x)

l=[1,5,9,10,16,98]
#sorted funzione 
#help(sorted)
#sorted(l,reverse=True, key=lambda x:x**2)
#lo=sorted(l)
#print(lo)

l.sort()
print(l)

l.reverse()
print(l)

#help(list)


s1=set(l)
print(s1)

d=dict(x=1,y=3, z=4)
print(d)

#help(dict)
#help(list)
d["t"]=5
print(d)
for u, v in d.items():
    print(u,v)

tu=(3,4)
x,y=tu
print(x)
print(y)
x,y,z =3,4,5
print(z)
del x
del y
del z
s1 =[1,2]
l=[]
l.extend(s1)
print(l)
l1=[4,5,6,7]
l=l+l1
print(l)

#def molt_lista(l:list, n:float) -> list:
    #restituisceuna nuova lista l1 tale che l1[1]=l[i]*n


l1:list=[]
for el in l1:
    l1 +=[el*n] #l1.append(el*n)
    return l1

    

