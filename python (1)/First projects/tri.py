p=["oussama","rayen","ayoub","ella","mohammed","sousou"]
t=[10,100,4,70,5,7]

for i in range(len(t)-1):
#~~~~~~~~~~~~~~~~~~~~
    pm=i
    for j in range(i+1,len(t)):
        
        if t[j]>t[pm]:
            pm=j
            
#~~~~~~~~~~~~~~~~~~~~
    if pm!=i:
        
        aux=t[i]
        auxp=p[i]
        
        t[i]=t[pm]
        p[i]=p[pm]
        
        t[pm]=aux
        p[pm]=auxp
        
#~~~~~~~~~~~~~~~~~~~~
    print(t)
    print(p)
    print()