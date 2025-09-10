str = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = 0
for char in str:    
    print (char)
    if char in vowels: 
        count=count+1
print(f"Number of vowels: {count}") 
