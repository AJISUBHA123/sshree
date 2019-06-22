a8=int(input())
b8=[]
x3=''
for i in range(a8):
    c=input()
    b8.append(c)
for i in range(a8-1):
    d=b8[i]
    e=b8[i+1]
    for y in range(len(min(b8,key=len))):
        if d[y]==e[y]:
            x3+=d[y]
        else:
            break
    b8.pop(i)
    b8.insert(0,x3)
    x3=''
print(b8[0])
