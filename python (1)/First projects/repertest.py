from numpy import array
from time import sleep

v=False
while v==False:
    type=input("choose type prbl / hyprbl :")
    v=type=="prbl"or type=="hyprbl"
n=1000

x=array([float()]*n)
y=array([str]*n)
x1=array([float()]*n)
y1=array([str]*n)

if type=="prbl":
    f=str(input("ax**y+bx+c for prbl: "))
    a=f[0:f.find("x**2")]
    b=f[f.find("**2")+3:f.find("x",len(f[0:f.find("x")+1]))]
    c=f[f.find("x",len(f[0:f.find("x")+1]))+1:len(f)]

    if eval(a)!=0 :
        x=array([float()]*n)
        y=array([str]*n)
        x1=array([float()]*n)
        y1=array([str]*n)
        a=eval(a)
        b=eval(b)
        c=eval(c)
        sx=(-b)/(2*a)
        i=0
        cx=sx
    
        while i<n:
            x[i]=cx
            h=eval(str(a)+"*(("+str(cx)+")**2)"+"+("+str(b)+"*"+str(cx)+")+"+str(c))
            y[i]=h
            cx+=0.1
            i+=1
        i1=0
        cy=sx
    
        while i1<n:
            x1[i1]=cy
            h1=eval(str(a)+"*(("+str(cy)+")**2)"+"+("+str(b)+"*"+str(cy)+")+"+str(c))
            y1[i1]=h1
            cy-=0.1
            i1+=1
        
    elif eval(a)==0:
        n=40
        x=array([float()]*n)
        y=array([str]*n)
        x1=array([float()]*n)
        y1=array([str]*n)
        b=eval(b)
        c=eval(c)
        sx=0
    
        i=0
        cx=sx
        while i<(n):
            x[i]=cx
            h=eval(str(a)+"*(("+str(cx)+")**2)"+"+("+str(b)+"*"+str(cx)+")+"+str(c))
            y[i]=h
            cx+=10
            i+=1
        
        i1=0
        cy=sx
        while i1<(n):
            x1[i1]=cy
            h1=eval(str(a)+"*(("+str(cy)+")**2)"+"+("+str(b)+"*"+str(cy)+")+"+str(c))
            y1[i1]=h1
            cy-=1
            i1+=1
    print(x1)
    print("##############################################")
    print(y1)
    print("a =",a)
    print("b =",b)
    print("c =",c)
    print("S(",x1[0],",",y1[0],")")

    print(str(a)+"*(("+str(sx)+")**2)"+"+("+str(b)+"*"+str(sx)+")")
elif type=="hyprbl":
    f=str(input("ax+b/cx+d for hyprbl: "))
    a=f[0:f.find("x")]
    b=f[f.find("x")+1:f.find("/")]
    c=f[f.find("/")+1:f.find("x",len(f[0:f.find("/")]))]
    d=f[f.find("x",len(f[0:f.find("x")+1]))+1:len(f)]
    
    if eval(a)!=0 :
        x=array([float()]*n)
        y=array([str]*n)
        x1=array([float()]*n)
        y1=array([str]*n)
        a=eval(a)
        b=eval(b)
        c=eval(c)
        d=eval(d)
        sx=-d/c
        i=0
        cx=sx
    
        while i<n:
            x[i]=cx
            try:
                h=eval("("+str(a)+"*"+str(cx)+"+"+str(b)+")/("+str(c)+"*"+str(cx)+"+"+str(d)+")")
            except:
                h="none"
            y[i]=h
            cx+=0.1
            i+=1
        i1=0
        cy=sx
    
        while i1<n:
            x1[i1]=cy
            try:
                h1=eval("("+str(a)+"*"+str(cy)+"+"+str(b)+")/("+str(c)+"*"+str(cy)+"+"+str(d)+")")
            except:
                h1="none"
            y1[i1]=h1
            cy-=0.1
            i1+=1
    
    print(x1)
    print("##############################################")
    print(y1)
    print("a =",a)
    print("b =",b)
    print("c =",c)
    print("d =",d)
    print("S(",x1[0],",",y1[0],")")
sleep(100000)