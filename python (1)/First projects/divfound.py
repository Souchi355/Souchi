while True:
    print("a/b = c/d: ")
    a=input("a: ")
    b=input("b: ")
    c=input("c: ")
    d=input("d: ")
    if a=="n":
        a=(int(c)*int(b))/int(d)
        print("a=",a)
    elif b=="n":
        b=(int(a)*int(d))/int(c)
        print("b=",b)
    elif c=="n":
        c=(int(a)*int(d))/int(b)
        print("c=",c)
    elif d=="n":
        d=(int(b)*int(c))/int(a)
        print("d=",d)
    print("——————————————————————————————————————————————————")
