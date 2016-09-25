a = int(input())
b = 0
c = 1
t = 1
while c < a:
        d = c+b
        b = c
        c = d
        t +=1
if(c == a):
    print(t)
else:
    print(-1)
