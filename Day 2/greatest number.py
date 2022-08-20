#using if elif else statement to check greatest number among three number
num1 = input("Enter a First Number:")
num2 = input("Enter a Second Number:")
num3 = input("Enter a Third Number:")

if num1 > num2 and num1 > num3:
    print(num1,"is the greatest number.")
    
elif num2 > num1 and num2 > num3:
    print(num2,"is the greatest number.")
    
else:
    print(num3,"is the greatest number.")