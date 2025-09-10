year=int(input ("Enter a year: "))

# But historically, 1900 is NOT a leap year ❌ (because divisible by 100 but not 400).
if (year%4==0 and year%100!=0) or (year%400==0): 
    print(f"{year} is a leap year") 
else:
    print(f"{year} is not a leap year")