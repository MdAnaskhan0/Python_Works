"""Triangle:

* 
* * 
* * * 
* * * *

"""

def main():
    n = int(input("Enter a number: "))
    triangle(n)
    
       
def triangle(n):
    for i in range (1,n+1):
        for j in range(1,i+1):
            print("*",end=(""))      
        print("\n")
        
main()
