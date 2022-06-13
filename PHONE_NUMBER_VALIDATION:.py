n=int(input())
c=0
s=0
t=n
while t:
    r=t%10
    s=(s*10)+r
    t=t//10
    c+=1
if(c==10 and s%10!=0):
    print("Valid")
else:
    print("Invalid")
