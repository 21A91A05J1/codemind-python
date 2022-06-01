n=int(input())
p=1
s=0
t=n
while t:
    r=t%10
    s=s+r
    p=p*r
    t=t//10
d=p-s
print(d)
    