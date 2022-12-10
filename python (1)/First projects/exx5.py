from random import*
indent=input("donner l'identifuant de la carte 8 chiffres:")
da=input("donner la date en form J/M:")
J=da[0:da.find("/")]
M=da[da.find("/")+1:]
X=randint(5,64)
y=int(J+M)*X
Y=str(y)
if len(Y)==4:
	Y=Y[1]+Y[2]+Y[3]+Y[0]
elif len(Y)==2:
	Y=Y+"0"+"0"
elif len(Y)==3:
	Y=Y+"0"
elif len(Y)>4:
	Y=str(int(Y[:4])+int(Y[4:]))
print("code=",Y)