from numpy import array
from time import sleep
from turtle import *

f=str(textinput("f(x)=ax**y+bx+c : ",""))
n=1000

x=array([float()]*n)
y=array([str]*n)
x1=array([float()]*n)
y1=array([str]*n)

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

def repere():
    speed(100000)
    k=0
    for i in range(38):
        penup()
        goto(500,k)
        pendown()
        goto(-500,k)
        k+=18
    p=0
    for i in range(37):
        penup()
        goto(-500,-p)
        pendown()
        goto(500,-p)
        p+=18
    s=0
    for i in range(30):
        penup()
        goto(s,1000)
        pendown()
        goto(s,-1000)
        s+=18
    u=0
    for i in range(30):
        penup()
        goto(-u,1000)
        pendown()
        goto(-u,-1000)
        u+=18
    penup()
    pencolor("red")
    width(3)
    goto(0,1000)
    pendown()
    goto(0,-1000)

    penup()
    pencolor("blue")
    width(3)
    goto(500,0)
    pendown()
    goto(-500,0)
    
repere()
penup()
pencolor("green")
goto(x[0]*18,y[0]*18)
pendown()
for i in range(n):
    goto(x[i]*18,y[i]*18)
penup()

penup()
pencolor("green")
goto(x1[0]*18,y1[0]*18)
pendown()
for i in range(n):
    goto(x1[i]*18,y1[i]*18)
penup()

sleep(100000)