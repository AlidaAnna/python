w=input("Enter a sentences")
se=input("Enter the word to search")
count=0
s=[]
l=w.lower()
s=l.split()
print(s)
for i in range(len(s)):
    if se==s[i]:
        count=count+1
print(count)

