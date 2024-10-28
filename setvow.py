vow=input("Enter a string")
vows=vow.lower()
count=0
set1={"a","e","i","o","u"}
for char in vows:
        if  char in set1:
                count=count+1
print (count)
