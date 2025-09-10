num=int(input("Enter a number: ")) 

cbro=num**(1/3)
if cbro==int(cbro): 
    print(f"{num} is a perfect cube")
else:
    print(f"{num} is not a perfect cube")