num = int(input("Enter a Number: "))

lastdigit = num%10

if lastdigit % 3 == 0: 
    print("Divisible by 3.")

else:
    print("Not divisible by 3.")