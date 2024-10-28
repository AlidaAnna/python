num=input("Enter a word")
countd=0
countc=0
for i in num:
    if(i.isdigit()):
        countd=countd+1
    else:
        countc=countc+1
print(countd)
print(countc)