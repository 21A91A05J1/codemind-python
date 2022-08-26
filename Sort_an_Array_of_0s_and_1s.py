n=int(input())
l=list(map(int,input().split()))[:n]
a=[]
b=[]
for i in l:
    if i==1:
        a.append(1)
    else:
        b.append(0)
b.extend(a)
print(*b)