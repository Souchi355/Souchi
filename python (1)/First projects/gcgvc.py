a=input("donner a + b: ")
A = float(a[0:a.find(" ")])
S = (a[a.find(" ")+1])
B =float(a[a.find(" ",2):])
if  S== "+":
	print(A + B)
elif S == "×":
	print(A * B)
elif S == "÷":
	print(A/ B)
elif S == "-":
	print(A - B)
elif S =="^":
	print(A ** B)