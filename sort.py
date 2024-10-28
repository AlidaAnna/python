s=[2,5,3,8,1]
for i in range(0,len(s)):
    for j in range(0,len(s)-i-1):
        if s[j]>s[j+1]:
            temp=s[j]
            s[j]=s[j+1]
            s[j+1]=temp
print(s)