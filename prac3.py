a=int(input("Enter a number to check Prime number or not: "))
flag=0

if(a==0 or a<0):
    print("You can't enter 0 or less then 0")
elif(a==1):
    print("You can't enter 1")
else:
    for i in range(1,a+1):
        if(a%i==0):
            flag+=1


if(flag==2):
    print(a,"is prime")
else:
    print(a,"is not prime")

