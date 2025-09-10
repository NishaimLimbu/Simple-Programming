num = int(input("Enter a number: "))

sqro = num ** 0.5
if sqro == int(sqro):
    print(f"{num} is a perfect square")
else:  
    print(f"{num} is not a perfect square")
print (sqro) # its in float
print (int(sqro)) # its in integer