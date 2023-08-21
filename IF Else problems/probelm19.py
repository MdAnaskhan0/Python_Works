#Take two int values from user and print greatest among them.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2: 
    print(num1,"is greatest.")
elif num2 > num1:
    print(num2,"is greatest.")
else:
    print(num1,"and",num2,"is equal.")

