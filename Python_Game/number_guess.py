import random

def main():
    rand_num = random.randint(1,20)
    guess_num = int(input("Enter a number between 1 to 20: "))
    check(guess_num, rand_num)
    
def check(guess_num, rand_num):
    count = 1
    while count <= 20:
        if rand_num == guess_num:
            print("Congratulations you win the game....!")
            print("Total try:",count,"times.")
            break
        elif guess_num > rand_num:
            print("Chose lowere number...!")
            guess_num = int(input("Enter a number between 1 to 10: "))
            count += 1
        elif guess_num < rand_num:
            print("Chose higher number...!")
            guess_num = int(input("Enter a number between 1 to 10: "))
            count += 1
        else: 
            print("Invalid Input...!")  
            guess_num = int(input("Enter a number between 1 to 10: "))
            count += 1
    
main()