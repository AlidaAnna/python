s=[[1,6],[5,1],[7,4]]
for i in range(0,len(s)):
     for j in range(0,len(s)-i-1):
          if s[j][1]>s[j+1][1]:
                temp=s[j]
                s[j]=s[j+1]
                s[j+1]=temp
print(s)
   