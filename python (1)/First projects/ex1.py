from numpy import array
from random import randint

#taille de tableau
valide1=False
while valide1==False:
    n=int(input("donner la taille de tableu: "))
    valide1=2<n<20
    
t=array([str()]*n)
r=array([int()]*n)

#remplir prenom
for i in range(n):
    valide2=False
    while valide2==False:
        prenom=input("donner prenom: ")
        if len(prenom)>2 and "A"<=prenom[0]<="Z":
            t[i]=prenom
            valide2=True
#remplir options
for i in range(n):
    valide3=False
    while valide3==False:
        ops=int(input("donner nombre de options: "))
        if ops>0:
            r[i]=ops
            valide3=True

nb=0
for i in range(n):
    if r[i]==1:
        print(t[i])
    else:
        nb=nb+1
print("les nombers des eleve qui choisi plus option: ",nb)