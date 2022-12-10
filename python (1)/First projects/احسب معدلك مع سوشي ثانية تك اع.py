print(" ! attention !")
print("- replace the cont1 with oral if they are no cont2")
print("- if they are no oral and cont2 replace cont2 or cont1 with 0")
print("- if they are no syn replace syn with 0")
def m1(m):
    cont1=float(input("give "+m+" cont1: "))
    cont2=float(input("give "+m+" cont2: "))
    syn=float(input("give "+m+" syn: "))
    if cont2==0 or cont1==0:
        s=(cont1+cont2+syn*2)/3
    elif syn==0:
        s=(cont1+cont2)/2
    elif m=="arabic":
        s=(cont1*1.5+cont2+syn*2)/4.5    
    else:
        s=(cont1+cont2+syn*2)/4
    return s
    
def display(p,moy):
    print("rate of "+p+" is "+str(moy))
    
isl=m1("islamiya")
math=m1("math")
ar=m1("arabic")
geo=m1("geography")    
his=m1("history")
fr=m1("french")
en=m1("english")
mad=m1("madaniya")
phy=m1("physics")
tech=m1("tech")
cs=m1("info")
sp=m1("sport")

display("islamiya",isl)
display("math",math)
display("arabic",ar)
display("geography" ,geo)
display("history",his)
display("french",fr)
display("english",en)
display("madaniya" ,mad)
display("physics",phy)
display("tech",tech)
display("info",cs)
display("sport" ,sp)

moy=((isl)+(geo)+(his)+(mad)+(sp)+(fr*2)+(en*2)+(tech*2)+(ar*2)+(phy*3)+(cs*3)+(math*4))/23
print("your moy is",moy)