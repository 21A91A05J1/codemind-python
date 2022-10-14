s=input()
t='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'
r=''
for i in range(len(s)):
    if(s[i]!=' '):
        t+=s[i]
    if(s[i]==' ' or i==len(s)-1):
        r+=''.join(reversed(t))
        if(i!=len(s)-1):
            r+=' '
        t='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'
print(r)