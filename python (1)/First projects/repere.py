from turtle import*
from time import sleep
from numpy import array

def repere():
    speed(100)
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

f=str(textinput("f(x)=ax**y+bx+c",""))    
n=int(textinput("lenght","nomber"))
x=array([int()]*n)
y=array([str]*n)
#if "**2" in str(f):
    #sx=eval(str(int(str(f)[str(f).find("**2")+3:str(f).find("x",len(str(f)[0:str(f).find("x")+1]))])*-1)+"/"+str(int(str(f)[0:str(f).find("x**2")])*2))
    
for i in range(n):
    h=eval(str(f).replace("x","*"+str(i)))
    x[i]=i
    y[i]=h
x1=array([int()]*n)
y1=array([str]*n)
x12=array([int()]*n)
y12=array([str]*n)
if "**2" in str(f) :
    for i in range(n):
        h1=eval(str(f).replace("x","*"+str(-i)))
        x1[i]=-i
        y1[i]=-h1
    repere()
    penup()
    pencolor("green")
    goto(x[0]*18,y[0]*18)
    pendown()
    for i in range(n):
        goto(x[i]*18,y[i]*18)
    penup()
    goto(x1[0]*18,y1[0]*18)
    for i in range(n):
        goto((x1[i])*18,(y1[i]+y[0]*2)*18)
        pendown()
        
elif not("**2"in str(f)) :
    for i in range(n):
        h1=eval(str(f).replace("x","*"+str(-i)))
        x1[i]=-i
        y1[i]=-h1
    repere()
    penup()
    pencolor("green")
    goto(x[0]*18,y[0]*18)
    pendown()
    for i in range(n):
        goto(x[i]*18,y[i]*18)
    penup()
    goto(x1[0]*18,y1[0]*18)
    for i in range(n):
        goto(x1[i]*18,-y1[i]*18)
        pendown()

    
    
    
    
    
    
sleep(100000)

