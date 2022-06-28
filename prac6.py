t=int(input("enter range for fibbonaci"))

def fibbo(t):
    if(t<=0):
        return 1
    else:
        return fibbo(t-1)+fibbo(t-2)
    
for i in range(1,t+1):
    print(str(fibbo(i)))