x="cef"
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"]
mors=["___","_.__","_","._",".","_._"]

def rep(x,al,mor):
    for i in range(len(alpha)):
        if alpha[i]==x:
            x+=" "+mors[i]
    return x
j=""
for i in range(len(x)):
    j+=rep(x[i],alpha,mors)+" "
j=j.split()
for i in range(len(j)):
    if j[i] in alpha:
        j[i]=" "
w=""
for i in range(len(j)):
    w+=j[i]
print(w)
