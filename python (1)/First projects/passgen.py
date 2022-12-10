from random import*
n=int(input("nunber c: "))
t="z x c v b n m a s d f g h j k l q w e r t y u i o p".split()
c=""
for i in range(n):
    c+=choice(t)
print(c)