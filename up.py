s=input("Enter a string")
cu=0
cl=0
for i in s:
    if i.isupper():
        cu=cu+1
    else:
        cl=cl+1
print(cu)
print(cl)