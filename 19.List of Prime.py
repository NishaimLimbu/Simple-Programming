PN=[]
num=int(input("Enter the number of prime numbers you want: "))
n=2
while len(PN)<num:
    for i in range(2,n):
        if n%i==0:
            break
    else:
        PN.append(n)
    n=n+1
print(PN)   
