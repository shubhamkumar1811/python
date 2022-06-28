t=int(input("enter range for fibbonaci: "))

def fibbo(t):
    if(t<=1):
        return t
    else:
        return (fibbo(t-1)+fibbo(t-2))

if (t<0):
    print("Enter Positive number! ")
else:
    for i in range(t):
    print(str(fibbo(i)))
