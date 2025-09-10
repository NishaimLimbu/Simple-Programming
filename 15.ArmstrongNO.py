num=int(input("Enter a number: "))
sum=0
temp=num #to store the original number
while temp>0:
    digit=temp%10
    sum=sum+digit**3 #for 3 digit number
    temp=temp//10 #to remove the last digit
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")