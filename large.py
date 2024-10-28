a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if (a>b) and (a>c):
    print(f"{a}is greater than {b} and {c}")
elif  (b>c):
    print(f"{b}is greter than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")