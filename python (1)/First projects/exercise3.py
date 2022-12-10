t= int(input("donner le nombre de sexondes:"))
h = (t%86400)//3600
m = (t%3600)//60
s = (t%60)
print( h, "heurs,", m, "minutes,", s, "secondes.")
