while True:   
    n=input("nomber = ")
    s1=0
    s2=0
    for i in range(0,len(n),2):
        s1=s1+int(n[i-1])
    for i in range(1,len(n),2):
        s2=s2+int(n[i-1])
    d=s1-s2
    print("s1 =",s1)
    print("s2 =",s2)
    print("d =",d)
    print("reste d =",d%11)
    print("reste n = ",int(n)%11)      
    print("——————————————————————————————————————————————————")