N = input("donner un entier:")
M =int(N[-4])
C =int(N[-3])
D = int(N[-2])
U = int(N[-1])
if U%M ==0 and D%M==0 and C%M==0:
	print(N,"est valable")
else:
	print(N,"non valable")