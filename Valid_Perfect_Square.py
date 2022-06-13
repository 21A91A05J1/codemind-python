n=int(input())
for i in range(n):
    m=int(input())
    for j in range(1,m):
        if(j*j==m):
            print(True)
            break
    else:
        print(False)
    