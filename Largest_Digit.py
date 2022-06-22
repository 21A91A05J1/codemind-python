n=int(input())
max=0
t=n
while t:
    r=t%10
    if r>=max:
        max=r
    t=t//10
print(max)