n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if(i%2!=0):
        b.append(i)
for j in a:
    if(j%2==0):
        b.append(j)
for k in b:
    print(k,end=' ')

        
        
    