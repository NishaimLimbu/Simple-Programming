num = int(input("Enter a number to find its fabonacci series: "))
a, b = 0, 1
if num <0:
    print ("Please enter a positive integer")
elif num == 0:
    print ("Please enter a number greater than zero")
else: 
    print("Fibonacci series:")
    for i in range(num):
        c=a + b
        print(a, end=' ')    
        a=b
        b=c