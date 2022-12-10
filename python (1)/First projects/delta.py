e=input("donner ax**2+bx+c:")
if e[0] =="-":	
    a=float(e[1:e.find("x")])
    a=-a
elif e[0]=="+":
	a=float(e[1:e.find("x")])
else:
	a=float(e[:e.find("x")])
if e[e.find("x")+4]=="-":
    b =(e[e.find("x")+5:e.find("x",2)])
   # b =-b
elif e[e.find("x")+4]=="+":
	b =float(e[e.find("x")+5:e.find("x",2)])
#if e[e.find("x",2)+1]=="-":
#    c =float(e[e.find("x",2)+2:])
    #c =-c
#elif e[e.find("x",2)+1]=="+":
	#c =float(e[e.find("x",2)+2:])
print("a=",a,"b=",b,"c=")