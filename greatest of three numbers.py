a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

if a>b:
    if a>c:
        print(f"{a} is the greatest of {a,b,c}")
    else:
        print(f"{c} is the greatest of {a,b,c}")
else:
    if b>c:
        print(f"{b} is the greatest of {a,b,c}")
    else:
        print(f"{c} is the greatest of {a, b, c}")