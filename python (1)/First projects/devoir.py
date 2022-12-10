from numpy import array

def saisir():
    valide=False
    while valide==False:
        n=int(input("donner taille :"))
        valide=2<=n<=15
    return n
def poid(ch):
    s=0
    for i in range(len(ch)):
        s=s+ord(ch[i])
    return s
    
def remplir1(t1,n):
    for i in range(n):
        valide=False
        while valide==False:
            t1[i]=input("donner chaine de ["+str(i)+"]")
            valide=t1[i] !=""
            
def remplir2(t1,t2,n):
    for i in range(n):
        t2[i]=poid(t1[i])
        
def affiche(t1,t2,n):
        print("t1:")
        for i in range(n):
            print(t1[i])
        print("t2: ")
        for i in range(n):
            print(t2[i])

n=saisir()
T=array([str]*n)
R=array([int()]*n)
remplir1(T,n)
remplir2(T,R,n)
affiche(T,R,n)